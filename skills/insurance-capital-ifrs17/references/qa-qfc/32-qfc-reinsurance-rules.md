# Qatar (QFC): reinsurance rules, capital credit by structure, and structured-solution screening

**Sources:**
- **[RULE]:** PINS V20, chiefly Schedule 3, 4.4-4.6, 5.5.6, 8.4.5-8.4.6, Ch 10-11.
- **[TEMPLATE]:** INS340, INS610.x.

**Scope caveat.** PINS has **no dedicated reinsurance chapter** comparable to UAE Decision 23/2019. The following are **not in PINS**:
- a rating floor for reinsurers;
- a finite-reinsurance ban;
- a mandatory retention plan;
- a ceded-premium provision.

Reinsurance governance sits in risk-management requirements (Schedule 1 guidance, CTRL) and in the capital formula. **VERIFY** that no QFCRA notice or other module (GENE, CTRL, COND) adds cession rules before telling a client "there is no restriction".

## 1. What the rules do say about reinsurance [RULE]
| Rule | Content | Consequence |
|---|---|---|
| A3.2.1, Tables B/C | Reinsurance assets are charged **1-8% by grade** if the reinsurer is supervised by a subrule (2) regulator, and **1.2-9.6%** (+20%) if not | Domicile and supervision of each panel member change the capital cost. Get each reinsurer's rating, regulator and IAIS MMoU status |
| A3.1.1(3), A3.1.2 | Unrated reinsurer = grade 4 (6% / 7.2%). Where ratings differ, use the worst-charge rating | Unrated retakaful or regional capacity costs 6-7.2% of the recoverable |
| A3.2.2 | Collateral in cash or grade 1-3 debt, or an unconditional guarantee from an unrelated grade 1-3 guarantor, substitutes that charge for the covered part | **Funds withheld, trust or collateral accounts and parental guarantees cut the counterparty charge** |
| A3.7.2(2), A3.8.2(2), A3.10.3 | Premium risk, claims risk and MER are measured **net of expected reinsurance recoveries** | Outward cover earns linear credit, with no floor |
| A3.9.3 | Capital at risk is net of expected reinsurance recoveries | Risk-premium/YRT life cession reduces the 0.1% CAR and mortality charges |
| 3.7.1 | ORR is on gross premiums and gross provisions, but capped at 15/85 × (IRR + InsRR) | Cession reduces ORR only where the cap binds |
| 8.4.5 | A liability is not derecognised because reinsurance was bought, unless the obligation itself is discharged | Gross liabilities stay on the balance sheet. Novation or transfer (Ch 11) is different from reinsurance |
| 8.4.6 (takaful) | Reinsurance is valued only for risks on policies **in force** at the reference date. Provisions for future policies are ignored | No credit today for cover on business not yet written |
| 5.5.6 | No internal reinsurance between long-term funds, or between a long-term fund and the rest of the company | Internal capital-relief structures inside a life insurer are prohibited |
| 6.5.1 (takaful) | No loans from a takaful fund | Qard-type funding cannot flow out of the fund |
| Ch 10 (10.1.7-10.1.9) | Intra-group transactions must be inquired into by the governing body; the Authority may give directions | Captive or intra-group reinsurance is in scope |
| Ch 11 | Transfer of insurance business needs a scheme report and notices to policyholders | A legal portfolio transfer (not an LPT reinsurance) is a scheme |
| A3.10.2(1) RP | Inward reinstatement premiums count only with a **binding netting arrangement** with the cedant | Relevant to inward cat reinsurance written in the QFC |

[TEMPLATE] INS340 asks for the 10 largest reinsurers by receivable, including:
- domicile, rating grade, premium ceded and collateral held;
- aged receivables and amounts written off;
- treaty policy limits and net retention by line of business, with the two largest reinsurers.

INS300 splits premium into direct, fac proportional, fac non-proportional, treaty proportional and treaty non-proportional.

## 2. Capital credit by structure [RULE + INTERP]
| Structure | InsRR | IRR | ORR | Eligible capital | Watch |
|---|---|---|---|---|---|
| Medical or general QS | Premium and claims risk fall **in proportion to the cession** (net basis, no floor). MER falls if the QS applies to the event | + reinsurance asset × 1-9.6% | Unchanged unless the cap binds; then it falls with IRR + InsRR | Commission effects follow IFRS 17 (file 33) | If RBC is below QAR 24m, the QAR 36m floor binds and there is **no headroom gain** |
| Surplus / per-risk XoL | Small reduction in net claims and premium liabilities (expected recoveries only) | Small | Small | — | **Template fallback** (no cat cover): concentration = 2 × largest per-risk retention, so per-risk XoL retention matters directly |
| Cat XoL | **Concentration = MER + CoR − RP**: lower retention and prepaid reinstatements reduce it directly | Recoverables only post-event | Via cap | — | MER at ≥ 1-in-250; the actuary's advice is needed for complex books. Prepaying reinstatement removes CoR |
| Medical stop loss / aggregate XoL | Credit only to the extent of **expected** recoveries in net premium liability, which are usually small [INTERP] | — | — | — | Value lies in volatility and the ORSA view, plus a possible Authority SRR adjustment (3.3.2A guidance) |
| LPT / ADC on general reserves | Net outstanding claims fall by the **expected** recoveries | + recoverable × grade factor (collateral relief available) | Via cap | IFRS 17 day-1 effect (core file 00) flows to audited reserves | Not a transfer unless done as a Ch 11 scheme. Reserves stay gross (8.4.5) |
| Long-term QS / coinsurance | CAR charges fall (net). Provision charges (0.5-3%): net vs gross **VERIFY** | + reinsurance asset charge | Via cap | — | Internal fund-to-fund reinsurance is banned (5.5.6) |
| Risk premium / YRT life | CAR 0.1% + mortality 0.05% fall | Small | — | — | Low capital value: the factors are small |
| Fronting (≈100% ceded) | ≈ 0 | Full recoverable × grade factor | Gross basis ≥ 2% GWP, unless the cap binds (and with InsRR ≈ 0 the cap is low) | — | The QAR 36m MCR floor dominates. Concentration limit 8.1.6 excludes reinsurance receivables |
| Subordinated loan from a reinsurer or parent | — | — | — | **Lower tier 2**, if 4.4.2 terms are met (≥ 5 yrs, no step-up in the first 5 yrs, payment blocked in MCR breach); capped at 50% of tier 1 after deductions; legal opinion; 30-day notice | Amortises 20% a year in the last 4 yrs. Not eligible if secured |
| LoC / parental guarantee as capital | — | Can reduce asset risk as a guarantee (A3.2.2) | — | **Not eligible capital** (no ancillary tier) unless QFCRA recognises it | |
| Capital injection | — | Cash 0.5% | Via cap | Tier 1 | Tier 1 reductions later need approval (4.8.1) |

## 3. Screening checklist [INTERP]
1. **Entity and perimeter.** QFC LLC, branch or captive? QFC or onshore QCB (file 30 §1)?
   - Branches: the home regulator's rules decide the capital credit. PINS ORSA and Ch 3 do not apply.
2. **Binding test.**
   - Floor (RBC < QAR 24m) or SRR?
   - Is the ORR cap binding? If so, cession also cuts ORR.
3. **Counterparty cost.** For each panel member:
   - grade, using the worst-charge rating;
   - supervised-regulator status;
   - collateral or guarantee available.
   Price the A3.2.1 charge into the treaty economics.
4. **Risk transfer.** PINS has no finite ban text. Still run the core risk-transfer tests (core file 01 §4), because:
   - IFRS 17 measurement and the significant-risk test depend on substance;
   - the Authority can treat a structure as not reducing risk (3.3.3, 8.2.4 directions);
   - SRR setting takes risk management into account.
5. **Valuation.** Expected recoveries feed the capital charges directly. Make sure they are on the same basis as the gross liability (IFRS 17 for conventional insurers; Part 8.6 for takaful) and justified by the approved actuary.
6. **Group and related-party issues.** Intra-group reinsurance and loans raise:
   - Ch 10 inquiry duties;
   - connected lending of a capital nature (a deduction);
   - investment concentration (8.1.6 includes intra-group exposures).
7. **Notifications.** Material capital change → ORSA update and notification (2.4.3(2); GENE 4.1.3). Tier 2 changes → notices (4.4.2(1)(k), 4.8.3).
