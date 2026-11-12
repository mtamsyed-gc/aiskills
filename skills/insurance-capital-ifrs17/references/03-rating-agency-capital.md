# Core: rating-agency capital view - S&P, AM Best, and rating comparability

Use when the cedant is rated or wants a rating, when a reinsurer's rating matters to credit or to a regulatory minimum, or when a structure's value depends on the agency's model and not the regulator's.

### A10 Rating-agency capital view (S&P, AM Best)
Sources, read 12 Nov 2026: S&P Global Ratings, "Insurer Risk-Based Capital Adequacy: Methodology And Assumptions" (15 Nov 2023, republished 22 Jan 2025); AM Best, "Best's Credit Rating Methodology" (29 Aug 2024); Fitch Ratings white paper "Not All Insurer Financial Strength Ratings Are Created Equal" (July 2016). Condensed: open the documents for the full tables. Not covered: Moody's and Fitch's own insurance methodologies; AM Best's separate BCAR criteria (risk factors by line); the S&P insurer rating methodology that turns the capital result into a score.

Why it belongs here: a rated cedant, or one seeking a rating, can be bound by the agency's capital model before the regulator's. Reinsurer ratings also set the regulatory minimums (file 02, A7) and counterparty charges (file 02, A5).

**S&P capital model**
- Compares total adjusted capital (TAC) with risk-based requirements at four one-year VaR levels: 99.5% (moderate stress), 99.8% (substantial), 99.95% (severe), 99.99% (extreme).
- TAC starts from common equity on IFRS or GAAP accounts (statutory where those are all there is): less intangibles, treasury shares and unaccrued dividends; adjusted for unrealised gains and for reserve surpluses or deficits against S&P's best-estimate view; plus hybrid and debt-funded capital within tolerance limits; less non-insurance and unconsolidated insurance subsidiaries.
- Requirement = sum of risk charges less explicit diversification (variance-covariance at three levels). The diversification amount is cut by 10 / 20 / 30% at the three higher stress levels. No credit for geographic spread.
- **Reinsurance is recognised by charging exposures net of reinsurance, with no floor** (contrast the UAE and KSA-now 50% floors).

| Item | Base | Charge |
|---|---|---|
| Premium risk, health and medical expense, EMEA risks | Net written premium (net unearned premium if higher) | 10% at 99.5%; 12 / 14 / 16.5% at the higher levels |
| Reserve risk, health and medical expense, EMEA risks | Adjusted net loss reserves | 10% at 99.5%; 12 / 14 / 16.5% |
| Other levels, premium and reserve risk generally | | 1.2x, 1.4x, 1.65x the 99.5% charge |
| Non-proportional reinsurance written (a reinsurer's inward book) | Same bases | 1.25x the premium and reserve charges |
| Reinsurer counterparty | Reinsurers' share of outstanding loss reserves, and reinsurance receivables | At 99.5%: AAA 0.28, AA 0.73, A 0.99, BBB 2.03, BB 4.84, B 7.48, CCC 35.18. At 99.99%: 0.52, 1.38, 1.89, 3.86, 9.19, 14.21, 58.0 |
| Unrated reinsurer | | Treated as 'B'; 'CCC' if payment looks vulnerable |
| Collateral | Letters of credit from a secure institution, reinsurance deposits, trust assets | Offsets the counterparty charge, up to 100% |
| Natural catastrophe | Net aggregate 1-in-200 loss at 99.5%, after reinsurance and cat bonds, with reinstatement premiums | Plus a contingent credit charge on the recoveries |
| Pandemic (life) | Net amount at risk | 0.058% at 99.5% to 0.084% at 99.99% |

- Per-person XoL, stop loss and other non-proportional covers outside natural catastrophe are not in the standard charges. They count through lower net premium and reserves, or through a company-specific adjustment, which S&P makes only when material (for example a change of more than 5% in the total requirement) and sustainable.
- Reading for structures [INTERP]:
  - A QS cuts the S&P requirement in line with the cession, at a counterparty cost of about 1-2% of ceded reserves for A to BBB reinsurers.
  - Unrated local capacity is charged as 'B' (7.48% at 99.5%) unless collateralised: milder than the KSA-RBC cliff (file 02, A5) but still several times an A-rated line.
  - A stop loss or corridor needs a case put to the analyst; it does not flow through the factors.

**AM Best**
- Building blocks, in order: balance sheet strength sets a baseline; then operating performance (+2 to -3 notches), business profile (+2 to -2), enterprise risk management (+1 to -3 or -4), a comprehensive adjustment (up to 1 notch either way), and lift or drag from the wider group (typically 1 to 4 notches).
- BCAR = (available capital - net required capital) / available capital x 100, run at VaR 95, 99, 99.5 and 99.6.

| BCAR | Assessment |
|---|---|
| Above 25 at 99.6 | Strongest |
| Above 10 at 99.6 | Very strong |
| Above 0 at 99.5 | Strong |
| Above 0 at 99 | Adequate |
| Above 0 at 95 | Weak |
| 0 or below at 95 | Very weak |

- BCAR is not tied directly to a rating; a stable BCAR over time is viewed better than a volatile one.
- The baseline comes from balance sheet strength and the country risk tier (CRT-1 least risk to CRT-5). In CRT-1 and CRT-2: Strongest a+/a, Very strong a/a-, Strong a-/bbb+, Adequate bbb+ to bbb-. CRT-3 to CRT-5 pull each row down, by about one notch per tier. The tier of each GCC country is not in this document: check AM Best's country risk reports.
- Reinsurance is judged beyond its effect on BCAR, on three points: quality of the reinsurers, appropriateness of the programme, and dependence.
  - Relying on reinsurance for losses at high return periods is viewed less favourably than holding capital for them; AM Best likens heavy dependence to short-term debt, exposed to price and availability.
  - Ceded probable maximum loss relative to surplus is the dependence measure; above an acceptable level the balance sheet assessment is lowered.
  - Concentration of recoverables in a few reinsurers is weighed qualitatively. The ERM review also covers counterparty, dispute, programme-design and collateral risk.
- Reading for structures [INTERP]: a large QS can lift BCAR and still draw a dependence mark-down. For an AM Best-rated cedant, present the cession with panel quality, spread and permanence (multi-year terms, long relationships), not as replacement capital.
- AM Best financial strength rating to its own issuer credit scale: A++ = aaa, aa+; A+ = aa, aa-; A = a+, a; A- = a-; B++ = bbb+, bbb; B+ = bbb-; B = bb+, bb; B- = bb-. So a rule that accepts "AM Best B+" (KSA: file 02, A7) accepts bbb- on AM Best's own scale.

**Are ratings equal across agencies? (Fitch white paper, July 2016)**
- Fitch's claim: an AM Best A- is most comparable with BBB from Fitch, Moody's or S&P. It points to newly formed companies, insurers in high-country-risk states, captives and small insurers.
- Its evidence: AM Best reports a 10-year cumulative impairment rate of 5-6% for A and A- combined (Fitch extrapolates about 7% for A- alone), against about 2% 10-year default for Fitch's own A-.
- Caveats: this is one agency's view of a competitor and is dated; impairment is a wider event than default, as Fitch itself says; AM Best's reply is not in the file.
- Use [INTERP]: do not treat the same letter from different agencies as the same security. Where a treaty, a security list or a regulation names a minimum rating, state which agency's rating each reinsurer on the panel holds.
