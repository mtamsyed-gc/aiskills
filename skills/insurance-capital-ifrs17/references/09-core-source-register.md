# Core files 02-06: source register, open points and load tests

As at 12 Nov 2026 (skill v1.2.0). Files 00 and 01 are unchanged from v1.0.1; the UAE and QFC layers keep their own registers (19, 39).

## Sources
| File | Built from | Date of source | Notes |
|---|---|---|---|
| 02 GCC cross-regime comparison | Owner's "GCC Solvency Master File: KSA, Qatar (QFC) and UAE" | 12 Nov 2026 | Condensed. KSA-RBC values are the YE2025 5th dry run of template SCA.04 and can still change before the regulation is final |
| 03 Rating-agency capital | S&P "Insurer Risk-Based Capital Adequacy: Methodology And Assumptions"; AM Best "Best's Credit Rating Methodology"; Fitch white paper "Not All Insurer Financial Strength Ratings Are Created Equal" | 15 Nov 2023 (republished 22 Jan 2025); 29 Aug 2024; July 2016 | Capital and reinsurance passages read; not the full documents |
| 04 IFRS 17 worked numbers | Rules in file 00 (IFRS 17 as amended June 2020), applied to stylised figures | 12 Nov 2026 | Illustrative arithmetic; RA and discounting ignored |
| 05 Structures atlas | Owner's Reinsurance Structures Atlas (48 structures, 31 clauses) | Nov 2026 | Regulatory references inside entries are as at the UAE and KSA sources of files 02 and 12 |
| 06 Risk-transfer worked cases | Metric definitions of the owner's Structured Solutions Lab and Treaty Structure Metrics tools, on a stylised lognormal book | 12 Nov 2026 | 200,000 simulated years; one loss-ratio distribution, so no per-person XoL case |

## Open points (VERIFY)
1. **KSA-RBC final rules:** own-funds tiering, minimum ratio, intervention ladder, minimum capital amount, treatment of stop loss. Replace every [DRY RUN] value when the final regulation is published; retire the KSA-now columns from 1 Jan 2027.
2. **KSA finite ban:** whether Art 19 of the 2010 Reinsurance Regulation carries into the 2027 regulations.
3. **KSA cooperative surplus split** (Implementing Regulations Art 70).
4. **UAE:** whether eForms v1.7 is the version currently filed; units of the MGF minimum amounts.
5. **QFC:** category mapping and whether one-year group life is long-term business (the QFC layer's own register, file 39, has the full list).
6. **Rating agencies:** Moody's and Fitch insurance methodologies are not covered; AM Best's risk factors by line are in separate BCAR criteria; the AM Best country risk tier of each GCC state is not in the document read; check for later versions of all three before quoting a factor.
7. **File 04:** have the insurer's auditor confirm the reading before a number goes into advice. The split of a sliding-scale commission between premium and recoveries is this skill's reading of paragraph 86.
8. **File 06:** illustrative only. A real case needs the cedant's own claims ladder and uncertainty settings.

## Maintenance rule
- Files 02-06 mirror parts of the owner's Claude-side reference `reinsurance-capital-knowledge`. When that reference changes, regenerate the affected file, bump the skill version and add a line here.
- A full KSA overlay (`references/ksa/`, files 20-29, built from the primary texts on the overlay template) supersedes the KSA content of file 02 when it is added.
- The companion skill `reinsurance-pricing-knowledge` cites this skill by section code (A5, A7, C4 grossbasis, C7, C8 c_inure). If a code is renumbered here, update it there.

## Load-test questions (expected answer in brackets)
- **T1.** A Saudi medical insurer under today's rules: above what net loss ratio does the claims margin bind?
  - [About 67%: premium margin 16% of net written premium against 24% of three-year average net incurred claims. File 02, A0.]
- **T2.** It cedes 70% of medical. How much credit today, and under the 2027 RBC?
  - [Today: credit stops at the 50% net floor; cession cannot exceed 70% of total premium (Art 40). Under KSA-RBC: full credit, no floor, less a counterparty charge. Illustration: 7.9 per 100 GWP at 70% ceded under RBC against 9.6 today. Must say file 02 is condensed and RBC values are dry-run.]
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
