# KSA RBC: Template mechanics: legacy solvency sheet, financial statements, summary of results, validations, governance and template behaviours

Load when reproducing or reviewing a company's filled template, reconciling a number, or explaining why the template shows a result that differs from the rule as written.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", built from version SCA.04 (issued 2026-02-25, run "Risk Based Capital 5th Dry Run (2025YE)") as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026), **updated to SCA.07** (issued 2026-11-16, valuation 30 Sep 2026, `Solvency_and_Capital_Template_2026Q3_vSCA.07.xlsx`; every factor and matrix re-read from the SCA.07 workbook on 20 Nov 2026, changes in file 29). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 12. Regulatory Solvency sheet (current/legacy solvency margin basis)

Reported for 2025 actual, the current quarter actual (2026Q3 in SCA.07) and 2026 projected. This is separate from the RBC and is not an input to it. All line items are inputs; the sheet only adds them up.

```
Total Admissible Assets = Admissible assets policyholders (G&H) + policyholders (P&S) + shareholders
                          + adjustments + other assets allowed to cover the required minimum margin
Total Liabilities       = Policyholders liabilities (G&H) + (P&S) + shareholders liabilities
                          − liabilities allowed to be left out in covering the minimum margin
Net assets by fund      = admissible assets − liabilities, for G&H policyholders, P&S policyholders, shareholders
Adjustments line        = adjustments + other assets allowed + liabilities allowed to be left out
Total Net Admissible Assets = Σ three net-asset lines + adjustments line

Required margin (G&H)   = max( claims-method margin , premium-method margin )        (both inputs)
Total Required Margin   = Required margin (G&H) + Required margin (P&S)               (P&S input)
Required Minimum Margin = max( Total Required Margin , Minimum Capital Requirement )  (MCR input)
Excess/(deficiency)     = Total Net Admissible Assets − Required Minimum Margin
Solvency Ratio          = Total Net Admissible Assets / Required Minimum Margin
```

"Basis for Required Solvency Capital" is selected per year from: Premium-based; Claims-based; Minimum Capital; Article 67-based (P&S). The template does not contain the premium-method or claims-method formulas or the admissibility percentages.

---

## 12A. Reinsurance Impact sheet (new in SCA.07)

Purpose: quantify the capital relief from reinsurance as **gross minus net standard-formula results**. The company runs a **separate standard-formula calculation on gross-of-reinsurance data** and types the gross results into column B; the net column links to the RBC sheet.

| Row | Gross (input) | Net (link) | Impact |
|---|---|---|---|
| Counterparty default | B6 | RBC!S18 | B − C |
| Life UW | B7 | RBC!S26 | B − C |
| Non-life UW and short-term group life | B8 | RBC!S57 | B − C |
| – Premium risk / – Reserve risk / – CAT risk | B9 / B10 / B11 | RBC!S30 / S33 / S54 | B − C |
| Total before inter-module diversification | Σ B6:B8 | Σ C6:C8 | |
| Total after inter-module diversification | sqrt(vᵀ · M5[CD, Life, NonLife] · v) | same on net | |
| Overall RBC | B14 input (overall diversified RBC of the gross run) | RBC!S65 | B − C |

Gross basis rules (Instructions): premium, reserve and life UW on gross figures with no reinstatement-premium or sliding-scale effect; CAT with no recoveries, reinstatements or sliding commission; counterparty default **excluding** exposures arising from reinsurance (banks and Type 2 stay). Market and operational risk are not shown (reinsurance does not move them in the formula). The validations only check that the gross cells are filled.

Reading it [INTERP]: this is the template's own "capital relief from reinsurance" line, so the IA will see each treaty's effect by module every quarter. A per-person medical XoL shows almost no premium-risk relief (its only effect is the lower net premium); a quota share shows relief in premium and reserve risk, partly offset by a higher counterparty charge; cat XoL shows in CAT risk. Expect questions on structures whose impact is large relative to their cost.

---

## 13. Financial statements captured [SOFP, SOI]

SOFP is entered for three segments — General & Health; P&S non-linked; P&S linked — each split into Insurance Operations and Shareholders' Operations for actual years to 2025 and the current quarter (2026Q3 in SCA.07), and totals for projections 2026–2029; "Total Insurance" = sum of the three segments.

Assets: insurance contract assets; reinsurance contract assets; financial assets for unit-linked contracts; cash and cash equivalents; term deposits; statutory deposit; accrued income on statutory deposit; investments (incl. accrued investment income); own property and equipment, net; prepaid expenses and other assets; deferred tax asset; intangible assets; goodwill.

Liabilities: insurance contract liabilities; reinsurance contract liabilities; investment contract liabilities; accrued income payable to IA; accrued expenses and other liabilities; current liabilities (incl. short-term borrowings); EOSB provision; provision for zakat and income tax; dividends payable; deferred tax liability.

Equity: share capital; statutory reserve; fair value reserve for investments; retained earnings; re-measurement of EOSB obligations; share premium; insurance finance reserves; other reserves.

SOFP items used by the RBC calculation (valuation-date total insurance): total assets and total liabilities (interest rate base values and reconciliation), investments and own property & equipment (concentration asset base and market KPI).

SOI (2024–2025 actual, 2026–2028 projected): insurance revenue; insurance service expenses; reinsurance premium allocation and recoveries; insurance service result; investment income lines; net insurance finance result; FX and other movements; other income/expenses; net income before and after zakat & tax. SOI does not feed the RBC.

Projection columns are on a best-efforts basis.

---

## 14. Summary of results conventions

For each of 28 sub-modules the summary holds four ΔNAV figures (negative = loss): undiversified before risk mitigation; diversified before; undiversified after; diversified after; plus ranks (1 = largest loss). "Diversified" at this level means only geographical diversification and diversification inside the sub-module itself — LOB-level and cross-sub-module diversification happen on the RBC sheet.

| Sub-module | Before vs after risk mitigation differs by | Undiversified vs diversified differs by |
|---|---|---|
| Interest rate | Risk mitigation allowance | — |
| Equity | — | Matrix 6 |
| Property | — | Matrix 7 + independence of KSA / outside / P&E |
| Spread | — | — |
| Concentration | — | Root-sum-square over issuers |
| Currency | Risk mitigation allowance | — |
| Intangibles | — | — |
| CD Type 1 | Payables and collateral | Matrix 17 |
| CD Type 2 | Payables | — |
| Life sub-risks | — | — |
| Premium risk | Reinstatement premium + sliding commission | Geographical diversification |
| Reserve risk | — | Geographical diversification |
| Man-made CAT, pandemic | Reinsurance | — (credit & surety: root-sum-square of default and recession) |
| Natural CAT | Reinsurance | Regional correlation / outside-KSA formula |
| Operational | — | — |

---

## 15. Validations and governance

### 15.1 Reconciliation and sense checks (Pass/Fail)

1. Bonds: bonds classified in interest rate risk = total spread-risk exposure = (concentration exposures typed Bonds + Equities and Bonds + Equity) − total equity investments.
2. Property: Σ within-KSA property value in property risk = Σ concentration exposures with issuer type Property.
3. Equity: total equity investments = (concentration Bonds + Equities and Bonds + Equity) − total spread exposure.
4. SOFP total assets (YE2025) = Σ classified assets in the interest rate table; SOFP total liabilities = Σ classified liabilities.
5. Life UW: the exposure entered for mortality, lapse, expense and morbidity must be identical (zeros ignored).
6. Scenario exposures: outside-KSA property, energy and engineering premium totals must agree across flood, earthquake and windstorm; motor sum insured (KSA) and motor premium (outside) must agree between flood and hail; health pandemic number of lives = Σ sandstorm health insureds.
7. LOB allocation NEP vs premium-risk NEP (section 11.1).
8. Concentration: Σ exposures = asset base.
9. Counterparty default: Σ reinsurer shares of risk-mitigating effect within 1% of TotalRME.
10. Interest rate: Σ discounted cash flows ≥ classified in-scope assets/liabilities.
11. Completeness: every input cell on every tab populated (0 if not applicable); AF contribution and sign-off record complete.

### 15.2 Actuarial Function contribution

| Aspect | Options → weight | Max |
|---|---|---|
| Data provision | Low 2.5% / Significant 5% / Full responsibility 10% | 10% |
| Data validation | Low 2.5% / Significant 5% / Full responsibility 10% | 10% |
| Analysis | Limited 10% / Significant 30% / Major 50% | 50% |
| Report review or preparation | Review only 5% / Limited contribution in preparation 10% / Significant 15% / Major 20% | 20% |

Total involvement = sum of the four selected weights (maximum 90%).

### 15.3 Sign-off record

Must match the Sign-off Certificate submitted to the IA as PDF. Areas: Own Funds results (tiering and calculation); RBC results — market risk; non-life underwriting risk (incl. health, short-term life and CAT scenarios); life underwriting risk; counterparty default risk; operational risk. For each: department, name, title, expert judgments used, comments.

### 15.4 Comments tab

Free-text company and Appointed Actuary comments by sheet and risk module.

---

## 16. Template behaviours to respect and flag

These are how the workbook actually behaves (checked on SCA.07, 20 Nov 2026). Reproduce them when replicating template output and tell the user when one affects a result.

1. **Operational risk is zero until the cybersecurity score is entered.** With the score blank, the loading cell shows a text prompt and the final operational ΔNAV evaluates to 0.
2. **Spread — "Other Governments" with rating "Unrated"** returns blank (no charge): Table S2 has no Unrated column.
3. **Spread — PSE (with sovereign guarantee)** always uses rating A, whatever rating is entered.
4. **Spread — blank or invalid inputs** (missing duration, rating or issuer type) produce a blank stress factor and zero loss, with no error shown.
5. **Concentration thresholds** are looked up by rating from the Corporate Inside KSA row for every non-property issuer type. The 100% threshold shown for KSA Government is not used; KSA Government has no charge because its factor is 0.
6. **Concentration — missing rating** on a non-property exposure gives zero excess (no charge).
7. *(Retired in SCA.05.)* Windstorm recoveries were left out of TotalRME in SCA.04; since SCA.05 `Counterparty Default!C8` includes them, so every CAT scenario now feeds the risk-mitigating effect.
8. **Counterparty Type 1** net loss deducts payables and collateral from the *loss*, not from the exposure, floored at zero per counterparty. Diversification is by row: rows are assumed 0.25 correlated, so one counterparty split across rows receives diversification credit.
9. **Interest rate, top-down**: stressed asset and liability values are inputs. Stressed rates are blank for non-integer durations below 1 year.
10. **Interest rate, bottom-up**: for the 30+ year bucket the stressed values are manual inputs; if left blank while base cash flows are entered, the whole base value appears as a loss (assets) or gain (liabilities).
11. **Interest rate**: top-down and bottom-up losses are added; each is floored at zero separately.
12. **Flood — property**: only ground-floor sum insured is stressed.
13. **Premium risk** "after risk mitigation" is *higher* than "before" when reinstatement premium and sliding-scale commission impacts are positive.
14. **Marine and aviation scenarios** return zero if the hull (and cargo) exposure inputs are zero, even if other cost items are entered. **Motor** returns zero unless the applicability flag is "Yes".
15. **Health pandemic**: health and life net losses are added with no diversification.
16. **Intangibles** are added to market risk without diversification.
17. **Life UW** charges are floored at zero per sub-risk; lapse takes the worst of the three scenarios.
18. **LOB naming**: LOB14/LOB15 are labelled "Individual – Protection" / "Individual – Protection & Savings" in the dropdown list but "Individual Life – P&S" / "Individual Life – Protection" in the LOB-wise Allocation sheet.
19. **Summary "undiversified" for premium risk** before mitigation is the plain sum of LOB losses before geographical diversification; after mitigation it is the sum including reinstatement premium and sliding commission, also before geographical diversification.
20. **Operational risk KPI** on the RBC sheet uses the provision-based charge (3% / 0.45% × TP) in its denominator where the label says gross technical provisions.
21. **Reconciliation checks use exact equality** (no tolerance), except the reinsurer risk-mitigating-effect check (1%).
22. **Reinsurance Impact gross column is typed, not calculated** (section 12A): nothing checks that the gross run used the same exposures, so a gross RBC below net RBC goes through. Check the sign of every impact.
23. **Reinsurance Impact "Total after inter-module diversification"** uses only the CD / Life / Non-life block of Matrix 5 (no market), so it is not comparable with Basic RBC.
24. **Projected RBC no longer has Net RA / Net CSM rows** (SCA.05): available capital is eligible own funds from the Own Funds template (file 30). An SCA.04-era model that adds RA and CSM on top double-counts them.
25. **Intangibles are hit twice** across the two templates: 80% charge in market risk here and a full deduction in eligible own funds (file 30 section 30.5).
26. **Quarterly basis:** the projected-NEP reconciliation between LOB-wise Allocation and premium risk is greyed out (not applicable to quarterly submissions); duplicate-entry and dropdown validations exist on the Market and Counterparty Default tabs (SCA.05); exposure by region must equal total exposure for premium and reserve risk (SCA.06).
