# KSA: current solvency rules, reinsurance rules, capital credit by structure, and comparison with Solvency II

Load for anything about a Saudi insurer that is NOT a calculation inside the Solvency and Capital Template (SCA.07) or the Own Funds template: the solvency margin rules in force until 31 Dec 2026, the reinsurance and legal rules that screen a structure, how each reinsurance structure is credited under today's rules and under RBC, breach and reporting rules, and how the framework compares with Solvency II.

Sources and tags:
- Sections K1-K5 come from the owner's working file "GCC Solvency Master File: KSA, Qatar (QFC) and UAE" (12 Nov 2026), not from the SCA.04 template. Tags: **[RULE]** law or regulation (Implementing Regulations of the Cooperative Insurance Companies Control Law, 2010 Reinsurance Regulation, IA circulars); **[INTERP]** interpretation or market practice; **VERIFY** = check the primary text before a client relies on it.
- Section K6 is Appendix C of the SCA.04 specification **[TEMPLATE] [DRY RUN]**.
- Withholding tax on premium to non-resident reinsurers and the 30% local first refusal are in the companion skill `reinsurance-pricing-knowledge` (file 03); only the one-line rule is repeated here.
- Analysis, not legal advice.

## K1. The two regimes and the switch-over
| | Current rules ("KSA-now") | Risk-based capital ("KSA-RBC") |
|---|---|---|
| Instrument | Implementing Regulations Arts 63-68 **[RULE]**; in force to 31 Dec 2026 | IA Solvency and Capital Template (SCA.07, files 20-27) and Own Funds and Solvency Assessment Template (file 30); quarterly dry runs in 2026; mandatory from 1 Jan 2027 (VERIFY the final regulation) |
| Type | Solvency I volume margin | Modular, 17 correlation matrices, stresses and scenarios, 99.5% one-year |
| Floor | Minimum capital SAR 100m / SAR 200m (VERIFY which applies to which licence); SAR 300m in practice | MCR = RBC / 3 with absolute floor checks SR 20m insurer / 40m reinsurer or composite / 10m captive insurer / 20m captive reinsurer **[TEMPLATE] [DRY RUN]** (file 30); paid-up minimum capital under the Implementing Regulations unaffected (VERIFY) |
| Test | Required margin = max(minimum capital, premium-method or claims-method margin) | RBC solvency ratio = eligible own funds / RBC; MCR tier tests (T1 ≥ 80% MCR, T2 ≤ 20% MCR); no minimum ratio or intervention ladder in either template |
| Liability basis | Statutory forms | IFRS 17, with RA and CSM taken out of exposures and added to available capital |
| Reinsurance credit | Net, floored at 50% of gross | Net, no floor; offset by the counterparty charge (file 22) |
| Capital resources | Net admissible assets by fund (policyholders G&H, policyholders P&S, shareholders); Table 2 admission limits | Eligible own funds (file 30): Tier 1 in full, Tier 3 ≤ 15% of RBC, Tier 2 + Tier 3 ≤ 50% of RBC, Tier 1 ≥ 50% of RBC; then + net RA + net CSM − own shares − goodwill − foreseeable dividends − intangibles − deferred tax. Basic and ancillary (T2, T3) own funds. Tiering criteria not published. Admissibility has no effect |

The template's "Regulatory Solvency" sheet reports the current-rules position alongside RBC for 2025, the current quarter and 2026 (file 27, section 12): it only adds up inputs and does not hold the premium or claims method formulas.

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
- **Subordinated debt:** expected to be eligible as own funds under RBC (IA statement, Apr 2026). The Own Funds template (file 30) has Tier 2 and Tier 3 rows and the Solvency II-style limits, but no classification criteria: a subordinated loan would most likely be Tier 2, capped with Tier 3 at 50% of RBC and at 20% of MCR **[INTERP]**, VERIFY with the IA.

## K4. What binds and sector context [INTERP]
- Under the current rules a medical writer is bound by the claims method once its net loss ratio exceeds about 67%; reinsurance credit stops at 50% ceded.
- Under RBC, sector RBC is about 30-41% of NEP with premium risk the largest module; the YE2024 dry-run ratio was 182% under RBC against 206% under the current rules (owner's master file, from IA dry-run feedback; VERIFY the latest IA publication).
- For a property or energy writer, catastrophe (man-made property fire, energy) can dominate RBC, because the scenarios take 100% of the largest treaty risk's sum insured: in the specification's stylised worked example CAT is 347k of a 355k non-life charge (file 29).
- For a life and health book, the catastrophe charge is not only pandemic: the man-made property fire scenario takes 25% injured and 5% deaths among insured lives at the largest single property risk, and sandstorm adds emergency treatment (file 25).

## K5. Capital credit by structure: current rules vs RBC
| Structure | Current rules | RBC (SCA.07; unchanged from SCA.04 for every row) |
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
| Letter of credit | Not capital | Possibly ancillary own funds (Tier 2 / Tier 3 rows exist in the Own Funds template, file 30); no criteria or approval process published **[INTERP]**, VERIFY |
| Reinsurer rating | No charge | Cliff between BBB (5%) and BB or unrated (50%) |

Since SCA.07 the company also reports each treaty set's effect as gross minus net RBC by module on the `Reinsurance Impact` sheet (file 27 section 12A), so the IA sees the relief directly. A capital action that lowers RBC also lowers the room for Tier 2 and Tier 3 own funds (file 30) **[INTERP]**.

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
| Available capital | Eligible own funds incl. net RA and net CSM, after deductions; tier limits as Solvency II (file 30) | Own funds (risk margin is a liability); same tier limits |
