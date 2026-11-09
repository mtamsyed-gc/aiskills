# Core: how to read any solvency regime and test a capital lever (jurisdiction-neutral)

Tag: method and [INTERP] unless a country file supplies the [RULE].

## 1. Ten-point anatomy: fill this in for any regime before answering
1. **Liability basis.** How technical provisions are valued for solvency: prudent, best estimate, or best estimate plus margin; discounted or not; floors such as no negative reserves; treatment of unit-linked business.
2. **Asset basis.** Valuation and admissibility: limits by asset class and counterparty, haircuts, aged receivables, related parties, intangibles, deferred acquisition costs (DAC), real estate.
3. **Capital tiers.** What counts, in which tier, and the limits on each tier against each requirement. Examples: paid-in equity, retained earnings, subordinated debt, letters of credit, uncalled capital.
4. **Requirement layers.**
   - An absolute minimum: a fixed amount or the minimum paid-up capital.
   - A volume or factor minimum: premium- or claims-based, Solvency I style.
   - A risk-based requirement: modular, VaR- or factor-based.
   - Which layer applies (usually the highest), and which tier must cover it.
5. **Aggregation.** Correlation matrices, diversification credit, operational-risk add-ons and caps.
6. **Reinsurance credit.**
   - Is the requirement computed on gross or net figures?
   - Are there floors or caps on the net/gross ratio?
   - Is non-proportional cover recognised?
   - Counterparty charge and collateral credit; reinsurer rating and licensing rules.
7. **Risk-transfer and prohibited structures.** Finite bans, risk-transfer tests, approvals needed for portfolio transfers.
8. **Intervention ladder.** Triggers, notification duty, recovery-plan deadlines, sanctions (new-business bans, dividend stops, management removal).
9. **Reporting.** Frequency, certification (actuary, auditor), public disclosure of the ratio, lag allowed.
10. **Accounting link.** Is the regulatory balance sheet built from IFRS 17 or from a separate statutory basis? Is there a mandated reconciliation?

## 2. Binding-constraint analysis (do this first)
For each requirement R(i), compute:
- **cover(i)** = eligible own funds for R(i) ÷ R(i);
- **headroom(i)** = eligible own funds − R(i).

"Eligible" applies the tier limits for that requirement. Example: ancillary items may count for the risk-based requirement but not for the absolute minimum.

The binding test is the one with the lowest headroom. Then map levers to tests:

| Lever | Raises own funds | Cuts risk-based requirement | Cuts premium/volume minimum | Helps fixed minimum |
|---|---|---|---|---|
| New equity, retained profit | Yes (top tier) | — | — | **Yes** |
| Subordinated debt / approved hybrids | Yes, if eligible and approved | — | — | Usually not, or limited |
| Letter of credit / uncalled capital (ancillary) | Yes, haircut and approval | — | — | **No** (typically) |
| Quota share (proportional) | Small: commission, reserve release, cost | Yes, down to any net/gross floor; reduces cat and counterparty-adjusted net | **Yes**, if the minimum is on net premium | No |
| XoL / stop loss | — | Little or nothing under factor formulas on premium; yes under internal models or cat modules | No | No |
| LPT / ADC on reserves | Release of prudence margin less price | Reserve risk on the net (subject to floors) | Sometimes | No |
| Life coinsurance (vs risk premium/YRT) | Reserve credit on the ceded share; can fund new-business strain | Life shocks on net provisions | Sum-at-risk-based minimum | No |
| De-risking assets (equity, property, concentration) | Admissibility gain | Market and concentration risk | — | Only via admissibility gains |
| Receivables clean-up, settlement terms | Admissibility gain | Counterparty/receivables charge | — | Via admissibility |
| Dividend restraint | Retains own funds | — | — | Yes |

Rule of thumb: **reinsurance relieves requirements, not the minimum capital floor.** If the fixed minimum binds, the answer is capital or assets, not cession.

## 3. Factor formulas with net/gross floors: the most common trap
Generic form: capital = volume (gross) × max(net/gross, floor) × factor.
- Below the floor, more cession earns nothing. Example: with a 50% floor, ceding 70% gives the same charge as ceding 50%.
- **Non-proportional cover** barely moves net premium. It earns little or no credit in a premium-based factor formula, even when it removes most of the tail. Its value is earnings stability, rating-agency view and capacity, not regulatory capital.
- **Volume minimums on net premium** (Solvency I-style) often have **no floor**. Cession beyond the risk-based floor can still reduce the volume minimum. Check which one binds before sizing a treaty.

## 4. Risk transfer: evidence a reinsurer and a regulator will accept
- **Tests used in practice [INTERP]:**
  - **10-10.** There is at least a 10% probability that the reinsurer loses at least 10% of premium.
  - **ERD.** Expected reinsurer deficit = E[max(loss − premium, 0)] ÷ premium, usually at least 1%.
  - **Short-tail substitute.** Where 10-10 is unsuitable, use substantially all risk transferred.
- **Principles worth borrowing** from EU Solvency II Delegated Regulation 2015/35, Arts 208-215, on risk-mitigation recognition:
  - genuine, effective transfer of risk;
  - no material basis risk;
  - legal certainty and enforceability;
  - no clauses that undermine the transfer, such as guaranteed repayment, loss caps that remove tail, or experience accounts that return all losses.
- **Red flags for "finite / lender-borrower" readings:**
  - repayment of an upfront commission guaranteed from future profits;
  - funds withheld with guaranteed return of principal;
  - aggregate limits or corridors so tight that the reinsurer cannot lose;
  - commutation terms that refund the reinsurer's losses.
- **Document it:** write a risk-transfer memo with scenario results, cash-flow timing, contract features and the conclusion. The same memo supports the IFRS 17 significant-insurance-risk conclusion.

## 5. Three ledgers: always show all three for any action
| Ledger | Question | Typical divergence |
|---|---|---|
| Regulatory capital | Does cover improve on the binding test, and by how much per unit of cost? | Statutory day-1 gains (reserve releases, commission) |
| IFRS 17 earnings/equity | Day-1 effect, run-off pattern, presentation | Gains deferred in the CSM, commissions spread, past-event costs expensed |
| Cash and liquidity | Premium out, commission in, funds withheld, collateral | LPT pays reserves away; ADC pays only the premium |

**Efficiency metric:** capital headroom gained on the binding test ÷ expected economic cost (margin given to the reinsurer, plus fees, plus the cost of any regulatory provision). Compare levers on this metric.

## 6. Inputs checklist for a proper rebuild (request these)
- **Regulatory return** (or its parts): own funds build-up, requirement by module, admissibility schedule.
- **Premium:** written and earned, by line, gross and ceded.
- **Technical provisions:** by line, gross and net, on the regulatory basis.
- **Receivables aging:** direct, broker and reinsurance.
- **Investment schedule:** asset class, rating, issuer, listed or unlisted, domicile.
- **Reinsurance programme:** treaty type, retention, commission terms, reinsurer ratings, collateral, settlement terms.
- **Life:** sum at risk, mathematical reserves gross and net, products, reinsurance basis (risk premium/YRT vs coinsurance).
- **IFRS 17 notes:** LRC/LIC reconciliations, RA level, CSM run-off, onerous groups, transition method.
- **Plans:** growth, dividends, capital actions.

## 7. Standard workflows
**A. Capital read of an insurer**
1. Position (requirements, eligible own funds, cover, binding).
2. Drivers by module.
3. Bridge from IFRS equity to own funds.
4. Trend and sensitivity.
5. Levers ranked by efficiency, each with what it cannot do.
6. Data gaps.

**B. Structure assessment**
1. Describe the mechanism and its cash flows.
2. Legality and approval screen.
3. Regulatory capital effect, module by module and on the minimums.
4. IFRS 17 effect (day 1, run-off, presentation).
5. Cash.
6. Risk-transfer evidence.
7. Reinsurer economics: margin vs tail capital.
8. Verdict, conditions and pre-clearance list.

**C. Explaining a rule to a client or board**
1. Rule, with its citation.
2. What it means for this company, with numbers.
3. Decision options.
4. Open points.
