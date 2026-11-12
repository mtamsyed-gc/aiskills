# Core: GCC regimes side by side - UAE, Qatar QFC, KSA today and KSA risk-based capital (condensed)

Use this file to compare regimes, to answer a KSA question (no full KSA overlay is loaded yet: this file is the only KSA content, and it is condensed), and to see how each regime credits each reinsurance structure. For UAE or QFC detail, the country files (10-13, 30-33) are the authority; where this file and a country file differ, the country file wins and the difference should be reported.

Section codes A0-A9 are used by the other files of this skill.

Source: the owner's working file "GCC Solvency Master File: KSA, Qatar (QFC) and UAE" (12 Nov 2026), condensed. The master file itself is not part of this skill: where a table is needed in full, ask for it. Tags: [RULE] law or rulebook; [TEMPLATE] regulator workbook; [DRY RUN] KSA-RBC SCA.04 (YE2025, 5th dry run), parameters can still change; [INTERP] interpretation; VERIFY = check the primary document. This is analysis, not legal advice.
Not covered: DIFC, ADGM, and onshore Qatar under QCB. Never apply QFC rules to a QCB-licensed insurer.
Factor levels are not comparable across regimes because each uses a different base: UAE gross premium x net/gross floor; QFC net liabilities; KSA-now NWP or 3-year average claims; KSA-RBC NEP and net reserves.

### A0 Regimes and what binds
| | UAE | QFC | KSA-now | KSA-RBC |
|---|---|---|---|---|
| Instrument | IA Decision 25/2014 S2 (takaful 26/2014); eForms v1.7; Decree-Law 6/2025 | PINS v20 (1 Oct 2025), Sch 3 | Implementing Regs Arts 63-68; ends 31 Dec 2026 | SCA.04 template; mandatory 1 Jan 2027 |
| Type | Modular, correlated, factor-based; 99.5% VaR | Factor sum, no diversification | Solvency I volume margin | Modular, 17 correlation matrices, stress and scenarios; 99.5% |
| Floor | MCR AED 100m (reinsurer AED 250m), met from BOF only | QAR 36m (LLC); nil for branches | SAR 100m / 200m; SAR 300m in practice | Planned, amount not published |
| Tests | max(MCR, MGF, SCR) | Capital >= max(QAR 36m, RBC) and >= 150% RBC | max(min capital, premium or claims margin) | RBC; ratio not yet prescribed |
| Liability basis | Statutory provisions | IFRS 17 (AAOIFI for takaful) | Statutory forms | IFRS 17; RA and CSM stripped from exposures and added to capital |
| Reinsurance credit | Net/gross with floors (50 / 25 / 85%) | Net, no floor | Net, floored at 50% of gross | Net, no floor |

What binds [INTERP]:
- **UAE:**
  - MCR binds for small or loss-making companies; reinsurance and LoCs do not help.
  - MGF (26% of NEP) binds for high-retention health and motor writers.
  - SCR binds where asset risk is heavy or cession is already high.
- **QFC:** the QAR 36m floor binds until RBC exceeds QAR 24m. Above that the 150% test binds, so each 1 of RBC removed frees 1.5. Breaching the minimum stops new business; breaching 150% needs a board plan.
- **KSA-now:** the claims margin binds above a net loss ratio of health 67%, motor 80%, fire 80%, liability 86%, other 53% (premium/claims factors: health 16/24, motor 20/25, fire 16/20, liability 30/35, EMAE 30/30, other 16/30, inward 30/30). Only the premium method applies in the first 3 years.
- **KSA-RBC:** sector RBC is about 30-41% of NEP, with premium risk the top risk. YE2024 ratio was 182% under RBC against 206% under the current rules.

### A1 Capital resources
- **UAE:**
  - BOF = admissible assets less liabilities. Approved subordinated items count in BOF up to the MCR shortfall; the excess goes to AOF at 50%.
  - **Only UAE:** AOF (LoCs, guarantees, uncalled capital) count 50% toward SCR and MGF, 0% toward MCR.
  - DAC is nil (except first-year long-term life). Negative IBNR is never admissible.
  - Reinsurance receivables age from invoice date: UAE reinsurers 100% to 180 days, then 75 / 50 / 0%; foreign reinsurers 100% to 90 days, then 75 / 50 / 25 / 0%.
  - Dividends need CBUAE no-objection.
- **QFC:**
  - Tiers: T1, UT2 (perpetual hybrids), LT2 (sub debt of at least 5 years, no step-up in the first 5, amortised 20% a year over the last 4; LT2 <= 50% of net T1; total T2 <= 100%).
  - CSM and RA are liabilities, not capital. LoCs are not capital. DAC, DTA, fixed assets and subsidiaries are deducted. Interim profits count only once auditor-verified.
- **KSA-now:** net admissible assets by fund; Table 2 admission limits.
- **KSA-RBC:**
  - Available capital = Own Funds + net RA + net CSM.
  - Admissibility has no effect on RBC.
  - Sub debt expected to be eligible (IA, Apr 2026).
  - Tiering not published.
- **Instruments [INTERP]:** a reinsurer LoC helps only in the UAE (SCR and MGF). A sub loan works today only in QFC (LT2) and is expected in KSA from 2027.

### A2 Health and non-life underwriting (premium % / reserve %)
Methods:
- UAE: gross x max(net/gross, floor). Premium and reserve combined at 0.5, health segments at 0.5.
- QFC: net premium liability / net OS claims, simple sum.
- KSA-now: NWP / 3-year average net incurred claims, higher of the two.
- KSA-RBC: NEP / net discounted reserves at 0.75; geographic factor 0.75 + 0.25 x concentration.

| Line | UAE (floor) | QFC | KSA-now | KSA-RBC |
|---|---|---|---|---|
| Medical | 5 / 5 (50%) | 16 / 11 (12 / 8 on application) | 16 / 24 | 13 / 15 |
| Personal accident | 5 / 5 | 16 / 11 | 16 / 30 | 31 / 26 |
| Motor own damage / comprehensive | 8 / 8 | 13 / 9 | 20 / 25 | 18 / 19 (mixed book) |
| Motor TPL / compulsory | 10 / 9 | 21 / 14 | 20 / 25 | 31 / 23 |
| Property / fire | 8-10 / 10-12 (50%) | 16 / 11 | 16 / 20 | 29.5 / 22.5 |
| Engineering, energy | 17 / 16 (25%) | 16 / 11 | 30 / 30 | 27 / 20; energy 29.5 / 22.5 |
| Marine, aviation | 15 / 11 (25%) | 16 / 11 (hull), 21 / 14 (liability) | 30 / 30 | 45 / 24 |
| Liability | 8-10 / 11 (50%) | 21 / 14 | 30 / 35 | 31 / 26 |
| Group life / credit life, 1 year | 2 / 1 (85%), life module | long-term component (VERIFY) | Art 67 | **43 / 24**, non-life module |
| Inward non-proportional | 15-17 / 20 | 18-26 / 12-17 | 30 / 30 | 51 / 60 |

Other line features:
- **Only UAE:** lapse risk on short-term business = 40% x expected future profit (profit ratio capped at 25%).
- **Only KSA-RBC:** reinstatement premiums and sliding-scale commission are added to the loss.
- **UAE MGF (SM-6)** is on NEP:
  - 26% (min AED 3m): personal lines, medical, PA
  - 31% (AED 5m): commercial fire, marine, commercial motor, inward non-proportional
  - 36% (AED 7m): aviation, engineering, energy
  - life on net sum at risk: 0.2% (group life <= 1 year), 0.25%, 0.4%
  - Build: the lower of (sum by line with minimums) and (total NEP x weighted factor of the top 5 lines). MGF = max(non-life + life, SCR/3). VERIFY the units of the minimums.
  - MGF rewards cession with no floor.

### A3 Life
- **Short-term group life:**
  - UAE: credit stops after 15% ceded (85% floor); cat 2% of NWP; MGF 0.2% of net sum at risk.
  - QFC: 3% of provisions + 0.1% CaR + 0.05% mortality CaR; full credit.
  - KSA-now: 4% of provisions + 0.1% group CaR; credit capped at 50% of CaR.
  - KSA-RBC: 43% NEP, 24% reserves; pandemic 0.06% x life-years x average SaR; full credit.
  - [INTERP] Group life QS is worth far more in KSA from 2027.
- **Long-term life:**
  - UAE: seven shocks on net provisions (mortality +15%, longevity -20%, morbidity +35% then +25%, lapse +/-50% or 40% mass, expense +10% and +1 pt inflation, revision +3%, cat +0.15 pts); full credit.
  - QFC: 3% of provisions + 0.15% CaR; unit-linked 0.5% (1.25% with guarantee).
  - KSA-now: 4% of provisions + 0.3% individual CaR; credit capped at 50%. Art 20 bars reinsuring the investment element of savings contracts.
  - KSA-RBC: mortality +15%, morbidity +20%, lapse +/-5 pts or 40% mass, expense +1 pt; **no longevity stress**.

### A4 Catastrophe
- **UAE:** factor x NWP by location of risk; cat XoL barely counts.
  - Health: UAE 4%, GCC 4.6%, MENA 6.2%, rest of world 8%.
  - Group life: UAE 2% up to 4%.
  - Non-life: UAE 4%, GCC 3.8%, MENA 4.7%, rest of world 6.5%.
- **QFC:** maximum event retention at 1-in-250 or longer + one reinstatement. With no cat cover, the template charges 2 x the largest per-risk retention. Cat XoL gets direct credit.
- **KSA-RBC:** named scenarios on sums insured, combined by root sum of squares. Recoveries are deducted scenario by scenario, reinstatement premiums added back, and the reinsurer default charge applies at half the rating factor on cat recoveries.
  - Medical pandemic is about SAR 2 per life (negligible).
  - Property fire takes 100% of the largest treaty risk; flood uses ground-floor sums insured.
- **KSA-now:** no cat charge.

### A5 Counterparty (charge per 100 of reinsurance exposure)
| Rating | UAE | QFC (recognised regulator / other) | KSA-now | KSA-RBC |
|---|---|---|---|---|
| AAA | 0.001 | 1.0 / 1.2 | 0 | 1.5 |
| AA | 0.005 | 2.0 / 2.4 | 0 | 1.5 |
| A | 0.025 | 4.0 / 4.8 | 0 | 5.0 |
| BBB | 0.12 | 6.0 / 7.2 | 0 | 5.0 |
| BB or below / unrated | 0.6-2.09 | 8 / 9.6 (unrated 6 / 7.2) | 0 | 50 |

- **UAE:** exposure is 50% of recoverables; 80% of collateral is deducted. Premium receivables are charged 15% under 3 months, 90% beyond.
- **QFC:** +20% surcharge where the reinsurer's regulator is not recognised. A split rating takes the highest charge.
- **KSA-RBC:**
  - exposure = ceded provisions net of RA + pipeline claims + commission - ECL
  - collateral is deducted from the loss
  - counterparties correlated at 0.25
  - cliff at BBB (5) vs BB or unrated (50)
  - broker receivables charged 15 / 45 / 90% against 3.75 / 7.5 / 15% for policyholders and TPAs
- [INTERP] In QFC and KSA-RBC, ceding 100 to an A-rated reinsurer adds back about 4-5. In the UAE the rating barely matters above BBB. Unrated regional capacity is about 10x costlier in KSA-RBC.

### A6 Operational and market (headline only)
- **Operational:**
  - UAE: max(5% GEP, 3% TP non-life and health / 0.5% life), capped at 30% BSCR; growth load above 20%.
  - QFC: max(2% GWP, 2% TP), capped at 15/85 of other risks.
  - KSA-RBC: max(3% GEP, 3% TP) non-life; 4% / 0.45% life; capped at 30% BRSCR; x0.95-1.05 cyber score.
  - All are on gross volumes. Cession only cuts operational risk once the cap binds.
- **Market:**
  - Listed equity: UAE 20%, QFC 16%, KSA TASI 27%, OECD 46.9%.
  - Currency: UAE RoW 10%; QFC none; KSA non-pegged 25%.
  - QFC has no interest-rate, FX or concentration charge.
- **UAE localisation:** assets matching reserves held in the UAE; at least 5% in UAE banks.

### A7 Reinsurance rules and capital credit by structure
Cession rules:
- **Rating:** UAE S&P BBB on a full rating (Decision 23/2019). KSA BBB / AM Best B+, approval if lower. QFC: no rule, rating drives the charge.
- **Finite reinsurance:** prohibited in UAE (Art 25) and KSA (2010 Reinsurance Regulation Art 19; carry-over into the 2027 regulations not confirmed). Not addressed in QFC PINS (VERIFY other modules).
- **Retention:** KSA retain >= 30% of total premium (Art 40).
- **Local cession:** KSA 30% first refusal to local reinsurers (from 1 Jan 2025). Mechanics and WHT: skill `reinsurance-pricing-knowledge`, Part F.
- **Registration:** KSA foreign reinsurers on the IA platform. KSA gearing: approval if GWP > 10x capital and reserves (Art 48).
- **UAE only:** 0.5% provision on ceded premium each year, accumulating (Art 34); inward <= 49% of premium; 3-year board reinsurance plan; prior approval for liability transfers (CB Law Art 125).
- **KSA reporting:** profit and loss sharing, caps, swing rates and reinstatements reported; annual strategy filed by 30 April.

| Structure | UAE | QFC | KSA-now | KSA-RBC |
|---|---|---|---|---|
| Medical / general QS | SCR to 50% retained (25% MAEE); MGF keeps falling | Full; asset charge 1-9.6% | Premium margin to 50% floor; claims margin lags | Full; default charge 1.5-50% |
| Group life QS | First 15% only | Full | Up to 50% of CaR | Full |
| Per-risk / cat XoL | About nil | Via MER (or 2 x retention) | Nil | Direct, by scenario |
| Stop loss / aggregate | About nil | Expected recoveries only | Nil | No explicit credit (VERIFY guidance manual) |
| Sliding-scale commission | No effect | Via IFRS 17 | No effect | **Increases** the charge |
| LPT / ADC | Net reserve with floor; Art 125 approval | Net claims fall | Slow (3-year average) | Net reserves fall; counterparty rises |
| Long-term coinsurance | Full (net shocks) | CaR falls | Capped at 50% | Net BEL |
| Fronting | As if 50% retained | Near nil plus floor and recoverable charge | As if 50% retained; breaches 30% retention | Near nil plus full counterparty charge |
| Collateral / funds withheld | 80% off exposure | Collateral's own factor | n/a | Off the loss |
| LoC | 50% for SCR and MGF | Not capital | Not capital | Not published |

Screening order [INTERP]:
1. Legality: finite ban, rating, registration, approvals.
2. The binding test.
3. Floors and caps.
4. Counterparty cost.
5. The IFRS 17 effect (QFC and KSA-RBC start from IFRS 17).

### A8 Governance and takaful
- **Breach:**
  - UAE: plan in 30 days; SCR/MCR compliance in 6 months, MGF in 3; reports every 30 days.
  - QFC: below the minimum, stop new business; below 150%, an action plan.
  - KSA-now ladder: 75-100% restore by next quarter; 50-75% corrective plan; 25-50% regulator measures; below 25% adviser or cease. KSA-RBC ladder not published.
  - KSA also has Companies Law triggers at 50% accumulated losses.
- **Reporting:** UAE quarterly within 45 days. QFC within 1 month. KSA monthly within 15 working days, with 4-year RBC projections.
- **Takaful:**
  - UAE: qard hasan up to shareholders' equity within 15 days; reinsurance commission belongs to the fund; retakaful first.
  - QFC: no loans from a takaful fund.
  - KSA: all insurers are cooperative; VERIFY the Art 70 surplus split.

### A9 Illustrative medical book (per 100 GWP, A-rated reinsurer)
At nil cession:
- UAE MGF 26
- KSA-now / KSA-RBC 18-19
- QFC (x150%) about 15
- UAE SCR (underwriting only) about 12

UAE SCR and KSA-now flatten at 50% ceded. MGF, QFC and KSA-RBC keep falling (KSA-RBC 7.9 at 70% ceded against 9.6 under KSA-now). For each unit ceded, QFC gives back over a quarter of the relief through the reinsurance asset charge.

Open items: KSA-RBC tiering, ratio, ladder and MCR; KSA-RBC treatment of stop loss; whether eForms v1.7 is the version currently filed; QFC category mapping and group life classification. Re-date on any source change. On 1 Jan 2027, retire the KSA-now columns and replace [DRY RUN] values with the final regulation.
