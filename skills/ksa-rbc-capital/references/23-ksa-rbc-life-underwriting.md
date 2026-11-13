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
