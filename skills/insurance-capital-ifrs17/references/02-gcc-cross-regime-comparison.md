# Core: GCC regimes side by side - UAE and Qatar QFC

Use this file to compare regimes and to see how each regime credits each reinsurance structure. **KSA is not in this skill:** Saudi solvency (current margin rules and the 2027 risk-based capital, SCA.04) is in the separate skill `ksa-rbc-capital`; ask the user to load it with `/ksa-rbc-capital`. For UAE or QFC detail, the country files (10-13, 30-33) are the authority; where this file and a country file differ, the country file wins and the difference should be reported.

Section codes A0-A9 are used by the other files of this skill.

Source: the owner's working file "GCC Solvency Master File: KSA, Qatar (QFC) and UAE" (12 Nov 2026), condensed, UAE and QFC parts only. The master file itself is not part of this skill: where a table is needed in full, ask for it. Tags: [RULE] law or rulebook; [TEMPLATE] regulator workbook; [INTERP] interpretation; VERIFY = check the primary document. This is analysis, not legal advice.
Not covered: DIFC, ADGM, and onshore Qatar under QCB. Never apply QFC rules to a QCB-licensed insurer.
Factor levels are not comparable across regimes because each uses a different base: UAE gross premium x net/gross floor; QFC net liabilities.

### A0 Regimes and what binds
| | UAE | QFC |
|---|---|---|
| Instrument | IA Decision 25/2014 S2 (takaful 26/2014); eForms v1.7; Decree-Law 6/2025 | PINS v20 (1 Oct 2025), Sch 3 |
| Type | Modular, correlated, factor-based; 99.5% VaR | Factor sum, no diversification |
| Floor | MCR AED 100m (reinsurer AED 250m), met from BOF only | QAR 36m (LLC); nil for branches |
| Tests | max(MCR, MGF, SCR) | Capital >= max(QAR 36m, RBC) and >= 150% RBC |
| Liability basis | Statutory provisions | IFRS 17 (AAOIFI for takaful) |
| Reinsurance credit | Net/gross with floors (50 / 25 / 85%) | Net, no floor |

What binds [INTERP]:
- **UAE:**
  - MCR binds for small or loss-making companies; reinsurance and LoCs do not help.
  - MGF (26% of NEP) binds for high-retention health and motor writers.
  - SCR binds where asset risk is heavy or cession is already high.
- **QFC:** the QAR 36m floor binds until RBC exceeds QAR 24m. Above that the 150% test binds, so each 1 of RBC removed frees 1.5. Breaching the minimum stops new business; breaching 150% needs a board plan.

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
- **Instruments [INTERP]:** a reinsurer LoC helps only in the UAE (SCR and MGF). A sub loan works today in QFC (LT2).

### A2 Health and non-life underwriting (premium % / reserve %)
Methods:
- UAE: gross x max(net/gross, floor). Premium and reserve combined at 0.5, health segments at 0.5.
- QFC: net premium liability / net OS claims, simple sum.

| Line | UAE (floor) | QFC |
|---|---|---|
| Medical | 5 / 5 (50%) | 16 / 11 (12 / 8 on application) |
| Personal accident | 5 / 5 | 16 / 11 |
| Motor own damage / comprehensive | 8 / 8 | 13 / 9 |
| Motor TPL / compulsory | 10 / 9 | 21 / 14 |
| Property / fire | 8-10 / 10-12 (50%) | 16 / 11 |
| Engineering, energy | 17 / 16 (25%) | 16 / 11 |
| Marine, aviation | 15 / 11 (25%) | 16 / 11 (hull), 21 / 14 (liability) |
| Liability | 8-10 / 11 (50%) | 21 / 14 |
| Group life / credit life, 1 year | 2 / 1 (85%), life module | long-term component (VERIFY) |
| Inward non-proportional | 15-17 / 20 | 18-26 / 12-17 |

Other line features:
- **Only UAE:** lapse risk on short-term business = 40% x expected future profit (profit ratio capped at 25%).
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
- **Long-term life:**
  - UAE: seven shocks on net provisions (mortality +15%, longevity -20%, morbidity +35% then +25%, lapse +/-50% or 40% mass, expense +10% and +1 pt inflation, revision +3%, cat +0.15 pts); full credit.
  - QFC: 3% of provisions + 0.15% CaR; unit-linked 0.5% (1.25% with guarantee).

### A4 Catastrophe
- **UAE:** factor x NWP by location of risk; cat XoL barely counts.
  - Health: UAE 4%, GCC 4.6%, MENA 6.2%, rest of world 8%.
  - Group life: UAE 2% up to 4%.
  - Non-life: UAE 4%, GCC 3.8%, MENA 4.7%, rest of world 6.5%.
- **QFC:** maximum event retention at 1-in-250 or longer + one reinstatement. With no cat cover, the template charges 2 x the largest per-risk retention. Cat XoL gets direct credit.

### A5 Counterparty (charge per 100 of reinsurance exposure)
| Rating | UAE | QFC (recognised regulator / other) |
|---|---|---|
| AAA | 0.001 | 1.0 / 1.2 |
| AA | 0.005 | 2.0 / 2.4 |
| A | 0.025 | 4.0 / 4.8 |
| BBB | 0.12 | 6.0 / 7.2 |
| BB or below / unrated | 0.6-2.09 | 8 / 9.6 (unrated 6 / 7.2) |

- **UAE:** exposure is 50% of recoverables; 80% of collateral is deducted. Premium receivables are charged 15% under 3 months, 90% beyond.
- **QFC:** +20% surcharge where the reinsurer's regulator is not recognised. A split rating takes the highest charge.
- [INTERP] In QFC, ceding 100 to an A-rated reinsurer adds back about 4-5. In the UAE the rating barely matters above BBB.

### A6 Operational and market (headline only)
- **Operational:**
  - UAE: max(5% GEP, 3% TP non-life and health / 0.5% life), capped at 30% BSCR; growth load above 20%.
  - QFC: max(2% GWP, 2% TP), capped at 15/85 of other risks.
  - All are on gross volumes. Cession only cuts operational risk once the cap binds.
- **Market:**
  - Listed equity: UAE 20%, QFC 16%.
  - Currency: UAE RoW 10%; QFC none.
  - QFC has no interest-rate, FX or concentration charge.
- **UAE localisation:** assets matching reserves held in the UAE; at least 5% in UAE banks.

### A7 Reinsurance rules and capital credit by structure
Cession rules:
- **Rating:** UAE S&P BBB on a full rating (Decision 23/2019). QFC: no rule, rating drives the charge.
- **Finite reinsurance:** prohibited in UAE (Art 25). Not addressed in QFC PINS (VERIFY other modules).
- **UAE only:** 0.5% provision on ceded premium each year, accumulating (Art 34); inward <= 49% of premium; 3-year board reinsurance plan; prior approval for liability transfers (CB Law Art 125).

| Structure | UAE | QFC |
|---|---|---|
| Medical / general QS | SCR to 50% retained (25% MAEE); MGF keeps falling | Full; asset charge 1-9.6% |
| Group life QS | First 15% only | Full |
| Per-risk / cat XoL | About nil | Via MER (or 2 x retention) |
| Stop loss / aggregate | About nil | Expected recoveries only |
| Sliding-scale commission | No effect | Via IFRS 17 |
| LPT / ADC | Net reserve with floor; Art 125 approval | Net claims fall |
| Long-term coinsurance | Full (net shocks) | CaR falls |
| Fronting | As if 50% retained | Near nil plus floor and recoverable charge |
| Collateral / funds withheld | 80% off exposure | Collateral's own factor |
| LoC | 50% for SCR and MGF | Not capital |

Screening order [INTERP]:
1. Legality: finite ban, rating, registration, approvals.
2. The binding test.
3. Floors and caps.
4. Counterparty cost.
5. The IFRS 17 effect (QFC starts from IFRS 17).

### A8 Governance and takaful
- **Breach:**
  - UAE: plan in 30 days; SCR/MCR compliance in 6 months, MGF in 3; reports every 30 days.
  - QFC: below the minimum, stop new business; below 150%, an action plan.
- **Reporting:** UAE quarterly within 45 days. QFC within 1 month.
- **Takaful:**
  - UAE: qard hasan up to shareholders' equity within 15 days; reinsurance commission belongs to the fund; retakaful first.
  - QFC: no loans from a takaful fund.

### A9 Illustrative medical book (per 100 GWP, A-rated reinsurer)
At nil cession:
- UAE MGF 26
- QFC (x150%) about 15
- UAE SCR (underwriting only) about 12

UAE SCR flattens at 50% ceded. MGF and QFC keep falling. For each unit ceded, QFC gives back over a quarter of the relief through the reinsurance asset charge.

Open items: whether eForms v1.7 is the version currently filed; QFC category mapping and group life classification. Re-date on any source change.

KSA (current margin rules, 2027 risk-based capital, KSA reinsurance rules and capital credit by structure for a Saudi cedant): skill `ksa-rbc-capital`, file 28 for the structure table and files 20-27 for the RBC rules.
