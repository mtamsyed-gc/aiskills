# 05 Dashboard measures and recipes from the files

## 1. How the dashboard reads the files
Power BI loads the `csv\` (or `parquet\`) tables as they are; every calculation is a DAX measure. Relationships:

| From | Column | To |
|---|---|---|
| fact_member_month, fact_claims | LifeID | dim_life (LifeID) |
| fact_member_month | MonthStart | Date |
| fact_claims, ultimates | IncurredMonth | Date |
| fact_member_month, fact_claims, ultimates | UWY / TPA / Payer Name | UW Year / TPA / Payer dimensions |
| cf_selected, recon, exceptions, diagnostics, dq_recon_scope | TPA | TPA |

So a dashboard UW year means **each fact's own UWY** (premium: life-period UWY; claims: assigned claim UWY), and a
dashboard month means **MonthStart** for premium and **IncurredMonth** for claims.

## 2. Bases and the experience cut
- **Premium basis** Gross / Net: slicer, else the run default (`run_manifest_premium` `default_premium_basis`, else Net).
- **Claims basis** Paid / Incurred (paid + outstanding; default) / Ultimate.
- **Reserve basis** IBNR (ultimate from paid + pending; default) / IBNP (ultimate from paid; Outstanding shown as 0).
- **Experience to** (month): slicer, else the report parameter `pExperienceTo`, else the valuation month; never after
  the valuation month. Claims incurred, premium earned and written premium booked up to it; ultimates are still
  developed to the same claims extract (it means "as known at the extract", not "as reported at that date").
- **Claims amount** Uncapped / Capped: Capped uses Paid and OS x PayerShareCapped / PayerShare.

## 3. Main measures (definitions)
| Measure | Definition | From the files |
|---|---|---|
| Written Premium | selected basis, booked up to Experience-to | Σ fact_member_month.WrittenPrem_<basis>, MonthStart <= cut |
| Earned Premium | earned to the cut, selected basis | Σ fact_member_month.EarnedPrem_<basis>, MonthStart <= cut |
| Written LY / Earned LY | life-years written / earned; zero-premium life-periods excluded | Σ WrittenLY_<basis> / EarnedLY_<basis>, MonthStart <= cut |
| Lives Earned | life-periods with earned days | distinct LifeID with EarnedDays > 0, MonthStart <= cut |
| Paid | payer share paid, claims treated by the cut | Σ fact_claims.Paid, InExperience = 1, IncurredMonth <= cut |
| Outstanding (Case) | TPA-reported outstanding, any reserve basis | Σ fact_claims.OS, same filter |
| Reported Claims | Paid + Outstanding (Case) | |
| Incurred | Paid + Outstanding (IBNR basis) / Paid (IBNP basis) | |
| Ultimate Claims | sum of claim-level ultimates on the reserve basis | Σ UltimateAmount (IBNR) or UltimateAmount_IBNP (IBNP), same filter |
| IBNR / IBNP | Ultimate - (paid + pending) / Ultimate - paid | |
| Claim Count | counted visits | Σ CountFlag, same filter |
| Ultimate Claim Count | count ultimates | Σ UltimateCount (or _IBNP), same filter |
| Loss Ratio | claims (selected basis) / earned premium (selected basis); also Paid LR, Incurred LR, Ultimate LR | |
| Frequency | claims per earned life-year | Claim Count / Earned LY |
| Burning Cost per LY | claims / earned LY (= frequency x severity) | |
| Gain / Loss | earned premium - claims, selected bases | |
| Earned Premium per LY / PMPM | average premium per earned LY / per member-month | |
| Match Rate (Count / Amount) | from recon_claims; red below 95% | see 03-control-tables |

Two adjustments can make the dashboard differ from a plain file sum, and both are visible on its pages: a
pre-adjudication basis other than Full claimed (changes reported outstanding and counts only), and UWY ultimate
adjustment factors on the Adjustment factors page (100% = none). Ask which are set before reconciling.

## 4. Recipes (pandas)
Read every key column as text. CSV in the LenAI Python sandbox (no Parquet there); Parquet or CSV with native `py`.
```python
import pandas as pd
o = r"<client>\04_Outputs\csv"
dl = pd.read_csv(f"{o}\\dim_life.csv", dtype={"LifeKey": str, "UWY": int})
mm = pd.read_csv(f"{o}\\fact_member_month.csv", dtype={"LifeKey": str}, parse_dates=["MonthStart"])
fc = pd.read_csv(f"{o}\\fact_claims.csv", dtype={"LifeKey": str, "ClaimKey": str, "ClaimID": str},
                 parse_dates=["IncurredMonth"])
man = dict(pd.read_csv(f"{o}\\run_manifest_claims.csv", dtype=str).values)
assert man.get("contract_version") == "IP4-13", man.get("contract_version")
cut = pd.Timestamp(man["valuation_date"]).to_period("M").to_timestamp()   # or the experience-to month
basis = "Net"                                                              # or "Gross"
```
**Ultimate loss ratio by UW year x TPA (drill-across, never join the facts):**
```python
prem = (mm[mm.MonthStart <= cut].groupby(["UWY", "TPA"])[[f"EarnedPrem_{basis}", f"EarnedLY_{basis}"]].sum())
clm = (fc[(fc.InExperience == 1) & (fc.IncurredMonth <= cut)]
       .groupby(["UWY", "TPA"])[["Paid", "OS", "UltimateAmount", "CountFlag"]].sum())
t = prem.join(clm, how="outer").fillna(0)
t["Incurred LR"] = (t.Paid + t.OS) / t[f"EarnedPrem_{basis}"]
t["Ultimate LR"] = t.UltimateAmount / t[f"EarnedPrem_{basis}"]
t["Freq per 1,000 LY"] = 1000 * t.CountFlag / t[f"EarnedLY_{basis}"]
```
**Cut by a member attribute** (e.g. Policy Type): attach the attribute to each fact on `LifeKey` + `UWY` (one row per
key in dim_life, so the join cannot duplicate), then aggregate as above.
```python
attr = dl[["LifeKey", "UWY", "Policy Type"]]
fc2 = fc.merge(attr, on=["LifeKey", "UWY"], how="left", validate="many_to_one")   # unlinked lines keep NaN
assert len(fc2) == len(fc) and abs(fc2.Paid.sum() - fc.Paid.sum()) < 0.01         # join invariance
```
**Written premium by UW year that ties to recon_premium:** Σ `fact_member_month.WrittenPrem_<basis>` with no month
cut = Σ `dim_life.WrittenPrem_<basis>` = `recon_premium` WrittenPrem_<basis> per TPA.

## 5. Traps (each has caused a real wrong answer)
| Trap | Effect | Do instead |
|---|---|---|
| Join on LifeKey without UWY | claims or premium counted once per UW year of the member | join on LifeKey + UWY (or LifeID within one run) |
| Join fact_claims to fact_member_month | claims x months fan-out | aggregate each, then join the aggregates |
| Sum earned premium from dim_life for an experience-to cut | dim_life earns to the valuation date | use fact_member_month with MonthStart <= cut |
| Count rows or ClaimKey as claims | frequency inflated for TPAs that split visits | Σ CountFlag |
| Forget InExperience = 1 | claims treated after the valuation date included | filter it |
| Mix Gross premium with a Net run default | LR off by the commission / fee gap | state and use one basis |
| Pivot raw premium by approval date or a UWY column | UW year mismatch | UWY = year of the policy coverage start date |
| Compare written premium at a cut with a raw pivot | refunds book in the month after the last covered day | prove the tie with no cut first, then apply the cut |
| Use LifeID to compare two runs | renumbered every run | LifeKey + UWY |
| Sum OS across extracts or months as a flow | OS is a balance at the extract | use it at one extract only |
| Read the `_excluded` tables into totals | adds scope-excluded business | main tables only |
| Treat fine-cut ultimates as precise | factors are per TPA x lag | call them indicative below payer x TPA x UWY x month |
