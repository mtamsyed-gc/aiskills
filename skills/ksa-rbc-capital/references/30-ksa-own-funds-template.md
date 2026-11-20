# KSA RBC: Own Funds and Solvency Assessment Template (eligible own funds, tiering, MCR)

Load for anything about available capital under KSA RBC: what counts as own funds, tiers and their limits, the deductions and additions (net RA, net CSM, goodwill, intangibles, deferred tax, dividends, own shares), the MCR, and the RBC solvency ratio as the IA now defines it.

Source: Insurance Authority (IA) "RBC Own Funds and Solvency Assessment Template", Q3 2026 edition (workbook `RBC_Own_Funds_and_Solvency_Assessment_Template_Q3_2026.xlsx`; sheets `1-Instructions` (Arabic), `2-Own Funds & Solvency`, hidden `3-Financial Projection`). This is the separate "Own Funds assessment and reporting template" that the Solvency and Capital Template refers to (SCA.04 change 11, SCA.07 `Projected RBC`). Every value is **[DRY RUN] [TEMPLATE]** until the final 2027 regulation. Cell references such as `[OF!B94]` are on sheet `2-Own Funds & Solvency`. Amounts in SAR thousands. Columns: B = Q3 2026 (current quarter), C = YE 2025. Recomputed in LibreOffice on 20 Nov 2026 with the worked example below: all cells match.

---

## 30.1 Instructions sheet (translated from Arabic)
- Title: "Available capital and solvency ratio template under the risk-based capital methodology".
- Company details: company, preparer, job title, email, phone.
- Every field must be filled.
- **Each own-funds component must be entered separately, according to the company's own capital structure** (rows marked "[Company to specify]").
- The company is responsible for checking the accuracy of the data before submission.
- Two governance questions, each with evidence to attach: (1) were the finance, risk management and actuarial functions all involved in preparing the template, and what was each one's role? (2) was the available capital presented to and discussed by the Board and its relevant committees, and what were their roles?

## 30.2 Company type and the MCR [Schedule 1]
Dropdown `[OF!B9]`: Insurance Company; Reinsurance Company; Captive Insurance Company; Captive Reinsurance Company. (An "Insurance and Reinsurance Company" floor exists in the check formula, but that option is not in the dropdown list.)

```
RBC  = input [OF!B17]                                   (must equal RBC!S65 of the Solvency and Capital Template)
MCR  = RBC / 3                                          [OF!B16]
MCR floor check [OF!G16]: PASS if MCR ≥ floor, else FAIL
   floor (SR '000): Insurance 20,000 | Reinsurance 40,000 | Insurance and Reinsurance 40,000
                    Captive insurance 10,000 | Captive reinsurance 20,000
```
The floor is a check, not a floor on the MCR value: the MCR used in the tier tests stays RBC / 3 even when the check fails **[TEMPLATE]**. These SAR 10-40m floors are a different concept from the SAR 100m / 300m paid-up capital rules (file 28 K1).

## 30.3 Own funds and the ratio [Schedules 2, 3, 4, 5]
```
Own Funds [B24]            = Total Assets [B21] − Total Liabilities [B22] + Regulatory Adjustments [B23 = B116]
Basic own funds            : Tier 1 [B32 = Σ B33:B41], Tier 2 [B43 = Σ B44:B52], Tier 3 [B54 = Σ B55:B63]   (company lists each item)
Ancillary own funds        : Tier 2 [B67 = Σ B68:B76], Tier 3 [B78 = Σ B79:B81]
Total by tier [Schedule 5] : T1 = basic T1 ; T2 = basic T2 + ancillary T2 ; T3 = basic T3 + ancillary T3
Eligible Own Funds [B26 = B125] = Total Eligible Own Funds before adjustments [B124] + Total Adjustments [B116]
Solvency Ratio [B28]       = Eligible Own Funds / RBC
```
There is no ancillary Tier 1. Ancillary items (e.g. uncalled capital, letters of credit, guarantees, by analogy with Solvency II) are not defined by the template; it gives only the rows **[INTERP]**.

## 30.4 Tier limits [Schedule 6]
Against RBC (the sheet labels this block "SCR"):
```
Eligible T1   [B93]  = T1                                         (no limit)
Eligible T3   [B95]  = min( T3 , 15% × RBC )
Eligible T2   [B94]  = min( T2 , 50% × RBC − min(T3, 15% × RBC) )
Eligible T2+3 [B96]  = min( T2_elig + T3_elig , 50% × RBC )      (reported only; B94 already enforces it)
Before adjustments [B124] = T1 + T2_elig + T3_elig
```
Against the MCR:
```
Eligible T1 for MCR [B99]  = T1
Eligible T2 for MCR [B100] = min( T2 , 20% × MCR )
Tier 3 is not eligible for the MCR. The template computes no MCR coverage ratio and adds no adjustments on the MCR side.
```
Checks:
| Cell | Test | Result |
|---|---|---|
| B104 | T1 ≥ 50% × RBC | PASS / FAIL |
| B105 | eligible T3 ≥ 15% × RBC | FAIL / PASS |
| B106 | eligible T2+T3 ≥ 50% × RBC | FAIL / PASS |
| B109 | T1 ≥ 80% × MCR | PASS / FAIL |
| B110 | eligible T2 for MCR ≥ 20% × MCR | FAIL / PASS |

Same structure as Solvency II Delegated Regulation Art. 82 (T1 ≥ 50% SCR, T3 < 15%, T2+T3 ≤ 50%; MCR: T1 ≥ 80%, T2 ≤ 20%) **[INTERP]**.

## 30.5 Regulatory adjustments [Schedule "5 - Eligible Own Funds", rows 115-123]
```
Total Adjustments [B116] = + Net CSM [B117] + Net RA [B118]
                           − Company's own shares [B119] − Goodwill [B120]
                           − Foreseeable dividends over the next twelve months [B121]
                           − Intangible assets [B122] − Deferred tax [B123]
```
- Adjustments are added **after** the tier limits, so net RA and net CSM count in full and are not tiered, and the deductions are not taken from a particular tier **[TEMPLATE]**.
- Net RA and net CSM sit here since SCA.05, which removed them from the Solvency and Capital Template's `Projected RBC` sheet. Available capital = eligible own funds; do not add RA or CSM a second time.
- Deferred tax: the line does not say asset or liability, or net. Read it as a net deferred tax asset deducted, entered positive **[INTERP]**; confirm with the IA.
- Intangible assets are deducted here in full, and SCA.07 also charges 80% of recognised intangibles in market risk (file 21 section 4.7). On these templates they reduce the ratio twice, through available capital and through RBC **[TEMPLATE]**; raise it with the IA rather than adjusting it yourself.

## 30.6 Template behaviours to respect and flag
1. **Own Funds [B24] does not reconcile to the tiers.** B24 = assets − liabilities + adjustments; the ratio uses tiered items + adjustments [B125]. Nothing checks that Σ tiers = assets − liabilities. Reconcile them yourself.
2. **Cap checks fail at the cap.** B105, B106 and B110 compare the capped eligible amount with the cap using ≥, so they show FAIL whenever the company holds enough T3 / T2+T3 / MCR-T2 to reach the cap, even though the excess is simply not counted. Read FAIL as "limit binding", not as a breach.
3. **A blank column shows FAIL** on B105 / B106 (0 ≥ 0) and PASS on B104.
4. **The MCR floor is a check only** (30.2).
5. **No MCR ratio** and no adjustments on the MCR side (30.4).
6. **No tiering criteria.** Which instruments are T1, T2 or T3 (subordinated debt, letters of credit, uncalled capital, reconciliation reserve) is not defined; the company lists items. Expect the IA to publish criteria; until then any classification is **[INTERP]** and VERIFY.
7. **Block labels say "SCR"** where they mean RBC; two schedules are numbered 5.
8. **Hidden sheet `3-Financial Projection`** carries a full 2026 quarterly SOI with populated figures (insurance revenue about SR 21.8bn for 2026, net combined ratio about 98%) that are not referenced by any formula. They belong to an unknown insurer: treat as residue, never as a benchmark or as the company's own figures.

## 30.7 Worked example (test figures, SR '000; recomputed in LibreOffice 20 Nov 2026)
RBC 300,000 (so MCR 100,000). Tier 1 400,000; basic Tier 2 120,000 + ancillary Tier 2 30,000; basic Tier 3 40,000 + ancillary Tier 3 20,000. Adjustments: net CSM 5,000; net RA 20,000; own shares 2,000; goodwill 10,000; foreseeable dividends 15,000; intangibles 8,000; deferred tax 3,000. Total assets 1,000,000; total liabilities 600,000.

| Item | Value |
|---|---|
| T2 total / T3 total | 150,000 / 60,000 |
| Eligible T3 = min(60,000, 45,000) | 45,000 |
| Eligible T2 = min(150,000, 150,000 − 45,000) | 105,000 |
| Eligible before adjustments | 550,000 |
| Total adjustments = 25,000 − 38,000 | −13,000 |
| **Eligible own funds** | **537,000** |
| **Solvency ratio** = 537,000 / 300,000 | **179%** |
| Own Funds [B24] = 1,000,000 − 600,000 − 13,000 | 387,000 (does not reconcile: behaviour 1) |
| MCR side: T1 400,000; eligible T2 = min(150,000, 20,000) | 20,000 |
| Checks: T1 ≥ 50% RBC; T3; T2+T3; T1 ≥ 80% MCR; MCR T2 | PASS; FAIL; FAIL; PASS; FAIL (behaviour 2: limits binding) |
| MCR floor (insurer 20,000) | PASS |

## 30.7a Using it with the Solvency and Capital Template
- `Projected RBC` row 9 "Eligible Own Funds Available to Meet RBC" = [OF!B26] for the matching date; RBC row 8 = [OF!B17].
- Tier limits move with RBC: any action that lowers RBC (reinsurance included) also lowers the room for Tier 2 and Tier 3. A cedant relying on Tier 2 near the 50% limit gets less from capital relief than the ratio arithmetic alone suggests **[INTERP]**.
- Subordinated debt is the obvious Tier 2 candidate (IA statement, Apr 2026, file 28 K3); capacity for T2 + T3 = 50% of RBC, and for the MCR only 20% of MCR.
