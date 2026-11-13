# Core files 02-06: source register, open points and load tests

As at 13 Nov 2026 (skill v1.3.0). v1.3.0 removed all KSA content to the separate skill `ksa-rbc-capital`. Files 00 and 01 are unchanged from v1.0.1; the UAE and QFC layers keep their own registers (19, 39).

## Sources
| File | Built from | Date of source | Notes |
|---|---|---|---|
| 02 GCC cross-regime comparison | Owner's "GCC Solvency Master File: KSA, Qatar (QFC) and UAE" | 12 Nov 2026 | Condensed; UAE and QFC parts only. The KSA rows of the master file are in `ksa-rbc-capital` (file 28) |
| 03 Rating-agency capital | S&P "Insurer Risk-Based Capital Adequacy: Methodology And Assumptions"; AM Best "Best's Credit Rating Methodology"; Fitch white paper "Not All Insurer Financial Strength Ratings Are Created Equal" | 15 Nov 2023 (republished 22 Jan 2025); 29 Aug 2024; July 2016 | Capital and reinsurance passages read; not the full documents |
| 04 IFRS 17 worked numbers | Rules in file 00 (IFRS 17 as amended June 2020), applied to stylised figures | 12 Nov 2026 | Illustrative arithmetic; RA and discounting ignored |
| 05 Structures atlas | Owner's Reinsurance Structures Atlas (48 structures, 31 clauses) | Nov 2026 | Regulatory references inside entries are as at the UAE sources of files 02 and 12; KSA references point to `ksa-rbc-capital` |
| 06 Risk-transfer worked cases | Metric definitions of the owner's Structured Solutions Lab and Treaty Structure Metrics tools, on a stylised lognormal book | 12 Nov 2026 | 200,000 simulated years; one loss-ratio distribution, so no per-person XoL case |

## Open points (VERIFY)
1. **KSA:** all KSA open points are kept in `ksa-rbc-capital` (file 29).
2. **UAE:** whether eForms v1.7 is the version currently filed; units of the MGF minimum amounts.
3. **QFC:** category mapping and whether one-year group life is long-term business (the QFC layer's own register, file 39, has the full list).
4. **Rating agencies:** Moody's and Fitch insurance methodologies are not covered; AM Best's risk factors by line are in separate BCAR criteria; the AM Best country risk tier of each GCC state is not in the document read; check for later versions of all three before quoting a factor.
5. **File 04:** have the insurer's auditor confirm the reading before a number goes into advice. The split of a sliding-scale commission between premium and recoveries is this skill's reading of paragraph 86.
6. **File 06:** illustrative only. A real case needs the cedant's own claims ladder and uncertainty settings.

## Maintenance rule
- Files 02-06 mirror parts of the owner's Claude-side reference `reinsurance-capital-knowledge`. When that reference changes, regenerate the affected file, bump the skill version and add a line here. File 02 is generated from its Part A **without** the KSA-now and KSA-RBC columns and KSA bullets; KSA mentions elsewhere become pointers to `ksa-rbc-capital`.
- KSA lives in the separate skill `ksa-rbc-capital` (owner's decision, 13 Nov 2026), not as a `references/ksa/` overlay here.
- The companion skill `reinsurance-pricing-knowledge` cites this skill by section code (A5, A7, C4 grossbasis, C7, C8 c_inure). If a code is renumbered here, update it there.

## Load-test questions (expected answer in brackets)
- **T1.** A Saudi medical insurer: what is its RBC premium-risk factor?
  - [This skill has no KSA rules: must say so and ask for `/ksa-rbc-capital` (where the answer is 13% premium / 15% reserve, dry run). Must not answer from memory.]
- **T2.** Compare the reinsurer counterparty charge for an A-rated reinsurer in the UAE and QFC.
  - [UAE 0.025 per 100 on 50% of recoverables, 80% of collateral deducted; QFC 4.0 (recognised regulator) or 4.8. File 02, A5. Should add that KSA is in `ksa-rbc-capital`.]
- **T3.** Under S&P's model, what is charged on recoverables from an unrated reinsurer, and on EMEA medical premium?
  - [Unrated is treated as 'B': 7.48% at the 99.5% level, unless collateralised. Health and medical expense: 10% of net written premium at 99.5%. File 03.]
- **T4.** An insurer has BCAR of 12 at VaR 99.6. What is the BCAR assessment, and what does AM Best B+ equal on its issuer scale?
  - [Very strong (above 10 and not above 25 at 99.6). B+ = bbb-. File 03.]
- **T5.** A one-year medical book is onerous by 8 per 100 of premium. A 50% quota share is in force. What is the day-1 net effect?
  - [-8 on the underlying, +4 loss-recovery income, net -4; the 4 reverses over the cover. If the treaty was signed after the group was recognised: -8 on day 1, +4 later. File 04, case 2.]
- **T6.** Which structures relieve a premium-based test such as the UAE MGF?
  - [qs, corridorqs, capqs, slidingqs, marginlocked, capreliefqs; secondary corrsl, grossbasis. File 05, C0. Should add the finite-risk flags: capqs, marginlocked high.]
- **T7.** Does a break-even quota share on a stable medical book pass a 1% ERD test?
  - [Not on process risk alone: 0.26% in the stylised case, against 2.7% with a year-wide swing. The answer must state the volatility basis and the pro-rata reading for plain proportional cover. File 06.]
- **T8.** Does a medical stop loss reduce the S&P capital requirement?
  - [Not through the standard charges: only through lower net premium, or a company-specific adjustment S&P makes when material (about 5% of the requirement) and sustainable. File 03.]
- **T9.** A question about Oman's solvency rules.
  - [No layer loaded: answer from the core method (file 01), say so, list the local facts needed.]
