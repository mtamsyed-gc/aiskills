# KSA RBC: Framework, aggregation, operational risk and the RBC solvency ratio

Load for any KSA RBC question: how the modules fit together, the aggregation rule, rating buckets and lines of business, operational risk, available capital and the ratio, LOB allocation, KPIs and the calculation order.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 1. Scope, basis and general conventions

| Item | Rule |
|---|---|
| Regulator | Insurance Authority, Kingdom of Saudi Arabia (contact in template: Actuarial@ia.gov.sa) |
| Valuation date | 31 December 2025 (YE2025). The YE2025 solvency ratio is the "Base". |
| Units | All amounts in SAR thousands (SR '000). |
| Accounting basis | IFRS 17 / IFRS 9 balance sheet (SOFP) values. |
| Calibration | All calibrations are at the 99.5th percentile. Premium and reserve risk factors for direct and proportional business are on a one-year view (emergence-pattern approach: 95% for Motor and Health, 90% for other LOBs applied to ultimate-view factors). |
| Asset/liability values in stresses | As at YE2025. |
| Exposure data for scenarios | Relate to calendar year 2026 (e.g. largest exposures may be written in 2025 and partly earned in 2026, or written in 2026 and expiring in 2027). |
| Risk mitigation | Where allowed, based on **existing** risk mitigation arrangements only. |
| Sign of inputs | Use a negative sign for a reduction in NAV. Liabilities are input as positive values. |
| Empty cells | Cells must not be left empty; enter 0 when not applicable. |
| Pools | Treated like any other exposure: apply all relevant stresses to the company's share of the pool's assets and liabilities (information from the pool leader). |
| Technical provisions used as exposure | Discounted and **excluding Risk Adjustment (RA) and CSM** wherever technical provisions are an exposure measure (LOB allocation, non-life UW, operational risk, life UW, counterparty default Type 1). |
| Admissibility | Admissibility rules have no effect on RBC calculations (removed in SCA.03). |
| Inapplicable stresses | If a stress/scenario is considered not applicable, the company must list tab, stress name and reason in the Instructions tab. |

### 1.1 Workbook map

| Sheet | Role |
|---|---|
| Instructions | General rules, rating mapping, region definitions |
| Version | Change log |
| Sign-off Record, Comments, AF contribution | Governance |
| Validations | Completeness, reconciliation and sense checks |
| SOFP, SOI | IFRS balance sheet and income statement, actual 2023–2025 and projections 2026–2029 |
| Regulatory Solvency | Current (legacy) solvency margin basis — separate from RBC |
| RBC | Aggregation of all modules to the Risk-Based Capital; KPIs |
| Projected RBC | Own Funds, Net RA, Net CSM, RBC and RBC solvency ratio, actual and projected |
| LOB-wise Allocation | Allocation of RBC to 16 lines of business |
| Market, Counterparty Default, Non-Life & Short Term P&S UW, Life UW, Op risk | Stress-test modules |
| Scenarios | Catastrophe scenarios (health pandemic, 5 natural CAT, 6 man-made CAT) |
| Summary of results | Collects ΔNAV by sub-module, before/after risk mitigation |
| Correlations | 17 correlation matrices |
| Input Collation | Read-only collation of inputs (no calculations affecting RBC) |
| Comparison with SII | Narrative comparison with Solvency II |
| Dropdown (hidden) | Lists used for data validation |

---

## 2. Framework structure

```
RBC  =  Basic RBC (diversified)  +  Operational risk
Basic RBC = aggregate[ Market, Counterparty Default, Life UW, Non-Life UW ]          (Matrix 5)

Market            = aggregate[ Interest rate, Equity, Property, Spread, Concentration, Currency ] (Matrix 1)
                    + Intangible assets (added linearly, outside the matrix)
Counterparty Def. = aggregate[ Type 1 (reinsurers & banks), Type 2 (other counterparties) ]     (Matrix 4)
Life UW           = aggregate[ Mortality, Lapse, Expenses, Morbidity/Disability ]               (Matrix 2)
Non-Life UW       = aggregate[ Premium risk, Reserve risk, CAT ]                                (Matrix 3)
   Premium risk   = aggregate over LOB1..LOB13                                                  (Matrix 15)
   Reserve risk   = aggregate over LOB1..LOB13                                                  (Matrix 16)
   CAT            = aggregate[ Man-made CAT, Health Pandemic, Natural CAT ]                      (Matrix 10)
      Man-made    = aggregate[ Energy, Property, Motor, Marine, Aviation, Credit & Suretyship ] (Matrix 8)
      Natural     = aggregate[ Pluvial Flood, Earthquake, Hail, Sandstorm, Windstorm ]          (Matrix 9)
```

"Non-Life UW" covers general insurance, health insurance and **short-term (one-year) group life / group credit life** (LOB11–LOB13). "Life UW" covers long-term Protection & Savings business only and excludes one-year group life and group credit life.

### 2.1 Aggregation rule

For a vector of positive charges `x` and correlation matrix `C`:

```
aggregate(x, C) = sqrt( xᵀ · C · x ) = sqrt( Σ_i Σ_j C[i,j] · x_i · x_j )
```

Diversification benefit at any node = (sum of inputs) − (aggregated result).

All inputs to the aggregation on the RBC sheet are the **"Diversified change in NAV AFTER risk mitigation"** values from the Summary of results (column G), sign-flipped.

### 2.2 Top-level formulas [RBC sheet]

```
Market        = aggregate([IR, Equity, Property, Spread, Concentration, Currency], M1) + Intangibles   [S12]
CD            = aggregate([Type1, Type2], M4)                                                          [S18]
LifeUW        = aggregate([Mortality, Lapse, Expenses, Morbidity], M2)                                 [S26]
Premium       = aggregate(PremiumLoss_LOB[1..13], M15)                                                 [S30]
Reserve       = aggregate(ReserveLoss_LOB[1..13], M16)                                                 [S33]
ManMadeCAT    = aggregate([Energy, Property, Motor, Marine, Aviation, Credit&Surety], M8)              [S42]
NatCAT        = aggregate([Flood, Earthquake, Hail, Sandstorm, Windstorm], M9)                         [S44]
CAT           = aggregate([ManMadeCAT, HealthPandemic, NatCAT], M10)                                   [S54]
NonLifeUW     = aggregate([Premium, Reserve, CAT], M3)                                                 [S57]
BasicRBC      = aggregate([Market, CD, LifeUW, NonLifeUW], M5)                                         [S61]
OpRisk        = see section 10                                                                         [S63]
RBC           = BasicRBC + OpRisk                                                                      [S65]
```

Reporting lines also on the RBC sheet:
- Total undiversified reduction in NAV at sub-module level = −Σ Summary of results column F (rows 5–32) [S66].
- Total diversification benefit within the model = S66 − RBC [S67].

Because M8, M9 and M10 are identity matrices, ManMadeCAT, NatCAT and CAT each reduce to the square root of the sum of squares of their components.

---

## 3. Credit rating mapping and lists

### 3.1 External rating → rating bucket

| Bucket | AM Best | Moody's | Fitch | S&P |
|---|---|---|---|---|
| AAA | aaa | Aaa | AAA | AAA |
| AA | aa+, aa, aa− | Aa1, Aa2, Aa3 | AA+, AA, AA− | AA+, AA, AA− |
| A | a+, a, a− | A1, A2, A3 | A+, A, A− | A+, A, A− |
| BBB | bbb+, bbb, bbb− | Baa1, Baa2, Baa3 | BBB+, BBB, BBB− | BBB+, BBB, BBB− |
| BB | bb+, bb, bb− | Ba1, Ba2, Ba3 | BB+, BB, BB− | BB+, BB, BB− |
| B | b+, b, b− | B1, B2, B3 | B+, B, B− | B+, B, B− |
| CCC and below | ccc, cc, c | Caa, Ca, C | CCC, CC, C | CCC, CC, C |

KSA sovereign rating used by the template: **A+ (bucket A)**, based on Fitch (17 Jan 2026) and S&P (14 Mar 2025); subject to update when the rating changes.

### 3.2 Enumerations

- **Issuer type (spread):** KSA Government; Other Governments; PSE (with sovereign guarantee); Corporate Inside KSA; Corporate Outside KSA.
- **Issuer type (concentration):** the five above plus Property.
- **Exposure type (concentration):** Equity; Bonds; Equities and Bonds; Property.
- **Rating buckets (spread):** AAA; AA; A; BBB; BB; B and CCC or below; Unrated.
- **Rating buckets (concentration):** AAA; AA; A; BBB; BB; B; CCC or below (incl. unrated).
- **Rating buckets (counterparty Type 1):** AAA; AA; A; BBB; BB; B; Other (Incl. Unrated).
- **Counterparty type (Type 1):** Bank; Reinsurer; Other financial institution.
- **Counterparty type (Type 2):** Broker; Agent; TPA; Policyholder; Insurance Company; Others.
- **Foreign currency type:** USD-Pegged Currency (GCC); USD-Pegged Currency (Non-GCC); USD (given SAR pegging); Other Currencies.
- **Risk mitigation type (currency):** None; Currency forwards; Currency options; Currency swaps; Other.
- **Risk mitigation type (interest rate):** None; Interest rate swap; Interest rate cap; Interest rate floor; Interest rate collar; Other.
- **Fund asset class (look-through table):** Equity; Bond; Real Estate; Term Deposit; Cash and Cash Equivalents.
- **Fund treatment:** Using look-through approach (preferred); Treated as equity, excluded from concentration risk; Both.
- **Look-through basis:** Actual investments; Mandate; Blend of both.

### 3.3 Lines of business

| Code | Name | Module |
|---|---|---|
| LOB1 | Accident & Liability | Non-Life UW |
| LOB2 | Motor Compulsory | Non-Life UW |
| LOB3 | Motor Compulsory + Others | Non-Life UW |
| LOB4 | Property | Non-Life UW |
| LOB5 | Marine | Non-Life UW |
| LOB6 | Aviation | Non-Life UW |
| LOB7 | Energy | Non-Life UW |
| LOB8 | Engineering | Non-Life UW |
| LOB9 | Health Insurance (compulsory and non-compulsory) | Non-Life UW |
| LOB10 | Other General and Health Insurance products | Non-Life UW |
| LOB11 | Group Life | Non-Life UW (short term) |
| LOB12 | Group Credit Life | Non-Life UW (short term) |
| LOB13 | Group – Other | Non-Life UW (short term) |
| LOB14–16 | Individual Life (Protection & Savings; Protection; Other) | Life UW; appear only in LOB-wise allocation |

---

## 10. Operational risk [Op risk sheet]

Scenario narrative: ransomware attack during peak renewal period, systems down for several weeks, data accessed illegally.

| Segment | Premium factor | Provision factor |
|---|---|---|
| Non-life and short-term (group) life | 3% | 3% |
| Long-term life (individual & group) | 4% | 0.45% |
| Unit-linked long-term life | 25% of expenses incurred in the last year | — |

Inputs (all excluding unit-linked business): gross earned premium last year `GEP_prev` and projected for the current year `GEP_next`, per segment; discounted gross technical provisions excluding RA and CSM `TP`, per segment (must reconcile to the YE reserve reporting template); unit-linked expenses incurred during the last year `Exp_UL`; Cybersecurity Framework Compliance Score at YE2025 `Score` (0–1).

```
Op_premium   = 3% × max(GEP_prev, GEP_next)_nonlife  +  4% × max(GEP_prev, GEP_next)_longterm
Op_provision = 3% × TP_nonlife  +  0.45% × TP_longterm
Op_base      = min( 30% × BasicRBC , max(Op_premium, Op_provision) ) + 25% × Exp_UL
CyberFactor  = +5%    if Score < 50%
             = +2.5%  if 50% ≤ Score < 75%
             =  0     if 75% ≤ Score < 90%
             = −2.5%  if 90% ≤ Score < 100%
             = −5%    if Score = 100%
Charge_Op    = Op_base × (1 + CyberFactor)
```

BasicRBC here is the diversified Basic RBC of section 2.2. The 30% cap applies only to the premium/provision component, not to the unit-linked expense component.

---

## 11. RBC, available capital and solvency ratio

```
RBC = BasicRBC + Charge_Op                                           [RBC!S65 → Projected RBC!D8]
Available Capital = Own Funds + Net RA + Net CSM
RBC Solvency Ratio = Available Capital / RBC                         (0 if RBC is 0 or missing)   [Projected RBC row 12]
```

- **Own Funds**: input, must be consistent with the separate IA Own Funds assessment and reporting template (since SCA.04 it is no longer derived from SOFP net assets).
- **Net RA** (risk adjustment net of reinsurance) and **Net CSM** are added to available capital. CSM is relevant for insurers using GMM or VFA under IFRS 17.
- Columns: actual 2024YE and 2025YE; business-plan projections 2026YE–2029YE; optional **alternative projections** 2026YE–2029YE, required where the Appointed Actuary's assumptions (loss ratio, expense ratio, etc.) differ materially from management's.
- Only the 2025YE RBC is calculated by the template. RBC for other years and all capital items are inputs.
- Narrative inputs: drivers of the 2025YE vs 2024YE ratio change apart from calibration changes; drivers of projected ratio changes (2029YE vs 2025YE); drivers of alternative vs business-plan differences — in numerical terms (loss ratios, expense ratios, volumes) separately for each year.
- The template does not prescribe a minimum RBC ratio or supervisory ladder.

### 11.1 LOB-wise allocation of RBC [LOB-wise Allocation sheet]

For LOB1–LOB16 and each year 2025 (actual) and 2026–2029 (projected): inputs NEP and Net TP (discounted net technical provisions excluding RA and CSM).

```
Alloc_NEP(l)      = NEP_l / Σ NEP × RBC_year
Alloc_NEP+TP(l)   = (NEP_l + NetTP_l) / Σ (NEP + NetTP) × RBC_year
Alloc_AA(l)       = Appointed Actuary's own allocation (input)
```

RBC_year comes from the Projected RBC sheet (business-plan basis). Checks: 2025 NEP per LOB1–13 must equal `NEP_prev` in the premium risk module, and 2026 NEP must equal `NEP_next`.

### 11.2 Key ratios reported on the RBC sheet

Composition: each of Non-Life UW, Market, Credit (CD), Life UW, Operational as % of RBC; diversification benefit = BasicRBC/RBC − Σ(four module shares). Sub-module shares are also shown within Market, Life UW, Non-Life UW and CD.

Capital charge as % of exposure:

| Risk | Denominator |
|---|---|
| Non-Life UW | Σ premium exposure (DP + NP) + Σ reserve exposure (DP + NP) |
| Market | Investments + own property & equipment + intangible assets |
| Credit | Σ net Type 1 exposure + Σ risk-mitigating effect + Σ Type 2 receivables − Σ Type 2 payables |
| Operational | Labelled max(max gross EP, gross TP) + unit-linked expenses; the formula actually takes max(Σ per-segment max gross EP, provision-based operational charge) + unit-linked expenses |
| Life UW | abs(BEL net of RA & CSM) |

RBC as % of: max(NEP 2025, NEP 2026); max(gross EP prior, current); the same plus net/gross TP; and aggregate net/gross exposure (premium + TP + investments + PPE + intangibles + net credit & receivables + CAT risk-mitigating effect).

Diversification ratios: within Market (benefit/undiversified), Premium, Reserve; within sub-risks as `1 − diversified/undiversified` for Type 1 counterparty default, equity, concentration and each natural CAT peril.

---

## 17. Calculation order (algorithm)

1. Populate SOFP (YE2025 totals) → AssetBase, total assets, total liabilities.
2. Market: compute IR (4.1), Equity (4.2), Property (4.3), Spread (4.4), Concentration (4.5), Currency (4.6), Intangibles (4.7) → Market (4.8).
3. Scenarios: compute each CAT scenario gross and net (section 8); collect scenario recoveries → TotalRME (5.1).
4. Counterparty default: allocate TotalRME to reinsurers; compute Type 1, Type 2 → CD (section 5).
5. Life UW: four sub-risks → LifeUW (section 6).
6. Non-life: premium and reserve losses per LOB with geographical diversification → Premium, Reserve (section 7); CAT (8.14) → NonLifeUW (section 9).
7. BasicRBC = aggregate([Market, CD, LifeUW, NonLifeUW], M5).
8. Operational risk (section 10), using BasicRBC for the cap.
9. RBC = BasicRBC + Op. Ratio = (Own Funds + Net RA + Net CSM) / RBC.
10. LOB allocation and KPIs (section 11). Run validations (section 15).
