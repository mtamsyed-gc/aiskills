# Core: risk-transfer tests worked on a stylised book

Use with `01-core-solvency-method.md` section 4 when a structure has loss-sensitive terms (corridor, cap, sliding scale, swing rate, aggregate limit) or when someone quotes ERD or 10-10 without saying on what volatility.

### C9 Risk-transfer tests: worked cases
Source: metric definitions and test selector of the Structured Solutions Lab and Treaty Structure Metrics tools, applied 12 Nov 2026 to a stylised book. Illustrative only: not a client, not a regulatory number. Use it to see how each test reacts to a feature, then run the real case in the Treaty Structure Metrics kit.

**Set-up.** Per 100 of subject premium. Gross loss ratio lognormal with mean 90%, at two volatilities:
- sd 3 points: process risk only, i.e. a large stable medical book with next year's mean treated as known. 1-in-200 LR 98.0%.
- sd 10 points: with a year-wide swing (pricing, medical inflation, mix move the whole book). 1-in-200 LR 118.8%.

200,000 simulated years. QS share 50%. Brokerage 2.5% on a QS, 10% on aggregate covers. Resident panel, so no WHT (a non-resident panel takes 5 more points: skill `reinsurance-pricing-knowledge`, Part F). In each case one term is solved so that reinsurers expect a 3% margin on premium.

**Measures.** RI result = premium - brokerage - WHT - recoveries - commission.
- ERD = E[max(-RI result, 0)] / E[premium]. Pass at 1% or more.
- 10-10: pass if the chance of the reinsurer losing 10% of premium or more is at least 10%.
- T1 = RI result at its own 1-in-200, as % of premium.
- T2 = mean RI result in the cedant's worst 0.5% of gross years, as % of premium.
- T3 = improvement in the cedant's 1-in-200 result from the structure, after its cost, in points of subject premium. Negative = the structure makes the cedant's tail worse.

**With the year-wide swing (sd 10 points)**
| Structure (solved term) | P(RI loss) | ERD | 10-10 | T1 | T2 | T3 |
|---|---|---|---|---|---|---|
| 1 Plain QS (flat commission 4.5%) | 36% | 2.7% pass | 10.2% pass | -26% | -30% | +11.7 |
| 2 QS capped at 105% LR (commission 4.9%) | 38% | 2.5% pass | 10.8% pass | -12% | -12% | +5.0 |
| 3 QS, corridor 95-110% kept by cedant (commission 6.4%) | 43% | 1.6% pass | 0.9% fail | -13% | -17% | +5.1 |
| 4 QS, sliding commission 10.7% at LR 80% or below to 0% at 95% or above | 22% | 1.4% pass | 4.8% fail | -21% | -26% | +9.4 |
| 5 Margin-locked QS (3% margin at 95%: band 74.6-107.3%) | 2.9% | 0.14% fail | 0.4% fail | -9% | -13% | +3.0 |
| 6 Aggregate QS, 50% of unlimited xs 105% LR (premium 0.23) | 6.8% | 81% pass | 6.8% fail | about -30x | about -39x | +6.7 |
| 7 Stop loss 20 points xs 105% LR (premium 0.45) | 6.8% | 81% pass | 6.8% fail | about -30x | about -37x | +13.4 |

**Process risk only (sd 3 points)**
| Structure (solved term) | P(RI loss) | ERD | 10-10 | T1 | T3 |
|---|---|---|---|---|---|
| 1 Plain QS (flat commission 4.5%) | 16% | 0.26% fail | 0% fail | -5.0% | +1.2 |
| 3 QS, corridor 95-110% (commission 4.6%) | 16% | 0.21% fail | 0% fail | -2.1% | -0.2 |
| 4 QS, sliding commission 13.3% to 0% | 0.8% | 0.01% fail | 0% fail | -0.5% | -1.0 |
| 5 Margin-locked QS (band 85.2-95.0%) | 0.5% | 0.01% fail | 0% fail | 0.0% | -1.3 |

The 105% cap never bites at this volatility (1-in-200 LR is 98%), and covers attaching at 105% have no measurable expected loss.

**What the cases show**
1. **The volatility basis decides the answer.** The same break-even QS has ERD 0.26% without parameter risk and 2.7% with it. Always state the basis: process risk only, or with a year-wide swing and large-claim clustering. A test result quoted without it means little.
2. **A plain QS on a stable book fails strict ERD and 10-10.** That is why the usual reading treats a plain proportional QS as transferring risk pro rata (a switch in the tools). Say which reading was applied; the exemption does not extend to a QS with loss-sensitive terms.
3. **Every loss-sensitive feature takes risk back.** The corridor and the sliding scale buy a higher commission (6.4% and up to 10.7% against 4.5%) and roughly halve the ERD; both fail 10-10 here while still passing ERD.
4. **A cap hides from ERD and 10-10.** Capping at 105% leaves ERD at 2.5% and 10-10 passing, but halves the reinsurer's tail loss (T1 -12% against -26%) and cuts the cedant's 1-in-200 benefit from 11.7 to 5.0. Check T1, T2 and T3 whenever there is a cap or an aggregate limit.
5. **Margin-locked designs fail ERD at both volatilities** (0.14% and 0.01%): inside the band the reinsurer earns its margin whatever happens. Finite by construction (UAE Art 25, KSA Art 19).
6. **10-10 is the wrong screen for remote covers.** The stop loss and aggregate QS have ERD of 81% but lose money in only 6.8% of years, so they fail 10-10. Use ERD or T3 for low-frequency, high-severity covers.
7. **T3 can be negative.** On the stable book the corridor, sliding-scale and margin-locked QS leave the cedant's own 1-in-200 result worse than no reinsurance, because the expected cost exceeds the tail benefit. A structure can earn credit in a volume formula and still weaken the cedant economically.
8. **Expected cost is the same, 2.75, for every QS variant at break-even** (50% x (3 margin + 2.5 brokerage)). The features move who carries the volatility, not the expected cost.
9. **Aggregate covers look cheap only at expected-loss pricing.** Here 0.45 buys a 13.4-point cut at the 1-in-200. Reinsurers price remote layers on capital, so real quotes can be several times that (C7).

**Running a real case**
1. Build the cedant's loss-ratio distribution from its claims ladder (skill `reinsurance-pricing-knowledge`, Part D) in the Treaty Structure Metrics kit; record the uncertainty settings.
2. Evaluate the treaty terms year by year, with the actual brokerage, WHT by reinsurer residency, commission, corridor, cap, profit commission and funds withheld.
3. Report margin, P(RI loss), ERD, 10-10, T1, T2 and T3 together, with the test the regulator's text supports named, and the cedant and reinsurer results side by side.
4. A structure that fails the chosen test gets no capital credit in the comparison.
