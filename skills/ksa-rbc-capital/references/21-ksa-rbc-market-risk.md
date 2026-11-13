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
