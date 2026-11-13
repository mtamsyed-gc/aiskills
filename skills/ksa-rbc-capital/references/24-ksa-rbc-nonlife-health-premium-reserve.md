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
