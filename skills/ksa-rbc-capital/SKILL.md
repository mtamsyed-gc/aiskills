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
