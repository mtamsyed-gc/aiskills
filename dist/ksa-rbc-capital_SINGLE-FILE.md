---
name: ksa-rbc-capital
description: Use for any question on Saudi Arabia (KSA) insurance capital - the Insurance Authority risk-based capital (RBC) framework in template SCA.04 (YE2025 5th dry run, mandatory from 2027) with every risk module, factor, correlation matrix, catastrophe scenario, operational risk, the RBC solvency ratio, template behaviours and validations; the current solvency margin rules to 31 Dec 2026; KSA reinsurance rules (finite ban, retention, rating); and how each reinsurance structure is credited for a Saudi insurer or cooperative.
version: 1.0.0 (13 Nov 2026) - built from the IA Solvency and Capital Template 2026 SCA.04 (issued 25 Feb 2026) as restated in the owner's KSA_RBC_Rules_vSCA04.md, plus the KSA rows of the owner's GCC Solvency Master File (12 Nov 2026). Replaces the condensed KSA content formerly in insurance-capital-ifrs17 file 02
---

# KSA risk-based capital skill

## 1. What this skill is for
You are supporting a life & health reinsurance broker / pricing actuary (FIA) who advises Saudi insurers (all cooperative). Typical questions:
- "What is this Saudi insurer's RBC, which module drives it, and what is its RBC solvency ratio?"
- "What factor, shock or correlation does SCA.04 use for X?"
- "What does a 50% medical QS, a group life QS, a cat XoL or an LPT do to RBC, and to the current solvency margin?"
- "Why does the template show this number?" (blank cells, lookups that return no charge, items left out of a formula)
- "Which reinsurer ratings, retention and cession rules apply to this placement?"
- "Draft the KSA capital section of a board paper or pitch."

## 2. Files and when to load them
Load only what the question needs. Section numbers are those of the owner's specification and are kept in the headings, so a reference such as "section 8.8" or "Matrix 15" means one place only.

| File | Holds | Load when |
|---|---|---|
| `references/20-ksa-rbc-framework.md` | Sections 1, 2, 3, 10, 11, 17 | Every RBC question: scope and conventions, module tree, aggregation rule, top-level formulas, rating buckets, enumerations, lines of business, operational risk, available capital and ratio, LOB allocation, KPIs, calculation order |
| `references/21-ksa-rbc-market-risk.md` | Section 4 | Interest rate (shock table, top-down and bottom-up), equity, property, spread (tables S1, S2), concentration, currency, intangibles, market aggregation |
| `references/22-ksa-rbc-counterparty-default.md` | Section 5 | Reinsurer or bank default (Type 1), receivables (Type 2), catastrophe risk-mitigating effect; the counterparty cost of any treaty |
| `references/23-ksa-rbc-life-underwriting.md` | Section 6 | Long-term protection and savings: mortality, lapse, expense, morbidity |
| `references/24-ksa-rbc-nonlife-health-premium-reserve.md` | Sections 7, 9 | Medical, general and one-year group life / credit life: factors, premium and reserve exposure, geographical diversification, non-life aggregation |
| `references/25-ksa-rbc-catastrophe-scenarios.md` | Section 8 | Pandemic, flood, earthquake, hail, sandstorm, windstorm, property fire, energy, motor, marine, aviation, credit and suretyship |
| `references/26-ksa-rbc-correlations-and-regions.md` | Appendices A, B | Any aggregation: all 17 matrices; KSA regions, earthquake locations, 7 premium regions, 18 outside-KSA catastrophe regions |
| `references/27-ksa-rbc-template-mechanics.md` | Sections 12-16 | Reproducing or reviewing a filled template: legacy solvency sheet, SOFP/SOI, summary of results, validations, governance, the 21 template behaviours |
| `references/28-ksa-rules-outside-template-and-structure-credit.md` | K1-K6 | Current rules to 31 Dec 2026; finite ban, rating, retention, local cession, reporting, breach ladder; capital credit by structure today vs RBC; comparison with Solvency II |
| `references/29-ksa-source-register.md` | Register | Sources, open points, template change history, worked examples (to check a calculation) and load tests |

Routing: this skill covers insurers licensed by the Saudi Insurance Authority. For UAE or Qatar QFC, for IFRS 17 measurement, rating-agency capital, the structures atlas or risk-transfer tests, use `insurance-capital-ifrs17`. For withholding tax, the 30% local first refusal or pricing a layer, use `reinsurance-pricing-knowledge`. Ask the user to load either with its slash command unless it is already loaded.

## 3. How to answer (always)
1. **Treat files 20-27 as the authoritative description of SCA.04.** Do not substitute Solvency II parameters or earlier IA dry-run parameters unless the files say they are identical. If a parameter is not in the files, say it is not defined in the template rather than estimating it.
2. **Tag every value.** **[DRY RUN]** for SCA.04 values (they can change before the final 2027 regulation); **[TEMPLATE]** for how the workbook implements a rule; **[RULE]** for law or regulation (file 28, with the article); **[INTERP]** for interpretation. Never present [INTERP] as [RULE].
3. **Keep three kinds of quantity apart:** prescribed parameters (factors, correlations, thresholds); company inputs (exposures, stressed values from the company's own models, reinsurance recoveries); calculated results.
4. **Say which inputs are needed** where a component is not formula-driven: life underwriting stressed values, top-down interest-rate stressed values, reinsurance recoveries, reinstatement premiums, sliding-scale commission, business interruption and several man-made catastrophe cost items.
5. **Sign convention.** Module sheets and the summary of results show change in NAV (loss negative); the RBC sheet shows charges positive. In these files `Charge_x` = -ΔNAV unless stated.
6. **Use exposures on the right basis:** discounted technical provisions excluding RA and CSM wherever provisions are an exposure; amounts in SAR thousands; valuation date 31 Dec 2025; exposures for scenarios relate to calendar 2026.
7. **Apply the template's actual behaviour** (file 27, section 16) when reproducing template numbers, and tell the user when one of those behaviours affects the answer.
8. **Do not invent what the template does not define:** minimum RBC ratio, intervention ladder, own-funds tiering and minimum capital are not in SCA.04.
9. **Show the arithmetic:** formula, inputs (label assumptions), result, and the matrix used for each aggregation. Check a calculation against the worked examples in file 29 where possible.
10. **For any reinsurance action give both regimes** in 2026 (current rules and RBC, file 28 K5), the counterparty cost (file 22), the legality screen (file 28 K3) and, where relevant, the IFRS 17 effect (`insurance-capital-ifrs17`).
11. **Close with** what drives RBC, the best 1-3 levers and why, what each cannot do, data needed, and items to pre-clear with the IA, compliance or the auditor.

## 4. Guardrails
- Analysis, not legal, regulatory or accounting advice. The IA's final regulation, its guidance and the company's Appointed Actuary decide.
- Keep client data inside LenAI. Anything prepared to leave LenAI must be free of client names, member data and row-level figures unless the user explicitly confirms otherwise.
- Worked examples in file 29 are the specification's test figures, not a company's.
- Do not give Sharia or cooperative-surplus rulings; state the regulatory fact and flag VERIFY.

## 5. Output patterns
- **Quick answer:** 3-6 lines: value, tag, file and section, one caveat.
- **RBC read of an insurer:** position table (RBC by module, diversification, available capital, ratio) → largest drivers → template behaviours that affect the figures → levers ranked → limits → data asks.
- **Structure assessment for a Saudi cedant:** mechanism → legality screen (K3) → current-rules effect → RBC effect by module, with counterparty cost → IFRS 17 pointer → verdict.


<!-- ===== FILE: references/20-ksa-rbc-framework.md ===== -->

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


<!-- ===== FILE: references/21-ksa-rbc-market-risk.md ===== -->

# KSA RBC: Market risk module

Interest rate, equity, property, spread, concentration, currency, intangibles and the market aggregation. Correlation matrices are in file 26.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 4. Market risk module [Market sheet]

General scoping rules:

- **Mutual / investment funds — look-through.** Apply the stress matching the nature of each underlying investment (e.g. equity part under Equity and Concentration; bond part under Interest rate, Spread and Concentration). If actual holdings are unavailable, use the investment mandate (e.g. 40% equity / 60% sukuk). If the mandate is not reliable, treat the whole amount as **Other equity** (highest stress factors) and **exclude it from concentration risk**. The company records per fund: name, basis (actual/mandate), asset class, issuer, value, issuer rating, modified duration (bonds).
- **Held-to-maturity fixed-interest investments** (other than fixed-term deposits) are in scope of interest rate risk exactly like fair-valued fixed-interest assets.
- **Term deposits** are excluded from interest rate risk and included in Counterparty Default Type 1.
- **Participations and subsidiaries** are in scope of both Equity and Concentration; they may be treated as strategic equity if the strategic criteria are met.
  - *Participation* (provisional): ownership, directly or through control, of ≥20% of voting rights or capital; or <20% with demonstrated ability to exert strong influence through joint control with other owners.
  - *Strategic equity participation* (provisional) — all of: (i) value likely to be materially less volatile over the next 12 months than other equities, because of the nature of the investment and the influence exercised; (ii) a clear decisive strategy to keep holding for a long period; (iii) consistency of that strategy with the main policies guiding or limiting the undertaking's actions; (iv) ability to continue holding the participation; (v) existence of a durable link.
- **Property for own use** is in scope of both Property and Concentration.
- **Real estate value** = balance sheet value (expected to be revalued sufficiently frequently).
- **KSA government bonds**: stressed under interest rate risk only; factor 0 under spread and concentration.
- **Public Sector Entity (PSE) with explicit sovereign guarantee and no rating of its own**: uses the factors for the KSA sovereign rating (bucket A).
- **Unit-linked business.**
  - Type A (death/disability benefit = higher of unit fund and sum insured): market-risk exposure = `min(Unit Fund Value, Sum Insured) × (90% × average portfolio mortality rate + 10% × average portfolio morbidity rate)`. Apply look-through to this exposure under each market sub-module (actual holdings, else fund mandate, else equity charge).
  - Type B (benefit = unit value + sum insured): excluded from market risk (fund volatility fully borne by policyholders).
  - All investments relating to unit-linked policies are excluded from concentration risk.

### 4.1 Interest rate risk

Scope: bonds, loans and every asset or liability that is discounted and therefore sensitive to risk-free rates (LIC and LRC if discounted, or only the discounted parts; likewise reinsurance ARC and AIC). The stress applies to the **risk-free** curve only (credit spread is handled in Spread risk).

**Shock table** (relative change applied to the rate; year = cash-flow timing):

| Yr | Up | Down | Yr | Up | Down | Yr | Up | Down |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.70 | 0.75 | 11 | 0.39 | 0.30 | 21 | 0.259143 | 0.288714 |
| 2 | 0.70 | 0.65 | 12 | 0.37 | 0.29 | 22 | 0.258286 | 0.287429 |
| 3 | 0.64 | 0.56 | 13 | 0.35 | 0.28 | 23 | 0.257429 | 0.286143 |
| 4 | 0.59 | 0.50 | 14 | 0.34 | 0.28 | 24 | 0.256571 | 0.284857 |
| 5 | 0.55 | 0.46 | 15 | 0.33 | 0.28 | 25 | 0.255714 | 0.283571 |
| 6 | 0.52 | 0.42 | 16 | 0.31 | 0.28 | 26 | 0.254857 | 0.282286 |
| 7 | 0.49 | 0.39 | 17 | 0.30 | 0.28 | 27 | 0.254000 | 0.281000 |
| 8 | 0.47 | 0.36 | 18 | 0.29 | 0.28 | 28 | 0.253143 | 0.279714 |
| 9 | 0.44 | 0.33 | 19 | 0.27 | 0.29 | 29 | 0.252286 | 0.278429 |
| 10 | 0.42 | 0.31 | 20 | 0.26 | 0.29 | 30 (or more) | 0.251429 | 0.277143 |

For years 21–30: `Up(t) = 0.26 − (t−20)×0.06/70`, `Down(t) = 0.29 − (t−20)×0.09/70`. Years 1–20 equal the Solvency II shocks.

Two approaches are provided; both are evaluated and **added**.

**(a) Top-down approach** (liabilities discounted top-down). Inputs: discount rate and duration for assets and for liabilities; base value considered (assets, liabilities); upward-stressed and downward-stressed values of each (company revalues using the stressed rates).

```
f_up(D), f_down(D): if D > 30 use year-30 factor; if D integer use table; otherwise linear interpolation
                    between floor(D) and ceil(D)
StressedRate_up   = Rate × (1 + f_up(D))        (floor 0%)
StressedRate_down = Rate × (1 − f_down(D))      (floor 0%)
NAV = Assets − Liabilities        (base, up, down)
Loss_up_TD = NAV_base − NAV_up ;  Loss_down_TD = NAV_base − NAV_down
```

**(b) Bottom-up approach** (automated). Inputs per currency block (SAR first, further currencies in following blocks) and per time bucket: annualised risk-free yield `y_t`, discounted asset cash flow `A_t`, discounted liability cash flow `L_t`. Time buckets: months 1–11 (t = 1/12 … 11/12), then years 1–30 (bucket 30 = 30 or greater).

```
k = ceil(t)                                  (months 1–11 use the year-1 shock)
y_up_t   = y_t × (1 + Up(k))      (0 if y_t blank)
y_down_t = y_t × (1 − Down(k))    (0 if y_t blank)
A_up_t   = A_t × (1+y_t)^t / (1+y_up_t)^t        ; same for L_up_t
A_down_t = A_t × (1+y_t)^t / (1+y_down_t)^t      ; same for L_down_t
For the "30 or greater" bucket the four stressed values are company inputs (no formula).
NAV_base = ΣA − ΣL ; NAV_up = ΣA_up − ΣL_up ; NAV_down = ΣA_down − ΣL_down
Loss_up_BU = NAV_base − NAV_up ; Loss_down_BU = NAV_base − NAV_down
```

The company also classifies SOFP assets and liabilities: assets excluded from the module; bonds (incl. bonds in funds); loans; RI ARC (excl. RA) if discounted; RI AIC (excl. RA) if discounted; other; and liabilities excluded; gross LIC (excl. RA) if discounted; gross LRC (excl. RA) if discounted; other. Sense checks: Σ discounted asset cash flows ≥ Σ in-scope classified assets; same for liabilities.

**Charge:**

```
Charge_IR_gross = max(0, max(Loss_up_TD, Loss_down_TD)) + max(0, max(Loss_up_BU, Loss_down_BU))     [O9 = −this]
ΔNAV_IR_net     = min( −Charge_IR_gross + RiskMitigationAllowance , 0 )                              [O12]
Charge_IR       = −ΔNAV_IR_net
```

`RiskMitigationAllowance` is a company input (positive amount) with a stated mitigation type. Charge_IR (after mitigation) feeds the market aggregation.

### 4.2 Equity risk

Stress factors (base + symmetric adjustment; symmetric adjustment updated on 2025 data — KSA from 2023–2025 TASI/Nomu data, outside KSA from EIOPA):

| Category | Base | Symmetric adj. | Applied factor |
|---|---|---|---|
| Within KSA — TASI listed | 36% | −9.00% | **27.00%** |
| Within KSA — Nomu listed | 41% (TASI + 5pp) | −10.55% | **30.45%** |
| Within KSA — Other (incl. unlisted) | 46% (TASI + 10pp) | 0 | **46.00%** |
| Within KSA — Strategic | 19% | 0 | **19.00%** |
| Outside KSA — listed in OECD countries | 39% | +7.90% | **46.90%** |
| Outside KSA — Other (incl. unlisted) | 49% | 0 | **49.00%** |
| Outside KSA — Strategic | 22% | 0 | **22.00%** |

Inputs per equity type i ∈ {TASI, Nomu, Other within KSA, OECD, Other outside KSA}: total equity investments `E_i` (balance sheet value, including equities in funds on look-through and Type A unit-linked equity on look-through) and the strategic part `S_i`.

```
NonStrategic_i = E_i − S_i
Loss_i = S_i × f_strategic(region of i) + NonStrategic_i × f_i
         (strategic factor: 19% for the three KSA types, 22% for the two outside-KSA types)
Charge_Equity = aggregate([Loss_TASI, Loss_Nomu, Loss_OtherKSA, Loss_OECD, Loss_OtherOutside], M6)   [CI31]
Undiversified = Σ Loss_i                                                                              [CH31]
```

### 4.3 Property risk

| Item | Factor |
|---|---|
| Within KSA — Residential | 17.5% |
| Within KSA — Commercial | 20% |
| Within KSA — Agricultural | 15% |
| Outside KSA (all types) | 25% |
| Plant & Equipment | 25% |

```
Loss_res = 17.5% × V_res ; Loss_com = 20% × V_com ; Loss_agr = 15% × V_agr     (balance sheet values)
KSA_div      = aggregate([Loss_res, Loss_com, Loss_agr], M7)
Loss_outside = 25% × V_outside
Loss_PE      = 25% × V_plant&equipment
Charge_Property = sqrt( KSA_div² + Loss_outside² + Loss_PE² )                  [CT29]
Undiversified   = Loss_res + Loss_com + Loss_agr + Loss_outside + Loss_PE
```

(Zero correlation between KSA property, non-KSA property and plant & equipment.)

### 4.4 Spread risk

Scope: fixed-income investments (bonds, sukuk), including bonds in funds and Type A unit-linked bonds on look-through. Inputs per bond: name, issuer type, current exposure (SOFP value), remaining modified duration `D` (years), rating bucket.

```
Duration band k and lower bound LB:  D ≤ 5 → k=1, LB=0 ; 5 < D ≤ 10 → k=2, LB=5 ; 10 < D ≤ 15 → k=3, LB=10 ;
                                     15 < D ≤ 20 → k=4, LB=15 ; D > 20 → k=5, LB=20
StressFactor = a[k, rating] + b[k, rating] × (D − LB)
Loss_bond    = StressFactor × Exposure
Charge_Spread = Σ Loss_bond            (no diversification)                    [AJ129]
```

Table selection by issuer type:
- **KSA Government** → StressFactor = 0.
- **Corporate Inside KSA** → Table S1.
- **PSE (with sovereign guarantee)** → Table S1 with rating forced to **A**.
- **Corporate Outside KSA** → Table S1 × 1.05 (both a and b).
- **Other Governments** → Table S2.

Table S1 — Corporate inside KSA, factor `a`:

| Band | AAA | AA | A | BBB | BB | B and CCC or below | Unrated |
|---|---|---|---|---|---|---|---|
| ≤5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5–10 | 0.045 | 0.055 | 0.070 | 0.125 | 0.225 | 0.375 | 0.175 |
| 10–15 | 0.070 | 0.084 | 0.105 | 0.200 | 0.350 | 0.585 | 0.275 |
| 15–20 | 0.095 | 0.109 | 0.130 | 0.250 | 0.440 | 0.610 | 0.345 |
| >20 | 0.120 | 0.134 | 0.155 | 0.300 | 0.465 | 0.635 | 0.3825 |

Table S1 — Corporate inside KSA, factor `b`:

| Band | AAA | AA | A | BBB | BB | B and CCC or below | Unrated |
|---|---|---|---|---|---|---|---|
| ≤5 | 0.009 | 0.011 | 0.014 | 0.025 | 0.045 | 0.075 | 0.035 |
| 5–10 | 0.005 | 0.006 | 0.007 | 0.015 | 0.025 | 0.042 | 0.020 |
| 10–15 | 0.005 | 0.005 | 0.005 | 0.010 | 0.018 | 0.005 | 0.014 |
| 15–20 | 0.005 | 0.005 | 0.005 | 0.010 | 0.005 | 0.005 | 0.0075 |
| >20 | 0.005 | 0.005 | 0.005 | 0.005 | 0.005 | 0.005 | 0.005 |

Unrated = average of BBB and BB (for both a and b).

Table S2 — Other governments (no Unrated column), factor `a`:

| Band | AAA | AA | A | BBB | BB | B and CCC or below |
|---|---|---|---|---|---|---|
| ≤5 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5–10 | 0 | 0 | 0.055 | 0.070 | 0.125 | 0.225 |
| 10–15 | 0 | 0 | 0.084 | 0.105 | 0.200 | 0.350 |
| 15–20 | 0 | 0 | 0.109 | 0.130 | 0.250 | 0.440 |
| >20 | 0 | 0 | 0.134 | 0.155 | 0.300 | 0.465 |

Table S2 — Other governments, factor `b`:

| Band | AAA | AA | A | BBB | BB | B and CCC or below |
|---|---|---|---|---|---|---|
| ≤5 | 0 | 0 | 0.011 | 0.014 | 0.025 | 0.045 |
| 5–10 | 0 | 0 | 0.006 | 0.007 | 0.015 | 0.025 |
| 10–15 | 0 | 0 | 0.005 | 0.005 | 0.010 | 0.018 |
| 15–20 | 0 | 0 | 0.005 | 0.005 | 0.010 | 0.005 |
| >20 | 0 | 0 | 0.005 | 0.005 | 0.005 | 0.005 |

(Other governments: AAA and AA carry no charge; A to B use the corporate column one notch better.)

Worked values: AAA corporate KSA bond, D = 5 → 4.5%; BBB corporate KSA, D = 5 → 12.5%; AAA corporate KSA, D = 10 → 7.0%.

### 4.5 Concentration risk

Scope: assets covered by equity, interest rate and property risk; excludes assets covered by counterparty default risk; excludes unit-linked investments. Exposure is aggregated **by issuer** (use exposure type "Equities and Bonds" where one issuer has both). Each single property is an exposure.

```
AssetBase = SOFP "Investments (incl. accrued investment income)" + SOFP "Own Property and equipment, net"   (YE2025 totals)
For each exposure i (issuer or property) with value V_i, issuer type, rating:
   share_i   = V_i / AssetBase                      (0 if AssetBase ≤ 0)
   excess_i  = max( share_i − Threshold_i , 0 )
   Loss_i    = AssetBase × excess_i × Factor_i
Charge_Concentration = sqrt( Σ Loss_i² )             (individual concentrations independent)   [DR9]
Undiversified        = Σ Loss_i                                                               [DX229]
```

| | AAA | AA | A | BBB | BB | B | CCC or below (incl. unrated) | Property |
|---|---|---|---|---|---|---|---|---|
| **Threshold** (applied to all non-property issuer types, by rating) | 5% | 5% | 5% | 2.5% | 2.5% | 2.5% | 1% | 10% |
| **Factor** — Corporate Inside KSA | 10% | 10% | 17.5% | 25% | 35% | 50% | 75% | 12% |
| **Factor** — Corporate Outside KSA (×1.05) | 10.5% | 10.5% | 18.375% | 26.25% | 36.75% | 52.5% | 78.75% | — |
| **Factor** — KSA Government | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| **Factor** — Other Governments | 0 | 10% | 10% | 17.5% | 25% | 35% | 50% | — |

- PSE (with sovereign guarantee): rating forced to A → threshold 5%, factor 17.5% (Corporate Inside KSA row).
- Property: threshold 10%, factor 12%.
- KSA Government: factor 0 in every bucket, so no charge.
- Check: Σ exposures listed must equal AssetBase.

### 4.6 Currency risk

| Currency type | Stress |
|---|---|
| USD-pegged currency (GCC) | 2.5% |
| USD-pegged currency (non-GCC) | 5% |
| USD (SAR is pegged) | 0% |
| Other currencies | 25% |

Per foreign currency c (up to 6 rows; listed currencies EUR, GBP, AUD, USD, AED, KWD, QAR, OMR, Other): inputs total assets `A_c` and liabilities `L_c` in that currency at balance sheet date, risk mitigation type and allowance `RM_c`.

```
ΔNAV_gross_c = −| (A_c − L_c) × Stress_c |
ΔNAV_net_c   = min( ΔNAV_gross_c + RM_c , 0 )
Charge_Currency_gross = −Σ ΔNAV_gross_c   [DA9]     Charge_Currency = −Σ ΔNAV_net_c   [DA10]
```

No diversification between currencies. The net-of-mitigation figure feeds the aggregation.

### 4.7 Intangible assets

```
Charge_Intangibles = 80% × recognised intangible assets        [EH16]
```

Added linearly to the market charge after the correlation aggregation (no diversification). Goodwill is dealt with under the Own Funds rules, not here.

### 4.8 Market aggregation

```
Charge_Market = sqrt( vᵀ · M1 · v ) + Charge_Intangibles,
   v = [Charge_IR, Charge_Equity, Charge_Property, Charge_Spread, Charge_Concentration, Charge_Currency]
```


<!-- ===== FILE: references/22-ksa-rbc-counterparty-default.md ===== -->

# KSA RBC: Counterparty default risk module

Type 1 (reinsurers, banks), Type 2 (brokers, agents, TPAs, policyholders), the catastrophe risk-mitigating effect and the aggregation. The reinsurer charge on any treaty starts here.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 5. Counterparty default risk module [Counterparty Default sheet]

Scope: loss from default of counterparties. Receivables from the KSA Government are excluded (unless there are known disputes).

### 5.1 Type 1 — reinsurers, banks and other financial institutions

| Rating | Stress factor | Risk-mitigating-effect multiplier (= 50% × factor) |
|---|---|---|
| AAA | 1.5% | 0.75% |
| AA | 1.5% | 0.75% |
| A | 5% | 2.5% |
| BBB | 5% | 2.5% |
| BB | 50% | 25% |
| B | 50% | 25% |
| Other (incl. unrated) | 50% | 25% |

Inputs per counterparty row (up to 300 rows): type, name, rating; for banks/financial institutions — deposits (incl. term deposits) `Dep`; for reinsurers — discounted ceded technical provisions (claim reserves + UPR, **net of RA**) `CTP`, ceded pipeline claims `Pipe`, reinsurance commission `Comm`, share of risk-mitigating effect in CAT scenarios `RME`; for all — collateral/guarantee `Coll`, payable to the counterparty `Pay`, expected credit loss `ECL`.

```
GrossExposure = (CTP + Pipe + Comm − ECL)   if Reinsurer
              = (Dep − ECL)                 otherwise
NetExposure   = GrossExposure − Pay − Coll                               (reported; not used in the loss)
GrossLoss     = Factor(rating) × GrossExposure + [Reinsurer only] Multiplier(rating) × RME
NetLoss       = max( GrossLoss − Pay − Coll , 0 )
Type1_gross = sqrt( Gᵀ · M17 · G ),  Type1_net = sqrt( Nᵀ · M17 · N )
   M17: 1 on the diagonal, 0.25 between any two different counterparty rows
   ⇒ closed form: sqrt( 0.75 × Σ x_i² + 0.25 × (Σ x_i)² )
Charge_Type1 = Type1_net                                                  [C11]
```

Rules:
- Payables may be entered only if (i) the company has a legal right of offset against the receivables, and (ii) the receivables from the counterparty fall due before the payables.
- Ceded technical provisions are net of RA: on a reinsurer default the company bears ceded claim reserves and unearned ceded premium only, and RA/CSM already receive credit in available capital.
- `RME` per reinsurer = (reinsurer's % share of total assumed recoveries in the CAT scenarios) × (diversified risk-mitigating effect from all CAT scenarios, `TotalRME`).
- `TotalRME` [C8] = sqrt( Σ_s Rec_s² ), where `Rec_s` is the total reinsurance recovery assumed in scenario s, for s ∈ {health pandemic (health + life), flood (KSA + outside), earthquake (KSA + outside), hail (KSA + outside), sandstorm, man-made property (property + health + P&S), energy, motor, marine, aviation, credit & suretyship}.
- Check: Σ RME over reinsurers must be within 1% of TotalRME.

### 5.2 Type 2 — other counterparties

| Counterparty | <90 days past due | 90–180 days | >180 days |
|---|---|---|---|
| Broker | 15% | 45% | 90% |
| Agent | 15% | 45% | 90% |
| TPA | 3.75% | 7.5% | 15% |
| Policyholder | 3.75% | 7.5% | 15% |
| Insurance Company | 3.75% | 7.5% | 15% |
| Others | 3.75% | 7.5% | 15% |

Inputs per counterparty row (up to 300): type, name, receivables **net of ECL** in each ageing bucket `R1, R2, R3`, payables `Pay`.

```
GrossLoss = f1 × R1 + f2 × R2 + f3 × R3
NetLoss   = max( GrossLoss − Pay , 0 )
Charge_Type2_gross = Σ GrossLoss  [D9]        Charge_Type2 = Σ NetLoss  [D11]      (no diversification)
```

Rules:
- Ageing starts immediately from the payment due date, not from the end of any grace period.
- Follow the counterparty classification and balances in the company's SOFP.
- Salvage and subrogation receivables (including IBNR, positive or negative) belong in Type 2, split by counterparty.
- Payables: same two offset conditions as Type 1.

### 5.3 Aggregation

```
Charge_CD = sqrt( T1² + T2² + 2 × 0.75 × T1 × T2 )        (M4)
```


<!-- ===== FILE: references/23-ksa-rbc-life-underwriting.md ===== -->

# KSA RBC: Life underwriting risk module (long-term protection and savings)

Mortality, lapse, expense and morbidity stresses on long-term business. One-year group life and group credit life are NOT here: they are in file 24 (LOB11-13).

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 6. Life underwriting risk module [Life UW sheet]

Scope: long-term Protection & Savings business. Excludes one-year group life and group credit life (LOB11–13, treated in section 7).

Exposure for all four sub-risks: **discounted net mathematical reserves excluding unit reserves, on a best-estimate basis (excluding RA and CSM)**, `BEL`. The same exposure must be used for all four sub-risks and must reconcile with the YE2025 reserving report.

Stressed values `BEL_stress` are company inputs, produced by re-running the valuation with the prescribed shock:

| Sub-risk | Prescribed shock |
|---|---|
| Mortality | +15% on mortality rates (each age, each policy where benefit is contingent on mortality) |
| Lapse — up | +5 percentage points on the annual lapse rate assumed |
| Lapse — down | −5 percentage points on the annual lapse rate assumed (floor 0%) |
| Lapse — mass | One-off discontinuance of 40% of policies |
| Expenses | +1 percentage point on the future annual expense inflation rate |
| Morbidity/Disability | +20% on disability and morbidity rates |

```
ΔNAV_mortality = min( BEL − BEL_mortality , 0 )
ΔNAV_expense   = min( BEL − BEL_expense   , 0 )
ΔNAV_morbidity = min( BEL − BEL_morbidity , 0 )
ΔNAV_lapse     = min( min( BEL − BEL_lapse_up , BEL − BEL_lapse_down , BEL − BEL_mass ) , 0 )
Charge_x       = −ΔNAV_x
Charge_LifeUW  = aggregate([Mortality, Lapse, Expenses, Morbidity], M2)
```

Lapse rules: the lapse stresses apply only to policies where discontinuance would increase technical provisions (without risk adjustment); policies for which the change in NAV under a scenario is positive are excluded from that scenario's calculation. The company also records the base lapse rate.

There is no risk mitigation column in this module (before = after).


<!-- ===== FILE: references/24-ksa-rbc-nonlife-health-premium-reserve.md ===== -->

# KSA RBC: Non-life, health and short-term group life: premium and reserve risk

Factors by line, premium and reserve exposure, geographical diversification, reinstatement and sliding-scale effects, and the non-life aggregation. Medical (LOB9) and one-year group life / credit life (LOB11-13) are here.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 7. Non-life, health and short-term P&S underwriting — premium and reserve risk [Non-Life & Short Term P&S UW sheet]

### 7.1 Stress factors

| LOB | Premium — direct & proportional inwards | Premium — non-proportional inwards | Reserve — direct & proportional inwards | Reserve — non-proportional inwards |
|---|---|---|---|---|
| LOB1 Accident & Liability | 31% | 51% | 26% | 60% |
| LOB2 Motor Compulsory | 31% | 51% | 23% | 60% |
| LOB3 Motor Compulsory + Others | 18% | 51% | 19% | 60% |
| LOB4 Property | 29.5% | 51% | 22.5% | 60% |
| LOB5 Marine | 45% | 51% | 24% | 60% |
| LOB6 Aviation | 45% | 51% | 24% | 60% |
| LOB7 Energy | 29.5% | 51% | 22.5% | 60% |
| LOB8 Engineering | 27% | 51% | 20% | 60% |
| LOB9 Health Insurance | 13% | 51% | 15% | 60% |
| LOB10 Other General and Health | 29% | 51% | 23.5% | 60% |
| LOB11 Group Life | 43% | 51% | 24% | 60% |
| LOB12 Group Credit Life | 43% | 51% | 24% | 60% |
| LOB13 Group – Other | 43% | 51% | 24% | 60% |

Premium risk = increase in the **net** loss ratio. Reserve risk = inadequacy of discounted **net** claim reserves and ULAE.

### 7.2 Premium risk

Inputs per LOB (all net of reinsurance): `NEP_prev` net earned premium in the past calendar year; `NEP_next` expected net earned premium in the current/next calendar year; `LC` loss component net of loss recovery component at the valuation date; `FP_exist` future net premium on long-term contracts written in the last calendar year or earlier, to be earned after the current calendar year (discounted if GMM); `FP_future` the same for contracts written/to be written in the current calendar year; `NP_exp` exposure value for non-proportional inwards reinsurance; `Reinst` impact of reinstatement premium; `Slide` impact of sliding-scale commission; and the premium exposure split over 7 regions (KSA; Asia excluding KSA; Europe; Africa; South America; North America; Australia) — by **location of risk**, not of policyholder.

```
Exposure_DP  = max( NEP_prev , NEP_next + LC ) + FP_exist + FP_future
Loss_DP      = Exposure_DP × f_prem_DP(LOB)
Loss_NP      = NP_exp × f_prem_NP(LOB)                 (51%)
TotalLoss    = Loss_DP + Loss_NP
TotalLoss_RI = TotalLoss + Reinst + Slide
GeoDiv(LOB)  = 0.75 + 0.25 × Σ_r P_r² / (Σ_r P_r)²      (= 1 if Σ_r P_r = 0)        P_r = premium exposure in region r
Loss_LOB_gross = TotalLoss × GeoDiv                     ("before risk mitigation")
Loss_LOB       = TotalLoss_RI × GeoDiv                  ("after": includes reinstatement premium and sliding commission)
Charge_Premium = aggregate( Loss_LOB[1..13], M15 )
Undiversified  = Σ Loss_LOB
```

GeoDiv ranges from 1.0 (single region) down to a floor of 0.75 + 0.25/7 ≈ 0.786 (equal spread over 7 regions): at most 25% weight is given to geographical diversification.

### 7.3 Reserve risk

Inputs per LOB: best estimate of OCR + IBNR + ULAE, **net of reinsurance and discounted**, at last year end, split into direct & proportional inwards `Res_DP` and non-proportional inwards `Res_NP`; reserve exposure by the same 7 regions.

```
Loss_res      = Res_DP × f_res_DP(LOB) + Res_NP × f_res_NP(LOB)       (NP = 60%)
GeoDiv_res    = 0.75 + 0.25 × Σ_r R_r² / (Σ_r R_r)²                    (= 1 if total is 0)
Loss_res_LOB  = Loss_res × GeoDiv_res
Charge_Reserve = aggregate( Loss_res_LOB[1..13], M16 )
```

No risk mitigation adjustment (before = after).

---

## 9. Non-life UW aggregation

```
Charge_NonLifeUW = aggregate([Premium, Reserve, CAT], M3)
   M3: Premium–Reserve 0.75 ; Premium–CAT 0.25 ; Reserve–CAT 0.25
```


<!-- ===== FILE: references/25-ksa-rbc-catastrophe-scenarios.md ===== -->

# KSA RBC: Catastrophe scenarios

Health pandemic, natural catastrophe (flood, earthquake, hail, sandstorm, windstorm) and man-made catastrophe (property fire, energy, motor, marine, aviation, credit and suretyship). Note for life and health books: the property-fire scenario and the sandstorm scenario both carry health and life losses, not only pandemic.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 8. Catastrophe scenarios [Scenarios sheet]

General rules:
- A scenario may hit several lines; the company reflects every relevant impact (e.g. a life-only insurer exposed to the man-made property fire scenario considers deaths at its largest concentration of insured lives under a group policy).
- Exposure measure is **sum insured** (not PML), "unless a lower sub-limit applies for this CAT event".
- Reinsurance recoveries, reinstatement premiums and sliding-scale commission refundable are company inputs based on existing reinsurance.
- Generic net-of-reinsurance relation for every scenario/segment:
  `NetLoss = GrossLoss − ReinsuranceRecovery + ReinstatementPremium + SlidingScaleCommissionRefundable [− Salvage, motor only]`.
- The values carried to the RBC are the **after reinsurance, after geographical diversification** figures.
- The company documents the assumptions used for each scenario.

### 8.1 Health pandemic

Health portfolio (exposure: number of insured lives `N_h`; exclude Visitor Visa, Tourism Visa and Umrah products because pandemic is an exclusion there):

| Parameter | Value |
|---|---|
| Insureds infected | 2% |
| Rejection ratio (fall under Unified Health Insurance Policy exclusions) | 95% |
| Of infected: require hospitalisation | 10% |
| Of infected: require physician consultation | 90% |
| Cost of hospital treatment per patient | SAR 15,000 (15 in SR '000) |
| Cost of testing and physician consultation per patient | SAR 550 (0.55 in SR '000) |

```
GrossLoss_health = N_h × 2% × (1 − 95%) × (10% × 15 + 90% × 0.55)      [SR '000]  = N_h × 0.001995
NetLoss_health   = GrossLoss_health − Recovery + ReinstatementPremium + SlidingScaleCommission
```

Short-term group life (exposure: number of life-years `N_l`, average sum at risk `SAR_avg`; only where policy terms do not exclude pandemic death):

```
GrossLoss_life = N_l × SAR_avg × 0.06%
NetLoss_life   = GrossLoss_life − Recovery
Charge_Pandemic = NetLoss_health + NetLoss_life            (simple sum)
```

### 8.2 Natural CAT — common mechanics

Within KSA: `Loss = RegionWeight × BaseFactor × SumInsured` per LOB and region; regional losses (summed over LOBs) are aggregated with the peril's regional correlation matrix.

Outside KSA: `Loss_region = PremiumFactor × EarnedPremium_region` where EarnedPremium is the **premium earned during 2025** (past 12 months) for risks in that region; 18 regions (Appendix B); regional multiplier = 1 for every region. Diversification:

```
Outside_div = (Σ_r L_r) × ( 0.5 + 0.5 × Σ_r L_r² / (Σ_r L_r)² )          (0 if Σ = 0)
Peril_total = sqrt( KSA_div² + Outside_div² )
```

The calculation is run twice: on gross losses (before reinsurance) and on net losses (after reinsurance). The undiversified figure is the plain sum of regional losses.

### 8.3 Pluvial flood

Base factor within KSA 0.10% of sum insured; outside KSA 110% of earned premium.

| KSA region | Western | Central | Eastern | Northern | Southern |
|---|---|---|---|---|---|
| Risk weight | 4 | 2 | 1 | 1 | 4 |
| Effective % of sum insured | 0.40% | 0.20% | 0.10% | 0.10% | 0.40% |

LOBs within KSA and exposure:
- Property: sum insured **on the ground floor** × (1 + 10% business interruption uplift). Sum insured on higher floors is collected but carries zero weight.
- Onshore marine: sum insured.
- Energy: sum insured × (1 + 10% business interruption uplift).
- Engineering: sum insured.
- Motor: sums insured under Motor Comprehensive policies; net loss also deducts salvage.

Outside KSA segments: property, onshore marine, energy, engineering, motor vehicle — each 110% × earned premium by region.
Regional correlation within KSA: Matrix 11.

### 8.4 Earthquake

Scenario: Red Sea fault line, north-western KSA. Base factor within KSA 0.10% of sum insured; outside KSA 120% of earned premium.

| Location | Haql | Qiyal | Neom | Tabuk |
|---|---|---|---|---|
| Risk weight | 8 | 5 | 3 | 3 |
| Effective % of sum insured | 0.80% | 0.50% | 0.30% | 0.30% |

LOBs: property, energy, engineering (within KSA: sum insured by location, no BI uplift; outside KSA: earned premium by region). Onshore marine is not included. Location correlation: Matrix 12 (all 1 → simple sum across the four locations).

### 8.5 Hail

Base factor within KSA 0.05% of sum insured (0.01% × 5 multiplier for motor comprehensive); outside KSA 30% of earned premium.

| KSA region | Western | Central | Eastern | Northern | Southern |
|---|---|---|---|---|---|
| Risk weight | 2 | 1 | 1 | 3 | 3 |
| Effective % of sum insured | 0.10% | 0.05% | 0.05% | 0.15% | 0.15% |

LOB: motor only (sums insured under Motor Comprehensive within KSA; motor earned premium by region outside KSA). Net loss deducts salvage. Regional correlation: Matrix 13.

### 8.6 Sandstorm (KSA only)

| KSA region | Western | Central | Eastern | Northern | Southern |
|---|---|---|---|---|---|
| Risk weight | 1 | 3 | 3 | 5 | 5 |

- Property (power plants): `Loss = 0.03% × RegionWeight × SumInsured_powerplants × (1 + 10% BI uplift)`.
- Health: `Insureds needing emergency treatment = Insureds × 0.5% × RegionWeight` (0.5% = 10% × 5%); `Loss = that number × SAR 500` (0.5 in SR '000).
- Regional loss = property + health; aggregate regions with Matrix 14. No outside-KSA component.

### 8.7 Windstorm (outside KSA only)

`Loss_region = 175% × earned premium` for property, energy and engineering by region; diversification by the outside-KSA formula in 8.2. No KSA component.

### 8.8 Man-made CAT — Property (fire)

Scenario: fire at the single largest property risk covered under a reinsurance treaty (excluding facultative risks); health and life covers of people in the same property are also hit.

```
Property loss  = 100% of sum insured (or lower applicable sub-limit)
               + business interruption loss (company input: claim for 50% of the maximum number of days in the policy)
Health loss    = insured lives × 25% (injuries needing hospital treatment) × average cost per claim (input)
P&S loss       = insured lives × 5% (deaths) × average cost per claim (input)
Gross          = Property + BI + Health + P&S
Net            = Gross − Σ recoveries (property, health, P&S) + reinstatement premiums + sliding scale commission (property, health)
```

### 8.9 Man-made CAT — Energy

Scenario: explosion and fire at oil refineries in the company's largest concentration of gross energy exposures (e.g. Ras Tanura), treaty business excluding facultative; onshore and offshore both considered when identifying the concentration.

```
Gross = Total sum insured (or lower sub-limit)
      + business interruption claim (input: 50% of the maximum number of days in the policy)
      + cost of environmental clean-up (input: 50% of the benefit limit unless excluded)
Net   = Gross − recovery + reinstatement premium + sliding scale commission
```

### 8.10 Man-made CAT — Motor liability & event cancellation

Scenario: collision between an insured car and a coach carrying European football league players; 5 passengers permanently disabled; match cancelled. Applicability flag (Yes/No) is a company input — the loss is zero when "No".

```
Liability for disability = 5 injured × SAR 2,000,000 average claim = 10,000 (SR '000)
Gross = Liability for disability + liability claim for event cancellation (input, if written)
Net   = Gross − recovery + reinstatement premium + sliding scale commission
```

### 8.11 Man-made CAT — Marine

Scenario: insured oil tanker collides with a cruise ship; all cruise passengers are US citizens (US litigation); hull, liability, wreck removal and pollution.

```
Death claims   = 50 deaths × SAR 300,000 = 15,000 (SR '000)
Injury claims  = 500 injured × SAR 500,000 = 250,000 (SR '000)
Gross = max marine hull exposure to a single tanker (input)
      + max marine cargo exposure to a tanker (input)
      + death claims + injury claims
      + wreck removal (input: 50% of benefit limit unless excluded)
      + oil pollution clean-up (input: 50% of benefit limit unless excluded)
      + US litigation cost (input: 10% of total injury claims cost, subject to policy cap)
Gross is set to 0 if hull + cargo exposure = 0.
Net   = Gross − recovery + reinstatement premium + sliding scale commission
```

### 8.12 Man-made CAT — Aviation

Scenario: two fully occupied passenger aircraft of two domestic airlines (Saudi Airlines and Fly Nas) collide over Riyadh airport; airport closed for days; the pilot of the aircraft insured by the company is held responsible.

```
Compensation to heirs = (350 + 150 deaths) × SAR 300,000 = 150,000 (SR '000)
Gross = hull loss airline 1 (input) + hull loss airline 2 (input) + compensation to heirs
      + business interruption at Riyadh airport (input: 5% of the BI benefit limit unless excluded)
Gross is set to 0 if both hull losses are 0.
Net   = Gross − recovery + reinstatement premium + sliding scale commission
```

### 8.13 Man-made CAT — Credit & suretyship

```
Default loss (gross) = 10% × exposure under the two largest trade credit & surety policies
Default loss (net)   = gross − recovery + reinstatement premium + sliding scale commission
Recession loss       = 100% × premium expected to be earned on trade credit & surety policies in the next 12 months
Gross = sqrt( DefaultGross² + Recession² )
Net   = sqrt( DefaultNet² + Recession² )
Undiversified (net) = DefaultNet + Recession
```

### 8.14 CAT aggregation

```
ManMadeCAT = sqrt( Energy² + Property² + Motor² + Marine² + Aviation² + Credit² )      (M8 = identity)
NatCAT     = sqrt( Flood² + Earthquake² + Hail² + Sandstorm² + Windstorm² )            (M9 = identity)
CAT        = sqrt( ManMadeCAT² + Pandemic² + NatCAT² )                                 (M10 = identity)
```


<!-- ===== FILE: references/26-ksa-rbc-correlations-and-regions.md ===== -->

# KSA RBC: Correlation matrices and regions

All 17 correlation matrices, the KSA regions and earthquake locations, the 7 premium/reserve regions and the 18 natural-catastrophe regions outside KSA.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## Appendix A — Correlation matrices

**Matrix 1 — Market**

| | IR | Equity | Property | Spread | Concentration | Currency |
|---|---|---|---|---|---|---|
| IR | 1 | 0.5 | 0.5 | 0.5 | 0 | 0.25 |
| Equity | 0.5 | 1 | 0.75 | 0.75 | 0 | 0.25 |
| Property | 0.5 | 0.75 | 1 | 0.5 | 0 | 0.25 |
| Spread | 0.5 | 0.75 | 0.5 | 1 | 0 | 0.25 |
| Concentration | 0 | 0 | 0 | 0 | 1 | 0 |
| Currency | 0.25 | 0.25 | 0.25 | 0.25 | 0 | 1 |

**Matrix 2 — Life UW**

| | Mortality | Lapse | Expenses | Morbidity |
|---|---|---|---|---|
| Mortality | 1 | 0 | 0.25 | 0.25 |
| Lapse | 0 | 1 | 0.5 | 0 |
| Expenses | 0.25 | 0.5 | 1 | 0.5 |
| Morbidity | 0.25 | 0 | 0.5 | 1 |

**Matrix 3 — Non-Life UW**

| | Premium | Reserve | CAT |
|---|---|---|---|
| Premium | 1 | 0.75 | 0.25 |
| Reserve | 0.75 | 1 | 0.25 |
| CAT | 0.25 | 0.25 | 1 |

**Matrix 4 — Counterparty default:** Type 1 – Type 2 = 0.75.

**Matrix 5 — Basic RBC**

| | Market | CD | Life UW | Non-Life UW |
|---|---|---|---|---|
| Market | 1 | 0.25 | 0.25 | 0.25 |
| CD | 0.25 | 1 | 0.25 | 0.5 |
| Life UW | 0.25 | 0.25 | 1 | 0 |
| Non-Life UW | 0.25 | 0.5 | 0 | 1 |

**Matrix 6 — Equity**

| | TASI | Nomu | Unlisted/other KSA | Listed OECD | Other outside KSA |
|---|---|---|---|---|---|
| TASI | 1 | 0.75 | 0.5 | 0.5 | 0.25 |
| Nomu | 0.75 | 1 | 0.5 | 0.5 | 0.25 |
| Unlisted/other KSA | 0.5 | 0.5 | 1 | 0.25 | 0.25 |
| Listed OECD | 0.5 | 0.5 | 0.25 | 1 | 0.5 |
| Other outside KSA | 0.25 | 0.25 | 0.25 | 0.5 | 1 |

**Matrix 7 — Property (KSA):** Residential–Commercial 0.75; Residential–Agricultural 0.25; Commercial–Agricultural 0.25.

**Matrix 8 — Man-made CAT (6×6), Matrix 9 — Natural CAT (5×5), Matrix 10 — CAT (3×3):** identity (all off-diagonals 0).

**Matrix 11 — Pluvial flood regions, and Matrix 13 — Hail regions (identical)**

| | W | C | E | N | S |
|---|---|---|---|---|---|
| W | 1 | 0.5 | 0 | 0.5 | 0.75 |
| C | 0.5 | 1 | 0.5 | 0.25 | 0 |
| E | 0 | 0.5 | 1 | 0.25 | 0 |
| N | 0.5 | 0.25 | 0.25 | 1 | 0 |
| S | 0.75 | 0 | 0 | 0 | 1 |

**Matrix 12 — Earthquake locations (Haql, Qiyal, Neom, Tabuk):** all entries 1.

**Matrix 14 — Sandstorm regions**

| | W | C | E | N | S |
|---|---|---|---|---|---|
| W | 1 | 0.25 | 0 | 0.5 | 0.25 |
| C | 0.25 | 1 | 0.75 | 0.5 | 0.25 |
| E | 0 | 0.75 | 1 | 0.25 | 0 |
| N | 0.5 | 0.5 | 0.25 | 1 | 0 |
| S | 0.25 | 0.25 | 0 | 0 | 1 |

**Matrix 15 — Premium risk by LOB.** Default 0.25 for every pair, except:

| Pair | Correlation |
|---|---|
| LOB2–LOB3 (Motor Compulsory – Motor Compulsory + Others) | 0.75 |
| LOB1–LOB9 (Accident & Liability – Health) | 0.5 |
| LOB2–LOB9, LOB3–LOB9 (Motor – Health) | 0.5 |
| LOB4–LOB8 (Property – Engineering) | 0.5 |
| LOB5–LOB7 (Marine – Energy) | 0.5 |
| LOB11–LOB12 (Group Life – Group Credit Life) | 0.75 |
| LOB11–LOB13, LOB12–LOB13 | 0.5 |

**Matrix 16 — Reserve risk by LOB.** Identical to Matrix 15 **except LOB1–LOB9 = 0.25** (not 0.5).

**Matrix 17 — Type 1 counterparties (300×300):** 1 on the diagonal, 0.25 everywhere else.

---

## Appendix B — Regions

**KSA regions (flood, hail, sandstorm):** Western, Central, Eastern, Northern, Southern. **Earthquake locations:** Haql, Qiyal, Neom, Tabuk.

**Premium/reserve risk regions (7):** KSA; Asia excluding KSA; Europe; Africa; South America; North America; Australia.

**Natural CAT regions outside KSA (18):**

1. Northern Europe — Denmark (except Greenland), Estonia, Finland, Guernsey, Iceland, Ireland, Isle of Man, Jersey, Latvia, Lithuania, Norway, Sweden, United Kingdom (except overseas territories).
2. Western Europe — Austria, Belgium, France (except overseas territories), Germany, Liechtenstein, Luxembourg, Monaco, Netherlands (except Caribbean territories), Switzerland.
3. Eastern Europe — Belarus, Bulgaria, Czech Republic, Hungary, Moldova, Poland, Romania, Russia, Slovakia, Ukraine.
4. Southern Europe — Albania, Andorra, Bosnia and Herzegovina, Croatia, Cyprus, North Macedonia, Gibraltar, Greece, Italy, Malta, Montenegro, Portugal, San Marino, Serbia, Slovenia, Spain, Vatican City.
5. Central and Western Asia (excluding KSA) — Armenia, Azerbaijan, Bahrain, Georgia, Iraq, Israel, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Lebanon, Oman, Qatar, Syria, Tajikistan, Turkey, Turkmenistan, United Arab Emirates, Uzbekistan, Yemen.
6. Eastern Asia — China, Japan, Mongolia, North Korea, South Korea, Taiwan.
7. South and South-Eastern Asia — Afghanistan, Bangladesh, Bhutan, Brunei, Myanmar, Cambodia, India, Indonesia, Iran, Laos, Malaysia, Maldives, Nepal, Pakistan, Philippines, Singapore, Sri Lanka, Thailand, East Timor, Vietnam.
8. Oceania — American Samoa, Australia, Cook Islands, Fiji, French Polynesia, Guam, Kiribati, Marshall Islands, Micronesia, Nauru, New Caledonia, New Zealand, Niue, Northern Mariana Islands, Palau, Papua New Guinea, Pitcairn Islands, Samoa, Solomon Islands, Tonga, Tuvalu, Vanuatu, Wallis and Futuna.
9. Northern Africa — Algeria, Benin, Burkina Faso, Cameroon, Cape Verde, Central African Republic, Chad, Côte d'Ivoire, Egypt, Gambia, Ghana, Guinea, Guinea-Bissau, Liberia, Libya, Mali, Mauritania, Morocco, Niger, Nigeria, Saint Helena, Senegal, Sierra Leone, South Sudan, Sudan, Togo, Tunisia.
10. Southern Africa — Angola, Botswana, Burundi, Comoros, DR Congo, Djibouti, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Kenya, Lesotho, Madagascar, Malawi, Mauritius, Mayotte, Mozambique, Namibia, Congo, Réunion, Rwanda, São Tomé and Príncipe, Seychelles, Somalia, South Africa, Swaziland, Uganda, Tanzania, Zambia, Zimbabwe.
11. Northern America (excluding USA) — Bermuda, Canada, Greenland, Saint Pierre and Miquelon.
12. Caribbean and Central America — Anguilla, Antigua & Barbuda, Aruba, Bahamas, Barbados, Belize, Bonaire, British Virgin Islands, Cayman Islands, Costa Rica, Cuba, Curaçao, Dominica, Dominican Republic, El Salvador, Grenada, Guadeloupe, Guatemala, Haiti, Honduras, Jamaica, Martinique, Mexico, Montserrat, Nicaragua, Panama, Puerto Rico, Saint Barthélemy, Saba, Saint Kitts and Nevis, Saint Lucia, Saint Martin, Saint Vincent and the Grenadines, Sint Eustatius, Sint Maarten, Trinidad and Tobago, Turks and Caicos Islands, US Virgin Islands.
13. Eastern South America — Brazil, Falkland Islands, French Guiana, Guyana, Paraguay, Suriname, Uruguay.
14. Northern, Southern and Western South America — Argentina, Bolivia, Chile, Colombia, Ecuador, Peru, Venezuela.
15. North-east USA — Connecticut, Delaware, District of Columbia, Maine, Maryland, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont.
16. South-east USA — Alabama, Arkansas, Florida, Georgia, Kentucky, Louisiana, Mississippi, North Carolina, Puerto Rico, South Carolina, Tennessee, Virginia, West Virginia.
17. Mid-west USA — Illinois, Indiana, Iowa, Kansas, Michigan, Minnesota, Missouri, Nebraska, North Dakota, Ohio, Oklahoma, South Dakota, Wisconsin.
18. Western USA — Alaska, Arizona, California, Colorado, Hawaii, Idaho, Montana, Nevada, New Mexico, Oregon, Texas, Utah, Washington, Wyoming.

(Puerto Rico appears in both region 12 and region 16 in the template.)


<!-- ===== FILE: references/27-ksa-rbc-template-mechanics.md ===== -->

# KSA RBC: Template mechanics: legacy solvency sheet, financial statements, summary of results, validations, governance and template behaviours

Load when reproducing or reviewing a company's filled template, reconciling a number, or explaining why the template shows a result that differs from the rule as written.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 12. Regulatory Solvency sheet (current/legacy solvency margin basis)

Reported for 2024 and 2025 actual and 2026 projected. This is separate from the RBC and is not an input to it. All line items are inputs; the sheet only adds them up.

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

## 13. Financial statements captured [SOFP, SOI]

SOFP is entered for three segments — General & Health; P&S non-linked; P&S linked — each split into Insurance Operations and Shareholders' Operations for actual years 2023–2025, and totals for projections 2026–2029; "Total Insurance" = sum of the three segments.

Assets: insurance contract assets; reinsurance contract assets; financial assets for unit-linked contracts; cash and cash equivalents; term deposits; statutory deposit; accrued income on statutory deposit; investments (incl. accrued investment income); own property and equipment, net; prepaid expenses and other assets; deferred tax asset; intangible assets; goodwill.

Liabilities: insurance contract liabilities; reinsurance contract liabilities; investment contract liabilities; accrued income payable to IA; accrued expenses and other liabilities; current liabilities (incl. short-term borrowings); EOSB provision; provision for zakat and income tax; dividends payable; deferred tax liability.

Equity: share capital; statutory reserve; fair value reserve for investments; retained earnings; re-measurement of EOSB obligations; share premium; insurance finance reserves; other reserves.

SOFP items used by the RBC calculation (YE2025 total insurance): total assets and total liabilities (interest rate base values and reconciliation), investments and own property & equipment (concentration asset base and market KPI).

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

These are how the SCA.04 workbook actually behaves. Reproduce them when replicating template output and tell the user when one affects a result.

1. **Operational risk is zero until the cybersecurity score is entered.** With the score blank, the loading cell shows a text prompt and the final operational ΔNAV evaluates to 0.
2. **Spread — "Other Governments" with rating "Unrated"** returns blank (no charge): Table S2 has no Unrated column.
3. **Spread — PSE (with sovereign guarantee)** always uses rating A, whatever rating is entered.
4. **Spread — blank or invalid inputs** (missing duration, rating or issuer type) produce a blank stress factor and zero loss, with no error shown.
5. **Concentration thresholds** are looked up by rating from the Corporate Inside KSA row for every non-property issuer type. The 100% threshold shown for KSA Government is not used; KSA Government has no charge because its factor is 0.
6. **Concentration — missing rating** on a non-property exposure gives zero excess (no charge).
7. **Windstorm reinsurance recoveries are not included in TotalRME** (the counterparty default risk-mitigating effect), although every other CAT scenario is.
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


<!-- ===== FILE: references/28-ksa-rules-outside-template-and-structure-credit.md ===== -->

# KSA: current solvency rules, reinsurance rules, capital credit by structure, and comparison with Solvency II

Load for anything about a Saudi insurer that is NOT a calculation inside the SCA.04 template: the solvency margin rules in force until 31 Dec 2026, the reinsurance and legal rules that screen a structure, how each reinsurance structure is credited under today's rules and under RBC, breach and reporting rules, and how the framework compares with Solvency II.

Sources and tags:
- Sections K1-K5 come from the owner's working file "GCC Solvency Master File: KSA, Qatar (QFC) and UAE" (12 Nov 2026), not from the SCA.04 template. Tags: **[RULE]** law or regulation (Implementing Regulations of the Cooperative Insurance Companies Control Law, 2010 Reinsurance Regulation, IA circulars); **[INTERP]** interpretation or market practice; **VERIFY** = check the primary text before a client relies on it.
- Section K6 is Appendix C of the SCA.04 specification **[TEMPLATE] [DRY RUN]**.
- Withholding tax on premium to non-resident reinsurers and the 30% local first refusal are in the companion skill `reinsurance-pricing-knowledge` (file 03); only the one-line rule is repeated here.
- Analysis, not legal advice.

## K1. The two regimes and the switch-over
| | Current rules ("KSA-now") | Risk-based capital ("KSA-RBC") |
|---|---|---|
| Instrument | Implementing Regulations Arts 63-68 **[RULE]**; in force to 31 Dec 2026 | IA Solvency and Capital Template SCA.04 (files 20-27); mandatory from 1 Jan 2027 (VERIFY the final regulation) |
| Type | Solvency I volume margin | Modular, 17 correlation matrices, stresses and scenarios, 99.5% one-year |
| Floor | Minimum capital SAR 100m / SAR 200m (VERIFY which applies to which licence); SAR 300m in practice | Planned; amount not published |
| Test | Required margin = max(minimum capital, premium-method or claims-method margin) | RBC solvency ratio = (Own Funds + net RA + net CSM) / RBC; no minimum ratio or ladder in SCA.04 |
| Liability basis | Statutory forms | IFRS 17, with RA and CSM taken out of exposures and added to available capital |
| Reinsurance credit | Net, floored at 50% of gross | Net, no floor; offset by the counterparty charge (file 22) |
| Capital resources | Net admissible assets by fund (policyholders G&H, policyholders P&S, shareholders); Table 2 admission limits | Own Funds from the separate IA Own Funds assessment and reporting template (which carries the tiering) + net RA + net CSM; admissibility has no effect on RBC |

The template's "Regulatory Solvency" sheet reports the current-rules position alongside RBC for 2024-2026 (file 27, section 12): it only adds up inputs and does not hold the premium or claims method formulas.

On 1 Jan 2027, retire section K2 and replace every [DRY RUN] value with the final regulation.

## K2. Current rules (to 31 Dec 2026) [RULE]
- **General and health:** required margin = higher of the premium method (factor x net written premium) and the claims method (factor x three-year average net incurred claims). Only the premium method applies in the first 3 years of operation.
- Factors, premium / claims: health 16 / 24; motor 20 / 25; fire (property) 16 / 20; liability 30 / 35; engineering, marine, aviation, energy (EMAE) 30 / 30; other 16 / 30; inward reinsurance 30 / 30. Personal accident is in "other" (16 / 30).
- Claims method binds above a net loss ratio of about: health 67% (16 / 24), motor 80%, fire 80%, liability 86%, other 53% **[INTERP]**.
- Reinsurance credit on net written premium is floored at 50% of gross.
- **Protection and savings (Art 67):**
  - short-term group life: 4% of technical provisions + 0.1% of group capital at risk; credit for reinsurance capped at 50% of capital at risk;
  - long-term individual: 4% of provisions + 0.3% of individual capital at risk; credit capped at 50%.
  - Art 20: the investment element of savings contracts cannot be reinsured.
- No catastrophe charge and no counterparty charge.
- **Breach ladder** (ratio of available to required margin): 75-100% restore by the next quarter; 50-75% corrective plan; 25-50% regulator measures; below 25% appointment of an adviser or cessation. Companies Law triggers apply separately at accumulated losses of 50% of capital.

## K3. Reinsurance and legal rules that screen a structure [RULE unless tagged]
- **Rating:** reinsurers rated at least BBB (S&P or equivalent) or AM Best B+; lower needs IA approval. AM Best B+ = bbb- on AM Best's own issuer scale, so the AM Best route accepts a lower security than a BBB from S&P (see `insurance-capital-ifrs17` file 03).
- **Finite reinsurance prohibited:** 2010 Reinsurance Regulation Art 19. Whether it carries into the 2027 regulations is not confirmed (VERIFY). Screen every loss-sensitive design with the risk-transfer tests in `insurance-capital-ifrs17` files 01 and 06.
- **Retention:** at least 30% of total premium retained (Art 40), so cession cannot exceed 70%.
- **Local cession:** 30% first refusal to Saudi-licensed reinsurers from 1 Jan 2025; 5% withholding tax on premium paid to non-resident reinsurers. Mechanics: `reinsurance-pricing-knowledge`, file 03.
- **Registration:** foreign reinsurers registered on the IA platform.
- **Gearing:** IA approval needed if gross written premium exceeds 10x capital and reserves (Art 48).
- **Reporting of terms (Art 18):** profit and loss sharing, loss-ratio caps, swing rates and reinstatements are reported; annual reinsurance strategy filed by 30 April.
- **Reporting cycle:** monthly returns within 15 working days; the RBC template carries 4-year projections (business plan, plus alternative projections where the Appointed Actuary's assumptions differ materially).
- **Cooperative model:** all Saudi insurers are cooperative; the surplus split to policyholders is in Implementing Regulations Art 70 (VERIFY the current split).
- **Subordinated debt:** expected to be eligible as own funds under RBC (IA statement, Apr 2026; VERIFY in the Own Funds template).

## K4. What binds and sector context [INTERP]
- Under the current rules a medical writer is bound by the claims method once its net loss ratio exceeds about 67%; reinsurance credit stops at 50% ceded.
- Under RBC, sector RBC is about 30-41% of NEP with premium risk the largest module; the YE2024 dry-run ratio was 182% under RBC against 206% under the current rules (owner's master file, from IA dry-run feedback; VERIFY the latest IA publication).
- For a property or energy writer, catastrophe (man-made property fire, energy) can dominate RBC, because the scenarios take 100% of the largest treaty risk's sum insured: in the specification's stylised worked example CAT is 347k of a 355k non-life charge (file 29).
- For a life and health book, the catastrophe charge is not only pandemic: the man-made property fire scenario takes 25% injured and 5% deaths among insured lives at the largest single property risk, and sandstorm adds emergency treatment (file 25).

## K5. Capital credit by structure: current rules vs RBC
| Structure | Current rules | RBC (SCA.04) |
|---|---|---|
| Medical / general QS | Premium margin falls to the 50% floor; the claims margin lags (3-year average) | Full credit through lower net premium exposure and net reserves (file 24); counterparty charge on ceded reserves + pipeline claims + commission at 1.5 / 5 / 50% by rating (file 22) |
| Group life QS | Credit up to 50% of capital at risk | Full credit on the 43% / 24% factors (LOB11-12) and on the pandemic life loss |
| Per-risk XoL | Nil | Credit in the man-made scenarios where the largest risk is hit (file 25); no credit in premium risk except through the lower net premium after the XoL premium |
| Cat XoL | Nil | Direct: recoveries deducted scenario by scenario, reinstatement premiums and refundable sliding-scale commission added back; counterparty charge at half the rating factor on the diversified recoveries (file 22, risk-mitigating effect) |
| Stop loss / aggregate | Nil | No explicit mechanism: premium risk is a factor on net exposure, and the only premium-risk mitigation items are reinstatement premium and sliding-scale commission. A scenario recovery from an aggregate cover is arguable as "existing reinsurance" (VERIFY with the IA guidance) |
| Sliding-scale commission | No effect | **Increases** the premium-risk charge when its impact is positive (file 24); refundable sliding commission is added back in scenarios |
| LPT / ADC | Slow (3-year average claims) | Net reserves fall (reserve risk, file 24); counterparty exposure rises by the ceded reserves |
| Long-term coinsurance | Credit capped at 50% | Net BEL falls in every life stress (file 23) |
| Fronting | As if 50% retained; can breach the 30% retention rule | Near nil underwriting charge, full counterparty charge on the fronted reserves; operational risk stays on gross premium |
| Collateral / funds withheld | n/a | Deducted from the counterparty loss, floored at zero per counterparty (not from the exposure) |
| Letter of credit | Not capital | Not addressed in SCA.04 (Own Funds template) |
| Reinsurer rating | No charge | Cliff between BBB (5%) and BB or unrated (50%) |

Reading the counterparty cost [INTERP]: the 5% for an A or BBB reinsurer applies to ceded technical provisions net of RA, pipeline claims and commission (less ECL), not to ceded premium. On a short-tail medical QS, ceded reserves are a fraction of ceded premium, so the charge per 100 of ceded premium is well below 5 before diversification (counterparties 0.25 correlated; Type 1 with Type 2 at 0.75; counterparty with non-life at 0.5 in Basic RBC).

Illustration from the owner's master file [INTERP]: a medical book per 100 GWP with an A-rated reinsurer needs 18-19 under both regimes at nil cession; at 70% ceded about 7.9 under RBC against 9.6 under the current rules, because RBC has no 50% floor. Basis as in the master file; for a real case compute with files 20-24.

Screening order [INTERP]:
1. Legality: finite ban (Art 19), rating, registration, 30% retention, local first refusal, approvals.
2. Which test binds (current rules in 2026; RBC from 2027) and whether the ratio target is the company's own.
3. Floors and caps (50% floor today; Op risk 30% cap).
4. Counterparty cost (rating cliff, collateral, payables offset).
5. IFRS 17 effect (RBC starts from IFRS 17 balances; `insurance-capital-ifrs17` files 00 and 04).

## K6. Main differences from Solvency II noted in the template [TEMPLATE] (specification Appendix C)

| Area | This framework | Solvency II |
|---|---|---|
| Interest rate shocks | SII table to year 20; long end 25.1% up / 27.7% down at 30+ | Falls to 20% at 90 years |
| Equity | TASI 36%, Nomu 41%, other KSA 46%, strategic KSA 19%; OECD 39%, other 49%, strategic 22%; symmetric adjustment | Type 1 39%, Type 2 49%, strategic 22% |
| Property | 15%–20% by type in KSA; 25% outside; 25% plant & equipment | 25% flat |
| Currency | 2.5% GCC USD-pegged, 5% other USD-pegged, 0% USD, 25% other | 25% |
| Spread | SII factors for KSA corporates; +5% relative for foreign corporates; KSA government 0 | Bonds, loans, securitisations, credit derivatives |
| Concentration | Thresholds 5% / 2.5% / 1%; factors 10%–75% | Thresholds 3% / 1.5%; factors 12%–73% |
| Counterparty Type 1 | Flat factors by rating (1.5% / 5% / 50%); LGD 50%, risk-mitigation LGD 25% | PD/LGD variance formula |
| Counterparty Type 2 | Three ageing buckets, lower factors for non-intermediaries | 15% / 90% over 3 months |
| Lapse | ±5 percentage points; 40% mass lapse | ±50% relative; mass lapse |
| Expense | +1pp inflation only | +10% expenses and +1pp inflation |
| Morbidity | +20% | +35% year 1, +25% thereafter, −20% recoveries |
| Premium risk | Applied to net loss ratio; local calibration blended with SII | Volume × 3σ |
| Nat CAT outside KSA | Factor × past-12-month earned premium | Based on next-12-month premium / sums insured by zone |
| Operational risk | 3% / 4% premium, 3% / 0.45% provisions, 30% BSCR cap, 25% UL expenses, cyber score adjustment | Same structure, no cyber adjustment, includes premium growth term |
| Available capital | Own Funds + Net RA + Net CSM | Own funds (risk margin is a liability) |


<!-- ===== FILE: references/29-ksa-source-register.md ===== -->

# KSA RBC: source register, open points, change history and load tests

As at 13 Nov 2026 (skill v1.0.0).

## Sources
| File | Built from | Date of source | Notes |
|---|---|---|---|
| 20-27 | IA "Solvency and Capital Template 2026" SCA.04, as restated in the owner's `KSA_RBC_Rules_vSCA04.md` | Template issued 25 Feb 2026 (YE2025, 5th dry run); specification 13 Nov 2026 | Sections 1-17 and Appendices A, B of the specification, unchanged in substance. Worked examples recomputed 13 Nov 2026: all match |
| 28 K1-K5 | Owner's "GCC Solvency Master File: KSA, Qatar (QFC) and UAE" | 12 Nov 2026 | Laws and IA circulars as summarised there, with corrections from the SCA.04 review (premium exposure, counterparty base, own-funds tiering, life-and-health catastrophe exposure) |
| 28 K6 | Specification Appendix C | 13 Nov 2026 | The template's own comparison with Solvency II |

The SCA.04 workbook itself is not part of this skill. A parameter not in files 20-27 is not defined in the template: say so rather than estimate it.

## Open points (VERIFY)
1. **Final RBC regulation for 1 Jan 2027:** minimum RBC ratio, intervention ladder, minimum capital amount. SCA.04 defines none of them. Replace every [DRY RUN] value when the final rules are published, and retire file 28 section K2.
2. **Own Funds:** tiering and eligibility (subordinated debt, letters of credit) are in the separate IA Own Funds assessment and reporting template, not in this skill.
3. **Stop loss and aggregate covers:** no mechanism in SCA.04 premium risk; whether a scenario recovery under an aggregate cover is accepted.
4. **Finite ban:** whether Art 19 of the 2010 Reinsurance Regulation carries into the 2027 regulations.
5. **Cooperative surplus split** (Implementing Regulations Art 70); minimum capital by licence type.
6. **KSA sovereign rating** (A+, bucket A) is used by the template for KSA government and PSE exposures: update if the rating changes.

## Maintenance rule
- Files 20-27 mirror the owner's specification; the Claude-side reference `ksa-rbc-knowledge` holds the same content. When either changes (a new SCA version, or the final regulation), regenerate the affected files, bump the skill version and add a line here.
- The cross-regime comparison of UAE and Qatar QFC is in `insurance-capital-ifrs17` (file 02). That skill no longer carries KSA content: this skill is the KSA authority.
- No client names, engagement notes or deal terms in this skill.

## Change history of the template relevant to interpretation (specification Appendix E)
- **SCA.02 (May 2024):** 99.5% calibration stated; equity categories (Nomu, strategic) and symmetric adjustment; property by type; interest rate shocks by term on the risk-free curve; spread risk module; concentration by issuer; Type 2 counterparty module; mass lapse; morbidity; geographical diversification for premium/reserve; recalibrated Nat CAT; sandstorm scenario; credit & suretyship scenario; operational risk formula with 30% cap; RA and CSM added to available capital; sum insured replaces PML.
- **SCA.03 / SCA.03.1 (March 2025):** admissibility removed from RBC; Projected RBC, LOB-wise Allocation, Input Collation, Validations tabs; fund look-through table; KSA government and other government categories; property outside KSA; automated bottom-up interest rate; Type 1 net loss gives full credit to payables and collateral; <90-day Type 2 bucket; one-year view for premium/reserve factors; group life reserve factor 36% → 24%; Nat CAT outside KSA by 18 regions; standardised man-made CAT cost assumptions; life charges as pre/post-stress difference; cybersecurity adjustment.
- **SCA.04 (February 2026):** USD-pegged currency categories; automated currency charge; corporate split inside/outside KSA (+5%); PSE category at KSA sovereign rating (A+); symmetric adjustment on 2025 data; interest rate risk mitigation inputs; "Other Assets" module removed — plant & equipment moved into property risk, intangibles a separate market sub-module, goodwill handled in Own Funds; windstorm scenario; loss component added to premium risk exposure; Own Funds made an input; alternative projections; sign-off record; rating mapping table.

## Worked examples (specification Appendix D; amounts in SR '000)
Amounts in SR '000. Use these to check an implementation of the rules.

**Spread factors.** Corporate inside KSA, A, D = 3 → 0.014 × 3 = 4.20%. Corporate inside KSA, BBB, D = 7.5 → 0.125 + 0.015 × 2.5 = 16.25%. Corporate outside KSA, AA, D = 12 → 1.05 × (0.084 + 0.005 × 2) = 9.87%. Other government, A, D = 8 → 0.055 + 0.006 × 3 = 7.30%. PSE entered as BB, D = 16 → treated as A: 0.13 + 0.005 × 1 = 13.50%. Corporate inside KSA, Unrated, D = 25 → 0.3825 + 0.005 × 5 = 40.75%. Corporate inside KSA, B and CCC or below, D = 5 → 0.075 × 5 = 37.50%.

**Top-down stressed rate.** Rate 5%, duration 7.5 → up 5% × (1 + (0.49 + 0.47)/2) = 7.40%; down 5% × (1 − (0.39 + 0.36)/2) = 3.125%.

**Concentration.** Asset base 540,000; Corporate inside KSA issuer rated A with exposure 60,000: share 11.11%, excess 6.11%, loss = 540,000 × 6.11% × 17.5% = 5,775. Property 70,000: share 12.96%, excess 2.96%, loss = 540,000 × 2.96% × 12% = 1,920.

**Type 1 counterparty.** Reinsurer rated AA: ceded TP 20,000, pipeline 1,000, commission 500, ECL 50, risk-mitigating-effect share 4,000, payable 300, collateral 100 → gross exposure 21,450; gross loss = 1.5% × 21,450 + 0.75% × 4,000 = 351.75; net loss = max(351.75 − 300 − 100, 0) = 0.

**Health pandemic.** 200,000 insured lives → 200,000 × 0.001995 = 399 gross.

**Market aggregation.** [IR 28.7332, Equity 9,988.6161, Property 4,897.9588, Spread 1,660.05, Concentration 13,644.2250, Currency 290] with Matrix 1 → 20,543.5121; plus intangibles 2,400 → **22,943.5121**.

**Non-Life UW.** [Premium 22,017.3007, Reserve 5,495.6067, CAT 347,155.2724] with Matrix 3 → **354,949.1083**.

**Basic RBC.** [Market 22,943.5121, CD 2,566.6729, Life UW 2,816.0256, Non-Life UW 354,949.1083] with Matrix 5 → **362,736.9333**.

**Operational risk.** Gross EP non-life 150,000 / 160,000, long-term 5,000 / 5,500; TP 60,000 and 50,000; unit-linked expenses 400; cyber score 60%. Op_premium = 3% × 160,000 + 4% × 5,500 = 5,020; Op_provision = 1,800 + 225 = 2,025; cap = 30% × 362,736.93 = 108,821; Op_base = 5,020 + 100 = 5,120; × 1.025 = **5,248**.

**RBC and ratio.** RBC = 362,736.9333 + 5,248 = **367,984.9333**. Own Funds 600,000 + Net RA 20,000 + Net CSM 5,000 → ratio = 625,000 / 367,984.93 = **169.84%**.

## Load-test questions (expected answer in brackets)
- **T1.** What is the RBC premium-risk factor for medical, and for one-year group life?
  - [Medical LOB9: 13% premium, 15% reserve (direct and proportional). Group life LOB11: 43% / 24%, in the non-life module, not life. Must tag [DRY RUN]. File 24.]
- **T2.** What is the premium-risk exposure for a line?
  - [max(last year's NEP, next year's NEP + loss component) + future premium on existing and new long-term contracts; non-proportional inwards separately at 51%; then geographical diversification 0.75 + 0.25 x Herfindahl over 7 regions. File 24.]
- **T3.** A reinsurer rated AA has ceded TP 20,000, pipeline 1,000, commission 500, ECL 50, risk-mitigating share 4,000, payable 300, collateral 100. Counterparty loss?
  - [Gross exposure 21,450; gross loss 351.75; net loss 0 (payables and collateral come off the loss, floored at zero). File 22.]
- **T4.** Reproduce the Basic RBC, RBC and ratio of the worked example.
  - [Basic RBC 362,736.93 (Matrix 5); operational 5,248 (cyber score 60% gives +2.5%); RBC 367,984.93; ratio 625,000 / 367,984.93 = 169.84%. Files 20, 26.]
- **T5.** A life and health-only insurer: which catastrophe scenarios hit it?
  - [Health pandemic (2% infected, 95% rejected, SAR 15,000 hospital / SAR 550 consultation: about SAR 2 per life; group life 0.06% x life-years x average sum at risk), man-made property fire (25% injured, 5% deaths among insured lives at the largest property risk), sandstorm health (0.5% x regional weight x insured lives x SAR 500). File 25.]
- **T6.** What is the operational risk charge if the cybersecurity score is left blank?
  - [Zero in the template: it must be flagged as a template behaviour, not a real nil charge. File 27 section 16, item 1.]
- **T7.** Does a sliding-scale commission reduce RBC?
  - [No: its impact is added to the premium-risk loss and raises the charge "after risk mitigation". File 24; file 28 K5.]
- **T8.** Medical insurer under today's rules (2026): when does the claims method bind, and how much credit for a 70% QS?
  - [Above a net loss ratio of about 67% (16% NWP vs 24% three-year claims). Credit stops at the 50% floor; 70% is the maximum cession under the 30% retention rule (Art 40). File 28 K2, K3.]
- **T9.** What is the minimum RBC ratio?
  - [Not defined in SCA.04; no ladder either. Do not invent one. File 20 section 11; file 29 open point 1.]
