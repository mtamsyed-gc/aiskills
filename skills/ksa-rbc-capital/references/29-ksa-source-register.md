# KSA RBC: source register, open points, change history and load tests

As at 20 Nov 2026 (skill v1.1.0; v1.0.0 13 Nov 2026).

## Sources
| File | Built from | Date of source | Notes |
|---|---|---|---|
| 20-27 | IA "Solvency and Capital Template 2026" SCA.04, as restated in the owner's `KSA_RBC_Rules_vSCA04.md` | Template issued 25 Feb 2026 (YE2025, 5th dry run); specification 13 Nov 2026 | Sections 1-17 and Appendices A, B of the specification, unchanged in substance. Worked examples recomputed 13 Nov 2026: all match |
| 28 K1-K5 | Owner's "GCC Solvency Master File: KSA, Qatar (QFC) and UAE" | 12 Nov 2026 | Laws and IA circulars as summarised there, with corrections from the SCA.04 review (premium exposure, counterparty base, own-funds tiering, life-and-health catastrophe exposure) |
| 28 K6 | Specification Appendix C | 13 Nov 2026 | The template's own comparison with Solvency II |
| 20-28 (SCA.07 update) | IA "Solvency and Capital Template 2026" SCA.07, workbook `Solvency_and_Capital_Template_2026Q3_vSCA.07.xlsx` (Version sheet rows 171-194) | Issued 16 Nov 2026; valuation 30 Sep 2026 | Every factor table, the 10 main correlation matrices, scenario parameters, op risk and aggregation formulas re-read on 20 Nov 2026: unchanged from SCA.04 except the items under SCA.05-SCA.07 below |
| 30 | IA "RBC Own Funds and Solvency Assessment Template" Q3 2026, workbook `RBC_Own_Funds_and_Solvency_Assessment_Template_Q3_2026.xlsx` | Q3 2026 edition (columns Q3 2026, YE 2025) | Full read; recalculated in LibreOffice with the worked example (all cells match) |

The workbooks themselves are not part of this skill. A parameter not in files 20-27 or 30 is not defined in the templates: say so rather than estimate it.

## Open points (VERIFY)
1. **Final RBC regulation for 1 Jan 2027:** minimum RBC ratio and intervention ladder (neither template defines them). The Own Funds template now gives MCR = RBC / 3 with SR 10-40m floor checks; whether that MCR is a hard intervention point is not stated. Replace every [DRY RUN] value when the final rules are published, and retire file 28 section K2.
2. **Own Funds:** the template (file 30) gives the tier limits and the adjustments but no criteria for classifying an item as Tier 1, 2 or 3 (subordinated debt, letters of credit, uncalled capital), no approval process for ancillary own funds, and no sign rule for deferred tax. Intangibles are both deducted and charged at 80% (file 27 behaviour 25): raise with the IA.
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
- **SCA.05 (13 Jul 2026):** valuation date moved from year-end to quarter-end (Q1 2026 first): exposure definitions and SOFP / SOI / Regulatory Solvency / Projected RBC columns gain the current quarter; LOB allocation actuals = past 12 months; symmetric adjustment on 2026Q1 data; **windstorm recoveries added to TotalRME**; **Net RA and Net CSM removed from Projected RBC** (now inside eligible own funds); duplicate and dropdown validations on Market and Counterparty Default; concentration asset-base check excludes plant and equipment; Q2 / Q4 projections need a full forecast, Q1 / Q3 best efforts.
- **SCA.06 (23 Aug 2026):** symmetric adjustment on 2026Q2 data; fund table gains treatment type and risk module per fund; region-vs-total reconciliation for premium and reserve risk; `Comments & Assumptions` tab for all assumptions and expert judgements; clarifications from the 29 Jul 2026 AAs and HAFs meeting: multiple agency ratings (lower of two; lower of the best two of three or more), fund table at underlying-asset level, accrued interest inside the asset value, REITs as property, non-traditional assets by nature, statutory deposits under counterparty default.
- **SCA.07 (16 Nov 2026; valuation 30 Sep 2026):** symmetric adjustment on 2026Q3 data (TASI 26.95%, Nomu 27.38%, OECD 46.71%); **EOSB added to interest-rate scope** as a discounted liability; prompts in `Comments & Assumptions`; **new `Reinsurance Impact` sheet** (gross minus net standard formula by module and overall RBC; file 27 section 12A).
- **Own Funds and Solvency Assessment Template (Q3 2026):** eligible own funds by tier with Solvency II-style limits, regulatory adjustments (net RA and CSM added; own shares, goodwill, foreseeable dividends, intangibles, deferred tax deducted), MCR = RBC / 3 with floor checks (file 30).

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

**RBC and ratio.** RBC = 362,736.9333 + 5,248 = **367,984.9333**. Eligible own funds 625,000 (Tier 1 600,000 with no deductions, + net RA 20,000 + net CSM 5,000 as Own Funds template adjustments) → ratio = 625,000 / 367,984.93 = **169.84%**. MCR = 122,661.6; Tier 1 ≥ 50% RBC and ≥ 80% MCR: PASS.

**Own funds and tiers.** See file 30 section 30.7 (RBC 300,000: eligible own funds 537,000, ratio 179%; T3 capped at 45,000, T2 at 105,000).

## Load-test questions (expected answer in brackets)
- **T1.** What is the RBC premium-risk factor for medical, and for one-year group life?
  - [Medical LOB9: 13% premium, 15% reserve (direct and proportional). Group life LOB11: 43% / 24%, in the non-life module, not life. Must tag [DRY RUN]. File 24.]
- **T2.** What is the premium-risk exposure for a line?
  - [max(NEP last 12 months, expected NEP next 12 months + loss component) + future premium on existing and new long-term contracts; non-proportional inwards separately at 51%; then geographical diversification 0.75 + 0.25 x Herfindahl over 7 regions. File 24.]
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
  - [Not defined in SCA.07 or the Own Funds template; no ladder either. Do not invent one. The Own Funds template does define MCR = RBC / 3 with floor checks and tier limits. File 20 section 11; file 30; file 29 open point 1.]
- **T10.** Tier 1 200,000, Tier 2 (subordinated loan) 120,000, no Tier 3, RBC 200,000, net RA 10,000, goodwill 5,000. Eligible own funds and ratio?
  - [Eligible T2 = min(120,000, 50% × 200,000) = 100,000; before adjustments 300,000; adjustments +5,000; eligible 305,000; ratio 152.5%. Checks: T1 ≥ 100,000 PASS; T2+T3 check shows FAIL because the 50% cap binds (template behaviour, not a breach). MCR 66,667: T2 for MCR = 13,333; MCR T2 check FAIL for the same reason. File 30.]
- **T11.** Does a reinsurer's rating of A from one agency and BBB from another change its Type 1 factor?
  - [Use the lower: BBB, still 5%. With A / BB the lower rating BB moves it to 50%. With three ratings use the lower of the best two. File 20 section 1; file 22.]
