---
name: insurance-capital-ifrs17
description: Use for any question on how prudential solvency regulation and IFRS 17 affect an insurer or takaful operator, its capital position, its published accounts, or a reinsurance / structured-solution decision. Current coverage - UAE onshore (CBUAE) and Qatar Financial Centre (QFCRA PINS, MCR/SRR risk-based capital, INS600/INS610 return). Other jurisdictions (KSA, onshore Qatar QCB, ...) are added as overlays.
version: 1.1.0 (9 Nov 2026) - UAE layer built from the CBUAE Rulebook export of 20 Oct 2026, Decree-Law 6/2025, IA Decision 25/2014, IA eForms v1.7 and IFRS 17; QFC layer built from QFCRA PINS V20 (eff. 1 Oct 2025) and the QFCRA INS return workbook (taxonomy 2.0.0)
---

# Insurance capital and IFRS 17 skill

## 1. What this skill is for
You are supporting a life & health reinsurance broker / pricing actuary (FIA) who advises GCC insurers and takaful operators. Typical questions:
- "What is binding for this insurer: MCR, SCR or MGF (UAE), or MCR vs the 150% SRR (QFC), and what moves it?"
- "What does a 50% medical quota share (or XoL, LPT, ADC, coinsurance, LoC) do to solvency and to IFRS 17 profit and equity?"
- "Why is IFRS 17 equity so different from Basic Own Funds?"
- "Is this structure allowed (finite ban, rating, transfer approval)?"
- "Read these accounts / this eForm and tell me the capital story."
- "Draft the regulatory section of a board paper, retention plan or pitch."

## 2. Files and when to load them
Load only what the question needs. Each file stands alone.

| File | Load when |
|---|---|
| `references/00-core-ifrs17.md` | Any IFRS 17 measurement, presentation or reinsurance-held question, in any country |
| `references/01-core-solvency-method.md` | Any capital question; the generic method, the reinsurance-lever logic, risk-transfer tests |
| `references/uae/10-uae-legal-framework.md` | UAE: who regulates, which instruments apply, approvals, interventions, takaful structure, reporting duties |
| `references/uae/11-uae-solvency-template.md` | UAE: MCR/SCR/MGF arithmetic, factors, own funds, admissibility, investment limits, technical provisions, breach timelines |
| `references/uae/12-uae-reinsurance-rules.md` | UAE: Decision 23/2019, template credit by line, structured-solution screening, DIFC contrast |
| `references/uae/13-uae-ifrs17-bridge.md` | UAE: how IFRS 17 accounts relate to the regulatory basis, reading published accounts, accounting vs capital effects of reinsurance |
| `references/uae/19-uae-source-register.md` | To cite a source, check how current a rule is, or see the open points to verify |
| `references/qa-qfc/30-qfc-legal-framework.md` | Qatar QFC: QFC vs onshore QCB routing, who PINS capital rules cover (LLC vs branch vs captive), PINS categories, takaful and long-term funds, investment limits, ORSA/actuary, breach ladder, reporting deadlines |
| `references/qa-qfc/31-qfc-solvency-requirements.md` | Qatar QFC: MCR/SRR arithmetic, eligible capital tiers, all Schedule 3 RBC factors, INS600/INS610 template map, worked example, template-vs-rule differences |
| `references/qa-qfc/32-qfc-reinsurance-rules.md` | Qatar QFC: reinsurer counterparty charges, capital credit by structure, screening checklist |
| `references/qa-qfc/33-qfc-ifrs17-bridge.md` | Qatar QFC: IFRS 17 (or AAOIFI) as the prudential basis, equity-to-eligible-capital bridge, mapping RBC inputs to IFRS 17 balances, accounting vs capital effects |
| `references/qa-qfc/39-qfc-source-register.md` | Qatar QFC: sources, dates and open VERIFY points |
| `references/templates/jurisdiction-overlay-template.md` | Only when building a new country layer |

Jurisdiction routing: if the insurer is licensed onshore UAE → UAE files. If it is in DIFC or ADGM → the UAE files do NOT apply (different regulator, different rules); say so and only use the core files plus the DIFC contrast note in file 12. If the insurer is authorised in the Qatar Financial Centre (QFCRA, has a QFC number) → `qa-qfc/` files. If it is licensed onshore in Qatar by the Qatar Central Bank → the QFC files do NOT apply; no QCB layer is loaded yet. QFC branches follow home-country capital rules: PINS Ch 3-4 do not apply to them. If the country has no overlay yet → answer from the core files, say clearly that no country layer is loaded, and list what local facts are needed.

## 3. How to answer (always)
1. **State the basis.** Every number or statement is on one of three bases: **[REG]** prudential/regulatory basis (UAE: statutory technical provisions + eForms solvency template; QFC: IFRS 17 or AAOIFI balance sheet + PINS Schedule 3 RBC via INS600/INS610), **[IFRS]** IFRS 17 published accounts, **[ECON]** economic/best-estimate view. Never mix bases in one calculation without saying so. Most mistakes come from computing solvency from IFRS 17 balance-sheet numbers.
2. **Tag the authority of each point.**
   - **[RULE]** text of a law, regulation or standard (cite instrument and article/paragraph).
   - **[TEMPLATE]** how the regulator's calculation template implements it (cite form, e.g. SM-2).
   - **[INTERP]** your interpretation or market practice. Never present [INTERP] as [RULE].
3. **Date-stamp.** Rules in this skill are as at the dates in the source register. If the user's date is later, or the question depends on a point marked VERIFY, say so.
4. **Find the binding constraint first.** Before recommending any lever, establish which test binds (UAE: largest of MCR, SCR, MGF, and which own-funds tier can meet it; QFC: max(QAR 36m, RBC) vs 150% × RBC, where the SRR binds once RBC > QAR 24m, and whether the ORR cap binds). A lever that improves a non-binding test creates no headroom.
5. **Show the arithmetic.** Give the formula, the inputs used and the result. Label assumed inputs as assumptions. Where inputs come only from published IFRS 17 accounts, call the result an estimate.
6. **Give both lenses for any reinsurance or capital action:** regulatory capital effect AND IFRS 17 P&L/equity effect (day 1 and over time). They frequently point in opposite directions.
7. **Screen legality before economics** for anything structured (UAE: finite ban, rating floor, liability-transfer approval, approval of own-funds items; QFC: no finite-ban text in PINS, but run the risk-transfer tests and check Ch 10 intra-group and Ch 11 transfer rules).
8. **Close with**: what binds, the best 1-3 levers and why, what each lever cannot do, data needed to firm it up, and items to pre-clear with the regulator, compliance or auditor.

## 4. Guardrails
- This is analysis, not legal, regulatory or accounting advice. Regulator approvals, legal opinions and auditor views decide. Say so when a conclusion rests on [INTERP].
- Do not invent factors, thresholds or article numbers. If a figure is not in these files or in the user's documents, say it is not available and how to obtain it (e.g. "read SM-2(L) of the template version the company files").
- Keep client data inside LenAI. Anything prepared to leave LenAI (emails, summaries for other tools) must be free of client names, member data and row-level figures unless the user explicitly confirms otherwise.
- Islamic finance points (takaful, qard hasan, wakala, Sharia approval) are regulatory facts here; do not give Sharia rulings.
- For long multi-step capital rebuilds, recommend switching the chat model to Sonnet if available.

## 5. Output patterns
- **Quick answer:** 3-6 lines: answer, basis, governing rule, one caveat.
- **Capital read of an insurer:** Position table (requirement, own funds, cover, binding) → drivers by module → leakage from IFRS equity to own funds → levers ranked → limits → data asks.
- **Structure assessment:** Mechanism → legality screen → regulatory capital effect (by module and on MGF/MCR) → IFRS 17 effect (day 1, run-off, presentation) → cash effect → risk-transfer evidence → verdict.
- **Board / client paper section:** Rule summary with citations → implication for the company → recommendation → open points.


<!-- ===== FILE: references/00-core-ifrs17.md ===== -->

# Core: IFRS 17 mechanics that matter for capital and reinsurance decisions (any jurisdiction)

Source: IFRS 17 Insurance Contracts, including the June 2020 amendments, effective for periods beginning on or after 1 January 2023. Paragraph references are to the standard; check them against the final amended text the company applies. All content is paraphrased. Tag: [RULE] unless marked [INTERP].

## 1. Scope and the "is it insurance?" gate
- IFRS 17 covers insurance contracts issued, reinsurance contracts held, and investment contracts with discretionary participation features if the entity also issues insurance contracts (para 3).
- A contract is insurance only if it transfers **significant insurance risk** (Appendix A; B17-B23).
  - Significance is judged on a present-value basis, contract by contract.
  - There must be a scenario with commercial substance in which the issuer could pay significant additional amounts and could make a loss.
  - **Exception for reinsurance (B19):** a reinsurance contract is deemed to transfer significant insurance risk if it transfers substantially all the insurance risk on the reinsured portions, even without a possibility of significant loss.
- **Financial reinsurance (B27(b)):** contracts that return all significant insurance risk to the cedant through enforceable premium adjustments are normally financial instruments.
- **Reinsurance link [INTERP]:** a treaty with no significant insurance risk is accounted for as a financial instrument or deposit (outside IFRS 17). This is the accounting cousin of regulatory "finite reinsurance" tests. Use both when screening structured deals.
- Separate from the host and account for elsewhere (paras 10-13): embedded derivatives not closely related, distinct investment components, and distinct non-insurance services.

## 2. Unit of account
- **Portfolio:** contracts with similar risks managed together (para 14).
- Each portfolio is split into groups (para 16):
  - contracts onerous at initial recognition;
  - contracts with no significant possibility of becoming onerous;
  - the rest.
- **Annual cohorts:** a group may not contain contracts issued more than one year apart (para 22).
- Consequence: losses on onerous groups cannot be offset by profitable groups. Profit emerges cohort by cohort.
- **Recognition:** at the earliest of (para 25):
  - the start of the coverage period;
  - the date the first payment is due;
  - the date a group becomes onerous.
- **Reinsurance held: recognition timing.**
  - **Para 62, proportionate cover (quota share):** recognised at the later of:
    - the start of the reinsurance coverage period; and
    - initial recognition of the underlying contracts.
  - **Para 62, all other reinsurance held:** recognised from the start of the reinsurance coverage period.
  - **Para 62A, exception:** if an onerous underlying group is recognised earlier, and the reinsurance was entered into before or at that time, the reinsurance held is recognised at that earlier date. This lets the loss-recovery component work (section 6).

## 3. General Measurement Model (GMM / BBA)
**On initial recognition:** liability = fulfilment cash flows (FCF) + contractual service margin (CSM) (para 32). FCF has three parts:
- **Estimates of future cash flows (paras 33-35, B61-B71).**
  - Unbiased, probability-weighted and current.
  - Only cash flows within the **contract boundary**. The boundary ends when the entity can reprice to fully reflect the risk.
- **Discounting (para 36, B72-B85).**
  - Rates must reflect the characteristics of the liability.
  - Two methods are allowed: bottom-up (a risk-free rate plus an illiquidity premium) or top-down (a reference portfolio yield less credit risk).
- **Risk adjustment for non-financial risk (RA) (para 37, B86-B92).**
  - The compensation the entity requires for bearing uncertainty in amount and timing.
  - The method is entity-specific, but the equivalent confidence level must be disclosed (para 119).

**CSM** (para 38):
- The unearned profit. It is set so that no day-1 gain arises.
- If the FCF is a net outflow, the group is **onerous**: the loss goes to P&L immediately and a loss component is set up (para 47).

**Subsequent measurement** (para 40):
- Liability for Remaining Coverage (LRC) = FCF for future service + CSM.
- Liability for Incurred Claims (LIC) = FCF for past service.

**CSM movements** (para 44):
- Add new business.
- Accrete interest at the **locked-in** rate.
- Absorb changes in FCF that relate to future service (for example non-financial assumption changes), measured at locked-in rates (B96).
- Release to revenue by coverage units (B119).

**Other movements:**
- Changes in FCF relating to past service go to P&L (insurance service result).
- Financial-risk changes go to insurance finance income or expense (para 87), optionally split between P&L and OCI (paras 88-89).

## 4. Variable Fee Approach (VFA) for direct participating business
- **Eligibility (B101).** All three must hold:
  - the policyholder participates in a clearly identified pool of underlying items;
  - the entity expects to pay a substantial share of the fair-value returns;
  - a substantial proportion of the change in the amount payable varies with the underlying items.

  Typical cases are unit-linked and many participating savings products.
- **The CSM absorbs changes in the entity's share of the underlying items** (para 45). This includes financial changes, so P&L volatility is lower than under GMM.
- **Risk-mitigation option (B115-B118):** if derivatives or reinsurance held mitigate financial risk, the related changes can go to P&L instead of the CSM, which avoids an accounting mismatch.

## 5. Premium Allocation Approach (PAA): the default for short-term business
**Eligibility (para 53):**
- the coverage period of each contract in the group is one year or less; or
- PAA is reasonably expected to give an LRC not materially different from GMM.

Most medical, group life, credit life (single-premium credit life is often longer than a year, so test it) and non-life business uses PAA.

**LRC under PAA (para 55):**
- premiums received;
- less insurance acquisition cash flows (IACF), unless they are expensed;
- adjusted for amortisation of IACF;
- less revenue recognised.

Options:
- IACF may be expensed when incurred if coverage is one year or less (para 59(a)).
- No time-value adjustment to the LRC if the time between premium and coverage is one year or less (para 56).

**LIC (para 59(b)):** measured at FCF, including the RA. Discounting is not required if claims are expected to be paid within one year of being incurred.

**Onerous test (paras 57-58):** performed only if facts and circumstances indicate onerousness. If so, recognise a loss component equal to the excess of the FCF for remaining coverage over the PAA carrying amount.

**Revenue (B126):** expected premium receipts allocated over the coverage period, on the basis of time unless risk release differs materially.

## 6. Reinsurance contracts held (paras 60-70A): the core of broker conversations
- **Measured separately** from the underlying contracts. Assumptions must be consistent with the underlying (para 63).
- **Non-performance risk** of the reinsurer is included in the FCF of the reinsurance held (para 63).
- **RA for reinsurance held** = the amount of risk transferred to the reinsurer (para 64). Ceding reduces the net RA.
- **Initial CSM (paras 65, 65A).**
  - Para 65: any net cost or net gain on purchase is deferred in the CSM and released as service is received.
  - **Para 65A, exception:** a net cost that relates to events before purchase (past events, for example an LPT or ADC on existing reserves) is **expensed immediately**.
  - **Practical test [INTERP]:** an LPT priced above the IFRS 17 FCF of the transferred LIC (best estimate plus RA, discounted) shows a day-1 loss, even when it releases statutory reserves.
- **Loss-recovery component (paras 66A-66B, B119C-B119F; 70A under PAA).**
  - **Trigger:** a loss is recognised on initial recognition of an onerous underlying group, or when onerous contracts are added to it.
  - **Effect:** the reinsurance-held CSM (or, under PAA, the asset for remaining coverage) is adjusted and income is recognised.
  - **Amount:** the loss × the percentage of claims on the underlying group that the entity has a right to recover.
  - **Later deterioration** of underlying groups that does not adjust their CSM flows through to reinsurance held in P&L via para 66(c)(ii).
  - **Practical consequence:** a quota share incepted at the same time as onerous business offsets part of the onerous loss.
  - VERIFY the final 2020 wording. The 2019 Exposure Draft limited this to proportionate cover; check the final standard for any change to that scope.
- **Reinsurance held cannot be onerous.** The cost of cover is spread, not front-loaded, except for the past-events rule above.
- **PAA for reinsurance held (paras 69-70)** is allowed on the same eligibility logic as section 5. A risk-attaching treaty covering one-year policies can have a coverage period longer than one year, so test eligibility.
- **Presentation (para 86).** Income and expense from reinsurance held is shown separately from insurance contracts issued. It may be presented as one net amount ("net expense from reinsurance contracts held").
  - Ceding commissions **not contingent on claims** reduce the premium ceded. They are recognised over the coverage, not on day 1.
  - Amounts **contingent on claims** of the underlying contracts are treated as part of claims recoveries. Examples are sliding-scale adjustments and loss-dependent profit commissions.
- **Broker implications [INTERP]:**
  1. A flat ceding commission does not create a day-1 IFRS gain. It shows in reinsurance income over the coverage period.
  2. Sliding-scale and profit commissions sit inside the recoveries line, so the treaty's loss-ratio sensitivity is visible.
  3. The reinsurance result is usually a net expense (the margin given to reinsurers). Management will judge treaties on it.
  4. Timing a quota share to inception of known-onerous business matters for the loss-recovery component.

## 7. Presentation and KPIs: translating old metrics
| Old (IFRS 4 / statutory) | IFRS 17 | Notes |
|---|---|---|
| Gross written premium (GWP) | Not presented. Insurance revenue = release of expected claims + expenses + RA release + CSM release + IACF allocation (GMM, B121-B124); under PAA it is the allocation of expected premium | GWP often appears only in segment notes or MD&A. Regulators and solvency factors usually still use GWP and earned premium |
| Net earned premium | Insurance revenue less allocation of reinsurance premiums | Not equal |
| Claims incurred | Insurance service expenses (incurred claims, expenses, losses and reversals on onerous groups, IACF amortisation) | Investment components are excluded from revenue and expenses (para 85) |
| Underwriting result | Insurance service result (ISR) = insurance revenue − insurance service expenses + net result from reinsurance held | |
| Investment income on technical funds | Net insurance finance income/expense, shown alongside investment income | Unwind of discount, effect of rate changes |
| Reserves (UPR, OSLR, IBNR, mathematical) | LRC, LIC (each split into PV of cash flows, RA and CSM in the notes) | Reconciliations: paras 98-105 |

## 8. Disclosures to mine when reading accounts
- **Movement analysis (paras 98-105):** LRC excluding loss component, loss component, LIC; and PV of future cash flows / RA / CSM.
- **Expected CSM release by time band (para 109).**
- **RA confidence level (para 119).**
- **Sensitivities to insurance and market variables (para 128).**
- **Claims development (para 130):** a direct test of reserving strength and of prior-year releases.
- **Transition method and transition CSM (paras C1-C33).** Full retrospective, modified retrospective or fair value. A fair-value transition CSM can flatter or depress future profit emergence.

## 9. Why IFRS 17 equity ≠ regulatory own funds (generic, [INTERP])
Typical reconciling items:
1. **Liability basis.** Prudential reserves may be prudent, undiscounted and floored, or best estimate with prescribed margins. IFRS 17 uses current discount rates, an entity-specific RA, and holds the CSM as a liability.
2. **Admissibility haircuts** on assets the accounts carry at full value. Examples: concentrations, real estate, related-party balances, aged receivables, intangibles, deferred acquisition costs.
3. **Capital items** recognised only by the regulator, such as approved letters of credit and uncalled capital, or deducted only by the regulator, such as treasury shares.
4. **Fund segregation** (takaful, participating funds).

Always rebuild the regulatory number from the regulatory basis. Do not adjust IFRS equity by a guessed factor.


<!-- ===== FILE: references/01-core-solvency-method.md ===== -->

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


<!-- ===== FILE: references/qa-qfc/30-qfc-legal-framework.md ===== -->

# Qatar (QFC): legal framework, perimeter, governance and reporting

**Sources.**
- **[RULE]:** QFCRA Insurance Business Rules 2006 (PINS), Version 20, effective 1 Oct 2025 (includes QFCRA Rules 2024-4 and 2025-1). Rule numbers below are PINS unless stated.
- **[TEMPLATE]:** QFCRA insurance prudential return (XBRL workbook, taxonomy `QFCRA_INS` 2.0.0, 2025 namespace), from a Q3 2026 specimen filing with no data. See file 31 §5.

## 1. Perimeter: Qatar has two insurance regimes. Route first.
| Where the entity is licensed | Regulator | Rules | Covered here? |
|---|---|---|---|
| **Qatar Financial Centre (QFC)**: has a QFC number, authorised by the QFC Regulatory Authority | QFCRA | Financial Services Regulations (FSR), PINS, GENE, CTRL, CAPI (captives) | **Yes**, this layer |
| **Onshore State of Qatar**: listed and unlisted Qatari insurers, takaful operators, branches of foreign insurers licensed by the central bank | Qatar Central Bank (QCB), under Law 13/2012 | QCB Governor Decision 1/2016 (Executive Instructions for the Insurance Sector and Governance Principles), plus later QCB circulars | **No.** No QCB layer is loaded. Say so, use the core files only, and list the QCB facts needed |

- **Do not apply PINS factors to an onshore QCB insurer.** Group parents of QFC entities are often QCB-regulated, so check the licence of the specific legal entity.
- Public reporting (not verified here) says QCB onshore requires capital above QAR 100m for listed insurers, or risk-based capital if higher, and a QAR 35m deposit for branches. Treat this as background only, until the QCB text is loaded.

## 2. Who PINS capital rules apply to [RULE]
- **QFC insurer**: an authorised firm with an authorisation to conduct insurance business (1.2.3).
- **QFC-incorporated insurers (LLCs)** must meet Chapter 3 (MCR, SRR) and Chapter 4 (eligible capital) (3.1.1, 4.1.1).
- **Branches** are outside Chapters 3 and 4. They follow home-jurisdiction capital rules (3.1.1 note; 4.1 guidance 3).
  - [TEMPLATE] base capital is 0 for a branch.
  - Form INS50 asks for the home capital requirement and the excess over it, plus cash and liquid assets held in Qatar.
- **Branches are also exempt from ORSA** (2.4.2 note). Run-off rules (Ch 12) do apply to a branch's QFC business.
- **QFC captive insurers** are excluded from Chapters 3 and 4 (CAPI applies).
- **Every insurer** must hold the financial resources PINS requires, plus whatever more is adequate for the nature, size and complexity of its business (1.2.2). The governing body judges whether the minimum is enough.

## 3. Business classification [RULE]
- **General and long-term business.** These are defined by the FSR, Schedule 3, Part 3: para 10.3 (general categories) and 10.4 (long-term) (1.2.5-1.2.6).
- **Composite ban** (1.5.1): an insurer cannot carry on both long-term and general business in or from the QFC, unless the general business is restricted to **categories 1 (accident) and 2 (sickness)**. So a life insurer may also write medical and personal accident, but not other general lines.
- **No non-insurance business** except activity directly connected with it (1.5.2). Managing investments for third parties is not "connected".
- **PINS categories** (1.2.8) drive the premium and outstanding-claims factors:

| PINS category | FSR general insurance categories | Meaning |
|---|---|---|
| 1 | 1, 2 | Accident, sickness (**medical, PA, group medical**) |
| 2 | 3, 18 | 3 = land vehicles (motor own damage) [INTERP]; 18 = assistance [INTERP] |
| 3 | 4-9, 16, 17 | Property, transport and miscellaneous classes [INTERP] |
| 4 | 10-15 | Liability classes, credit and suretyship [INTERP] |

- Only the names of categories 1 and 2 are confirmed by PINS text (1.5.1). The other names follow the usual EU-style class list. **VERIFY** them against FSR Schedule 3, Part 3, para 10.3.
- **Mapping is the filer's job.** The PINS category is a classification input. The template does not map the premium lines of business (INS300) to PINS categories.

## 4. Takaful [RULE]
- **Takaful entity**: an Islamic financial institution doing takaful, or a QFC insurer operating an Islamic window (1.2.7).
- **Chapter 6** applies (for a window, only to the Islamic business):
  - takaful funds must be established and kept segregated, with separate books (6.2-6.4);
  - asset allocations to funds must be fair (6.4.5);
  - **no loans from a takaful fund** (6.5.1);
  - surplus and deficit policies must be given to the Authority, and the surplus or deficit determined annually (6.6).
- **Capital** (4.2.2):
  - **owners' equity** counts as tier 1 only for a takaful entity, and only if surplus and loss participation is limited to policyholders (4.3.1(g));
  - **zakah fund balances are deducted** from capital (4.6.5).
- **Accounting basis:** AAOIFI (8.4.1(2)(a)). The PINS valuation rules in 8.4.6-8.4.7 and Parts 8.5-8.8 also apply (file 33).
- Do not give Sharia rulings (SKILL.md §4).

## 5. Long-term insurance funds [RULE]
- Long-term business must sit in **long-term insurance funds**, with segregated assets, liabilities, revenue and expenses (Ch 5).
- **Fund assets** may not be transferred, distributed or lent out of the fund, except as permitted (5.5.1-5.5.5).
- **Internal reinsurance** between a long-term fund and the rest of the insurer, or between its own long-term funds, is **prohibited** (5.5.6).
- Accident and sickness contracts may be attributed to a long-term fund (5.3.2).

## 6. Investments [RULE]
- **Prudent person** (8.1.4):
  - invest only where the insurer can identify, measure, manage and report the risk;
  - avoid concentration;
  - keep unlisted assets at prudent levels;
  - assets covering technical provisions must match the liabilities.
  - Guidance expects liquid assets: cash, deposits, tradable securities, listed shares, liquid bonds.
- **Derivatives** may be used for risk reduction and sound hedging only. Never for speculation (8.1.5).
- **Concentration limit for LLCs** (8.1.6): exposure to a single counterparty or related counterparties (on- and off-balance sheet, including intra-group) must not exceed **the lower of 20% of applicable assets and eligible capital**.
  - Applicable assets = total assets less reinsurance receivables, premium receivables, DAC, fixed assets, intangibles and other non-investment assets.
  - So **reinsurance recoverables are outside this limit**.
  - Assets already deducted from eligible capital are also outside it.
  - Bank deposits count, so a deposit with a single bank is a typical breach risk.

## 7. Governance hooks [RULE]
- **ORSA** (2.4): annual for QFC-incorporated insurers.
  - Covers own capital needs under adverse scenarios.
  - Written report approved by the governing body; given to the Authority on request.
  - Revised when a change of strategy or business plan materially changes capital adequacy.
  - The SRR guidance says ORSA evidence can move the insurer's SRR (3.3.2A guidance 2).
- **Actuary:**
  - Insurers required to have an approved actuary (CTRL 6.5.2) get an annual **Financial Condition Report** (9.1.2-9.1.3).
  - Others: the governing body considers an independent actuarial report annually, and **must commission one at least every 3 years** (9.2.2).
  - The approved actuary must advise on the maximum event retention (MER) in the cases in A3.10.2(2).
- **Groups** (Ch 10):
  - **MCR and SRR also apply at financial-group level**, calculated as if the group were one insurer (10.3.3).
  - Surplus capital of group members that is not freely transferable is excluded (10.3.2).
  - The insurer must inquire into, and the Authority may direct on, intra-group transactions (10.1.7-10.1.9).
- **Capital management:**
  - **Tier 1** may not be reduced without prior approval, which needs a capital plan showing MCR is met for 2 years without new capital (4.8.1-4.8.2). Buybacks count as reductions, as do dividends exceeding the year's earnings.
  - **Tier 2** reduction needs 6 months' notice (4.8.3).
  - **Dividends and distributions** must be reported within 15 business days of declaration (4.9.1).
- **Portfolio transfers** need a scheme report and notifications (Ch 11).
- **Run-off** (Ch 12): a run-off plan is required, and QFC-incorporated insurers in run-off may not make distributions.

## 8. Intervention ladder [RULE]
| Event | Duty | Consequence |
|---|---|---|
| Possible breach of 1.2.2 or Ch 3 (MCR or SRR) | Tell the Authority orally within 1 business day; written confirmation and explanation by the next business day; set out avoiding action (**except for SRR**); **no distributions** without written permission (3.9.1) | Authority confers with the insurer |
| Actual MCR breach (eligible capital < MCR) | Same notifications (3.3.2(1), 3.9.2) | **Stop writing new business** until permitted (3.3.2(2), 3.9.2(c)). Subordinated debt may not be serviced (4.4.2(1)(b)). Authority may require capital, suspend, place in run-off or withdraw authorisation (3.3.2 guidance) |
| Actual or possible SRR breach (eligible capital < SRR) | Notify; **board-approved action plan with timescales** as soon as possible; the Authority may amend it (3.9.3) | **No stop-writing rule** (3.3.2A note). No distributions without permission |

## 9. Prudential reporting [RULE + TEMPLATE]
- **Which returns:** set by written notice on an approved website. The Authority can add returns or exempt an insurer (1.4.1).
- **Deadlines:**
  - annual return: within **3 months** of year end (1.4.2);
  - biannual return: within **1 month** of 30 Jun or 31 Dec (1.4.3);
  - quarterly return: within **1 month** of quarter end (1.4.4).
- **Format:** XBRL workbook `QFCRA_INS`.
  - A declaration form and a scope-of-filing questionnaire switch schedules on or off:
    - Sharia, long-term, general;
    - client money, captive manager;
    - non-QAR currencies, derivatives;
    - PAA / GMM / VFA in use.
  - Amounts are in QAR '000.
- **The governing body can be asked** to certify compliance or the accuracy of returns (1.3.1).


<!-- ===== FILE: references/qa-qfc/31-qfc-solvency-requirements.md ===== -->

# Qatar (QFC): MCR, SRR, eligible capital, risk-based capital and the INS600/INS610 template

**Sources:**
- **[RULE]:** PINS V20 Chapters 3-4 and Schedule 3.
- **[TEMPLATE]:** the QFCRA INS prudential return workbook (taxonomy 2.0.0), forms INS600 and INS610.x.

Factors below were checked in Nov 2026 against both the rule text and the template formulas. Where they differ, see §6.

## 1. Architecture [RULE]
Applies to QFC-incorporated insurers only; not branches or captives (file 30 §2).

| Test | Requirement | Rule | Consequence of breach |
|---|---|---|---|
| **MCR** | Eligible capital ≥ **max(QAR 36m, risk-based capital requirement)** | 3.2.1, 3.3.1 | Stop writing new business |
| **SRR** (from 1 Aug 2024) | Eligible capital ≥ **150% × risk-based capital requirement**. The Authority may set a different SRR, taking account of: retail or catastrophe volatility, market importance, investment geography, risk management, ORSA, strategy and rating | 3.3.2A | Board-approved action plan; no stop-writing |
| Firm-specific | The Authority may impose a higher MCR as a licence condition (3.3.1 note 2) | | |

**Which test binds [INTERP]:**
- SRR binds whenever 1.5 × RBC > max(36m, RBC). That means whenever **RBC > QAR 24m**.
- Below QAR 24m RBC the QAR 36m floor binds. There, reducing RBC creates **no** headroom.
- From QAR 24m RBC upwards, each QAR 1 of RBC saved frees **QAR 1.5** of required capital.
- Always state both covers: eligible ÷ MCR, and eligible ÷ (1.5 × RBC).

**Risk-based capital requirement (RBC)** (3.4.1):
- **RBC = IRR + InsRR + ORR**: investment risk + insurance risk + operational risk.
- **Simple sum: no correlation or diversification credit.**
- An internal model approved by the Authority can replace the whole RBC or individual components (3.8). The insurer's home or group regulator must also have approved it.
- [TEMPLATE] INS610 L17 holds the internal-model figure. L18 MCR = MAX(base, RBC, internal model).

## 2. Eligible capital (4.2.2 table) [RULE] = template INS600
| Line | Item | Notes |
|---|---|---|
| A Tier 1 | Permanent share capital | Fully paid, undated, non-cumulative, first loss (4.3.1(a)) |
| | Audited reserves | Retained profits after tax and dividends. Includes capital contributions meeting (a), notified 1 month ahead (4.3.1(b)-(c)) |
| | Share premium | |
| | Externally verified interim net profits | **Auditor-verified only** (4.3.1(e)). Unverified quarter profits do not count |
| | Fund for future appropriations | |
| | Owners' equity | **Takaful only** |
| B Deductions from tier 1 | Own shares; **intangibles** (goodwill, capitalised development, brands, licences); interim net losses | Cumulative losses and negative reserves are deducted (4.3.1(i)) |
| C | Tier 1 after deductions = A − B | |
| D Upper tier 2 | Perpetual qualifying hybrids (unsecured, subordinated, perpetual, loss-absorbing); fixed-dividend ordinary shares | 4.4.1 |
| E Lower tier 2 | Subordinated debt; fixed-term preference shares | Sub debt conditions in 4.4.2. **≥5-year original maturity**; no step-ups in the first 5 years; no payment while in MCR breach; 30-day no-objection notice. **Amortised 20% a year over the last 4 years** (4.4.3). External legal opinion needed (4.5.1) |
| Limits | **Lower T2 ≤ 50% of C** (4.7.2); **total T2 ≤ 100% of C** (4.7.1) | [TEMPLATE] INS600 L18 = ROUND(MIN(L16+L17, L12/2)); L19 = MIN(L15+L18, L12) |
| G Deductions from T1+T2 | Investments in subsidiaries and associates; connected lending of a capital nature; **inadmissible assets**; zakah fund (takaful) | 4.6 |
| H | **Eligible capital = C + D + E − G** | INS600 L26 → INS610 L19 |

**Inadmissible assets** (4.6.4), deducted in full:
- tangible fixed assets, including inventories, plant, equipment and vehicles;
- **deferred acquisition costs**;
- **deferred tax assets**;
- deficiencies of net assets in subsidiaries;
- a subsidiary's holding of the insurer's own shares;
- investments not readily realisable.

Assets deducted here carry **no** asset risk charge (A3.2.4).

**There is no ancillary-capital tier.** Letters of credit, guarantees and uncalled capital do not appear in the table. The Authority may recognise other instruments that meet international standards (4.2.1 guidance). **[INTERP]:** an LoC is not capital without specific QFCRA recognition. It can still reduce asset risk as collateral or guarantee (A3.2.2).

## 3. Risk-based capital: module by module [RULE, Schedule 3]
### 3.1 Counterparty grades (A3.1.1-A3.1.2)
| Grade | S&P / Fitch | Moody's | AM Best |
|---|---|---|---|
| 1 | AAA | Aaa | A++ |
| 2 | AA+ to AA- | Aa1-Aa3 | A+ |
| 3 | A+ to A- | A1-A3 | A, A- |
| 4 | BBB+ to BBB- | Baa1-Baa3 | B++, B+ |
| 5 | BB+ and below | Ba1 and below | B and below |

- **Unrated = grade 4.**
- Use one agency consistently. If ratings differ, **use the one giving the highest charge**.
- Only the four listed agencies may be used, unless the Authority permits another.

### 3.2 Investment risk requirement (IRR) = asset + off-balance-sheet asset + off-balance-sheet liability components (3.5.1)
**Asset risk** = Σ value × factor (A3.2.1). INS610.10 lines 1-43.

| Factor | Non-reinsurance assets (Table A3.2.1A) |
|---|---|
| 0.5% | Cash, bank deposits and cash equivalents; grade 1 sovereign bonds |
| 1% | Bonds < 1 yr (grade 1-2); cash management trusts (grade 1-2) |
| 2% | Unpaid premiums ≤ 6 months due from grade 1-3 counterparties; bonds ≥ 1 yr (grade 1-2) |
| 4% | Unpaid premiums ≤ 6 months (unrated or grade 4-5); bonds grade 3; cash management trusts grade 3; secured loans |
| 6% | Unpaid premiums > 6 months (grade 1-3); bonds grade 4; cash management trusts grade 4 |
| 8% | Unpaid premiums > 6 months (unrated or grade 4-5); bonds grade 5; cash management trusts grade 5; listed subordinated debt |
| 10% | Unlisted subordinated debt; preference shares |
| 16% | Listed equity (includes collective investment funds, joint ventures, mudaraba/musharaka certificates per the glossary); listed trusts |
| 20% | Real estate (direct); unlisted equity; unlisted trusts; **any other non-reinsurance asset** |
| 100% | Loans to directors (and their related parties or dependants); unsecured staff loans (except under QAR 3,600); assets under a fixed or floating charge |

**Reinsurance assets** (Tables A3.2.1B/C):

| Grade | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Reinsurer supervised by a "subrule (2) regulator" | 1% | 2% | 4% | 6% | 8% |
| Reinsurer not supervised by one | 1.2% | 2.4% | 4.8% | 7.2% | 9.6% |

- **Subrule (2) regulators:** Qatar, EU member states, Australia, Canada, Hong Kong, Iceland, Japan, Norway, Singapore, Switzerland, USA, **or any signatory of the IAIS Multilateral MoU**.
- **[INTERP]:** most GCC regulators that have signed the IAIS MMoU qualify. **VERIFY** the signatory list on the date of use.

**Asset risk adjustments:**
- **Guarantee** (A3.2.2(1)): explicit, unconditional and irrevocable for the full term, from an unrelated guarantor rated grade 1-3. The asset takes the guarantor's charge.
- **Collateral** (A3.2.2(2)): cash or grade 1-3 debt. The covered part takes the collateral's charge.
- **Charged or mortgaged assets** (A3.2.3): 100% charge to the extent of the secured debt. If the security backs insurance liabilities, only the excess of market value over the supported liabilities is charged.

**Off-balance-sheet asset risk, derivatives** (A3.4):
- Excluded: put options serving as guarantees; FX contracts with original maturity ≤ 14 days; exchange-traded contracts that are marked to market daily.
- **Rule:** asset-equivalent value × the counterparty's asset-risk %, where asset-equivalent value = positive MTM + notional × add-on.

| Add-on | IR | FX & gold | Equity | Precious metals (not gold) | Other |
|---|---|---|---|---|---|
| < 1 yr | 0 | 1% | 6% | 7% | 10% |
| 1-5 yrs | 0.5% | 5% | 8% | 7% | 12% |
| ≥ 5 yrs | 1.5% | 7.5% | 10% | 8% | 15% |

**Off-balance-sheet liability risk** (A3.5):
- Face value of credit substitutes issued (LoCs, guarantees, put options serving as guarantees) × the asset charge of the underlying obligation.
- Collateral and guarantee relief applies.
- Credit and surety **insurance** is not a credit substitute.

### 3.3 Insurance risk requirement (InsRR) = premium + outstanding claims + long-term + concentration (3.6.1)
**Premium risk** (A3.7, general business):
- **Net premium liability** by PINS category × factor.
- Net premium liability = premium liability (8.6.7: the value of future claims and settlement costs on in-force cover) less expected reinsurance and other recoveries.

**Outstanding claims risk** (A3.8):
- **Net outstanding claims liability** (8.6.8: reported claims, IBNR and loss adjustment expenses, less expected recoveries) × factor.

| PINS cat | Premium: direct | Premium: prop. reins. | Premium: non-prop. reins. | Claims: direct | Claims: prop. | Claims: non-prop. |
|---|---|---|---|---|---|---|
| 1 (accident, sickness) | **16%** | 18% | 21% | **11%** | 12% | 14% |
| 2 | 13% | 15% | 18% | 9% | 10% | 12% |
| 3 | 16% | 18% | 21% | 11% | 12% | 14% |
| 4 | 21% | 23% | 26% | 14% | 15% | 17% |

- **The factors apply to NET liabilities, with no net/gross floor.** Contrast the UAE 50% floor.
- **The "reinsurance" columns are for inward reinsurance written**, by type. They are not a credit for outward cover.
- **Lower factors on application for medical business (lever):**
  - **PINS 1 premium factors** can be reduced with written consent where mortality and morbidity data support actuarial reliance. Floor: **12%** (direct and proportional), **16%** (non-proportional) (A3.7.3).
  - **Outstanding-claims factors** for any category can be reduced the same way, to a floor of **8%** (A3.8.3).
- Long-term contracts in PINS 1 use the long-term component instead (A3.7.4, A3.8.4).

**Long-term insurance risk** (A3.9) = Σ of:

| Item | Factor |
|---|---|
| Provisions: investment-linked with capital guarantee | 1.25% |
| Provisions: investment-linked without guarantee | 0.5% |
| Provisions: all other long-term business | 3% |
| Capital at risk (CAR) | **0.1%** |
| Mortality-contingent policies | Claims cost of a **+0.5 per mille** increase in the death rate over the next year |

- **CAR** = sums assured less mathematical reserves less **expected reinsurance recoveries**, floored at 0 per contract. For annuities, the sum assured is the PV of the annuity payments.
- [TEMPLATE] INS610.60 implements the mortality item as **0.05% × CAR of mortality-contingent policies**.
- **Whether "provisions" are gross or net of reinsurance is not stated.** VERIFY in the return instructions.

**Insurance concentration risk** (A3.10, general business):
- Charge = **MER + CoR − RP**.
  - **MER**: the maximum event retention net of reinsurance, for a single extreme event, at a **≥ 1-in-250** return period. Take the largest MER across events. The approved actuary's advice is required for portfolios that are unlimited, multi-line or complex.
  - **CoR**: the contractual (or estimated, but not below the original rate) cost of one reinstatement.
  - **RP**: inward reinstatement premiums under binding netting arrangements, for insurers that write reinsurance.
- Guidance names medical insurers: common-source claims (for example, a class action from one faulty procedure in a large scheme) are concentration risk even without a natural catastrophe.

### 3.4 Operational risk requirement (ORR) (3.7.1)
- **ORR = min[ 2% × max(GWP over the last 12 months, gross technical provisions), (IRR + InsRR) × 15/85 ]**.
- **The basis is gross, but the cap moves with net risk.** For an insurer whose cap binds, cutting InsRR also cuts ORR.

## 4. Worked example (QAR '000, illustrative; medical-focused QFC LLC)
**Inputs and asset risk:**

| Asset | Value | Factor | Charge |
|---|---|---|---|
| Cash and deposits | 150,000 | 0.5% | 750 |
| Bonds, grade 2, ≥ 1 yr | 100,000 | 2% | 2,000 |
| Listed equity | 30,000 | 16% | 4,800 |
| Unpaid premiums ≤ 6 months, unrated | 40,000 | 4% | 1,600 |
| Reinsurance assets, grade 3, supervised | 60,000 | 4% | 2,400 |
| **IRR** | | | **11,550** |

**Insurance risk:**
- Net premium liability PINS 1, direct: 50,000 × 16% = 8,000.
- Net outstanding claims PINS 1, direct: 70,000 × 11% = 7,700.
- Concentration: MER 5,000 + CoR 1,000 = 6,000.
- **InsRR = 21,700.**

**Operational risk:**
- 2% × max(GWP 300,000; gross technical provisions 220,000) = 6,000.
- Cap = 33,250 × 15/85 = 5,868.
- **ORR = 5,868** (the cap binds).

**Result:**
- **RBC** = 11,550 + 21,700 + 5,868 = **39,118**.
- **MCR** = max(36,000; 39,118) = 39,118.
- **SRR** = 1.5 × 39,118 = **58,677**.
- **Eligible capital** = share capital 60,000 + audited reserves 20,000 − intangibles 2,000 − inadmissible assets (DTA 500, fixed assets 1,500) 2,000 = **76,000**.
- **Cover:** MCR 194%; SRR 130% (= 194% / 150%). **SRR binds**, with headroom of 17,323.

**Adding a 30% medical quota share** (reinsurer grade 3, supervised; premium and claims liabilities ceded pro rata):
- Premium risk: 35,000 × 16% = 5,600.
- Claims risk: 49,000 × 11% = 5,390.
- InsRR = 16,990, assuming MER unchanged.
- Reinsurance assets rise by 36,000, at 4% = +1,440. IRR = 12,990.
- Cap = 29,980 × 15/85 = 5,291. **ORR = 5,291** (falls, because the cap binds).
- **RBC = 35,271** (−3,847). **SRR = 52,907.** Required capital falls by **5,770**.

Ignored here: cash ceded, commission, and IFRS 17 effects (file 33). Ceding to an unsupervised reinsurer would cost 4.8% instead of 4% on the recoverable.

## 5. Template map (INS workbook) [TEMPLATE]
Calculation order:

INS610.10 → .20 → .30 → .40 → .50 → .60 → .70 → INS610 → (with INS600) result.

| Form | Content | Feeds |
|---|---|---|
| INS600 | Eligible capital L1-L26 | INS610 L19 |
| INS610.10 | Asset risk: 28 non-reinsurance lines + 10 reinsurance lines (supervised and unsupervised, by grade). H = ROUND(value × factor) | INS610 L3 |
| INS610.20 | Derivative add-on grid (5 contract types × 3 maturities) | L4 |
| INS610.30 | Credit substitutes: value × manually entered %, per row | L5 |
| INS610.40 / .50 | Net premium liability / net outstanding claims, by PINS category 1-4 × direct / prop. / non-prop. | L7 / L8 |
| INS610.60 | Long-term (hidden if no long-term business) | L9 |
| INS610.70 | Concentration: cat cover yes/no | L10 |
| INS610 | L1 type (LLC or branch, from DECLARATIONFORM), L2 base capital 36,000 (branch 0); L6 IRR, L11 InsRR, L12-L15 ORR with cap; L16 RBC; L17 internal model; **L18 MCR = MAX(L2, L16, L17)**; L19 eligible capital; **L20 = L19 − L18** | Result |
| INS620 | Intermediary capital (base QAR 1.8m with client money / 0.9m without / 0.18m captive manager; paid-up capital test; adjusted net assets ≥ 50% of base) | Standalone, not the insurer test |

**Related disclosure forms (no formula feed into RBC):**
- INS100 balance sheet;
- INS130 investment concentration and geography;
- INS300 premiums by line of business, location, channel and fac/treaty;
- INS320 claims by line of business;
- INS340 reinsurance (10 largest reinsurers with rating and collateral; treaty limits and retentions by line);
- INS350 largest clients;
- INS700.10 intra-group.

**Every capital input is keyed by hand.** No formula links INS300, INS320 or INS100 to INS610.x. The filer must reconcile them.

## 6. Template vs rule: points to watch (VERIFY with the QFCRA return instructions)
1. **SRR is not computed in the workbook.** L20 shows only the surplus over MCR. Compute **eligible − 1.5 × L16** separately. A positive L20 can coexist with an SRR breach.
2. **INS610.70 has a fallback the rule does not contain.** If there is no cat reinsurance, the charge is **2 × largest per-risk retention**. This presumably comes from the return instructions. With cat cover: MER + CoR − RP, as in the rule.
3. **INS610.20 applies the add-on % to notional as the charge.** The rule adds positive MTM and then applies the counterparty's asset-risk %. Follow the instructions of the version filed.
4. **INS610.60 uses 0.1% CAR and 0.05% × mortality-contingent CAR.** This matches A3.9.2(d)-(e) as an approximation. Line 1 "annuity and pensions" uses 3%, matching (c).
5. **Prior-period comparatives carry hard-coded dates.** Do not treat them as linked.
6. **ORR GWP and gross technical provisions are entered by hand,** not pulled from INS200 or INS300.


<!-- ===== FILE: references/qa-qfc/32-qfc-reinsurance-rules.md ===== -->

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


<!-- ===== FILE: references/qa-qfc/33-qfc-ifrs17-bridge.md ===== -->

# Qatar (QFC): IFRS 17 and the prudential basis

**Sources:**
- **[RULE]:** PINS V20 8.4.1, 8.4.3-8.4.5, Parts 8.5-8.8, 4.3.1, 4.6.4.
- **[TEMPLATE]:** INS100, INS200, INS300, INS400-INS540 and SCOPEOFFILING.

## 1. What the regulatory balance sheet is [RULE]
**Prudential returns use a "permitted basis of accounting"** (8.4.1):
- **IFRS** for conventional insurers, so **IFRS 17**;
- **AAOIFI** for takaful entities.

**PINS measurement rules for takaful only.** The PINS rules below are stated to apply to **takaful entities**. They override AAOIFI where they conflict (8.4.1(3)(b)):
- reinsurance valuation (8.4.6);
- discount rate (8.5.1: a prudent estimate of the expected asset yield);
- premium liability and outstanding claims liability (Part 8.6);
- long-term valuation (Part 8.7);
- methods (Part 8.8).

**For all insurers:**
- the Authority can direct other valuation principles (8.2.4);
- an insurer may value assets lower and liabilities higher (8.2.1-8.2.2);
- assumption changes must hit values immediately (8.4.3);
- buying reinsurance does not derecognise the liability (8.4.5).

**Consequence [INTERP]:**
- For a conventional QFC insurer, **the capital base starts from the IFRS 17 balance sheet**. This is unlike the UAE, where a statutory basis applies.
- Eligible capital is IFRS 17 equity, re-tiered and with deductions. There is no separate statutory-reserve layer.
- So IFRS 17 measurement choices move capital one-for-one, before the RBC factors:
  - PAA vs GMM;
  - discounting;
  - RA confidence level;
  - CSM;
  - onerous-contract losses;
  - OCI option.

## 2. Equity-to-eligible-capital bridge [RULE + INTERP]
| Step | Item | Source line (INS100 / INS600) | Notes |
|---|---|---|---|
| IFRS 17 total shareholders' equity | | INS100 L157 | Takaful: shareholders only. Participants' fund columns are shown separately |
| − | **CSM and RA** | Inside insurance contract liabilities (L98) | **Not capital.** Under IFRS 17 they are liabilities. No add-back (contrast Solvency II, where future profits are own funds) |
| − | Unverified interim profits; + interim losses already deducted | INS600 L4 / L10 | Only **auditor-verified** interim profits count (4.3.1(e)) |
| − | Reserves not qualifying as "audited reserves" | INS600 L2 | FVOCI, insurance-finance OCI and hedging reserves: **VERIFY** treatment in the return instructions |
| − | Own shares; **intangibles** (goodwill, software, other) | INS100 L75 → INS600 L9 | |
| + | Qualifying tier 2 (hybrids, sub debt, fixed-term preference shares) within limits | INS100 L119 → INS600 L13-L19 | Sub debt is on the IFRS balance sheet as a liability |
| − | Subsidiaries and associates; connected lending | INS100 L67-L70 → INS600 L21-L22 | |
| − | **Inadmissible assets**: PP&E, DTA, DAC, non-realisable investments | INS100 L80, L83, L88 → INS600 L23 | Right-of-use assets as "tangible fixed assets": **VERIFY** |
| − | Zakah fund (takaful) | INS100 L140 → INS600 L24 | |
| = | **Eligible capital** | INS600 L26 | |

**[INTERP] DAC under IFRS 17.** Insurance acquisition cash flows are mostly inside the LRC, not a separate DAC asset. So the DAC deduction mainly bites on:
- deferred takaful acquisition costs (INS100 L88);
- any separately recognised IACF asset (INS400.x column "Assets for IACF").

**VERIFY** whether QFCRA expects IACF assets to be deducted.

## 3. Mapping the RBC inputs to IFRS 17 balances [INTERP; VERIFY with the return instructions]
| RBC input (Schedule 3) | Nearest IFRS 17 figure | Gap to watch |
|---|---|---|
| **Net premium liability** (8.6.7: value of future claims and settlement costs on in-force cover, net of expected recoveries) | LRC excluding loss component, plus loss component, less ARC | **Not the same concept.** PAA LRC = unearned premium less IACF; GMM LRC = PV future cash flows + RA + CSM. Premium liability is an expected-claims measure. Use the actuarial premium liability (UPR × expected loss and expense ratio, or GMM future outflows for remaining coverage), not the LRC carrying amount, unless the instructions say otherwise |
| **Net outstanding claims** (8.6.8) | LIC (PV future cash flows + RA) less AIC on reinsurance held | Close match. Includes RA and discounting under IFRS 17 |
| Reinsurance assets (asset risk) | Reinsurance contract assets (ARC + AIC), INS100 L55, by reinsurer | Split by reinsurer grade and supervision; INS340 lists the largest |
| Unpaid premiums by age | Premium receivables inside the LRC (IFRS 17 nets them into contract balances) | Use the ageing in INS300 Layout 2 (not yet due-90 / 91-180 / 180+ days) to fill the ≤ 6 m / > 6 m buckets |
| GWP over 12 months (ORR) | No GWP line in IFRS 17 revenue | Use INS300 (gross written by line of business, 4 quarters), not insurance revenue |
| Gross technical provisions (ORR) | Insurance contract liabilities gross (LRC + LIC), INS100 L98 | Includes CSM and RA [INTERP] |
| Long-term provisions | GMM/VFA LRC + LIC for long-term contracts | Whether CSM is included in the 3% base: **VERIFY** |
| Capital at risk | Sums assured − reserves − reinsurance | Not an IFRS 17 figure; comes from policy data |

[TEMPLATE] IFRS 17 disclosure forms. These are not linked to RBC; use them to cross-check:
- **SCOPEOFFILING**: PAA / GMM / VFA in use;
- **INS400.10-.50**: LRC/LIC roll-forwards, issued and held;
- **INS410.x**: CSM roll-forwards;
- **INS500/510**: by portfolio, with RA method and percentile, discount approach, coverage units, OCI option;
- **INS520**: CSM run-off by bucket;
- **INS530**: cash reconciliation to INS400;
- **INS540**: new business at initial recognition.

## 4. Accounting vs capital effects of common actions [INTERP]
| Action | IFRS 17 (P&L / equity) | QFC capital |
|---|---|---|
| Medical QS (PAA) | Reinsurance held: allocation of premium vs recoveries in net expense from reinsurance. Ceding commission reduces the allocated premium. Equity changes only by the expected net cost | RBC falls with net liabilities (file 32 §2). Eligible capital is reduced by the expected net reinsurance cost, as reflected in IFRS equity |
| Onerous group recognised | Loss component hits P&L at once and reduces equity | Eligible capital falls one-for-one. Premium risk is on net premium liability, which includes the deficiency |
| Loss-recovery component on reinsurance held (66A-66B) | Offsets onerous losses on the underlying | Restores equity, so eligible capital is restored |
| LPT / ADC with price above the ceded best estimate | Day-1 cost recognised immediately (retroactive cover; core file 00) | Eligible capital falls by the cost; outstanding-claims risk and ORR (via cap) fall |
| Higher RA confidence level | Lower equity; RA releases later | Eligible capital falls now. Claims charge rises slightly (the base includes RA) |
| GMM vs PAA choice | CSM defers profit | Deferred profit is not capital. GMM business typically shows lower eligible capital than PAA early in a cohort |
| Discount-rate changes (OCI option) | P&L or OCI | Eligible capital moves, subject to how OCI reserves are tiered (VERIFY) |
| Interim profit | In equity at the quarter end | Excluded until externally verified, so quarter-end SRR cover lags |
| Dividend declared | Reduces equity | Reduces tier 1. Report within 15 business days. If it exceeds the year's earnings it is a tier 1 reduction needing approval (4.8.1 guidance) |


<!-- ===== FILE: references/qa-qfc/39-qfc-source-register.md ===== -->

# Qatar (QFC) layer: source register and open verification points

QFC layer version 1.0, compiled 9 Nov 2026. It covers **QFCRA-authorised insurers only**. The onshore QCB regime is not loaded.

## Primary sources used
| # | Source | Date / version | Used for |
|---|---|---|---|
| Q1 | QFCRA Insurance Business Rules 2006 (PINS), Version 20 (file QFCRA_4538_VER20) | Effective 1 Oct 2025; includes QFCRA Rules 2024-4 and 2025-1 | Ch 1-6, 8-12; Schedule 3 (all RBC factors); glossary |
| Q2 | QFCRA insurance prudential return workbook, structural and formula extraction (XBRL taxonomy `QFCRA_INS` 2.0.0, 2025 namespace; Q3 2026 specimen with no data) | Q3 2026 | INS600/INS610.x formulas, INS620, scope flags, disclosure-form layout, template vs rule differences (file 31 §6) |
| Q3 | IFRS 17 Insurance Contracts, including the 2020 amendments | Effective 1 Jan 2023 | File 33 |
| Q4 | Public reporting on QCB Governor Decision 1/2016 (Gulf Times, Peninsula, MEIR, Al Tamimi practice guide) | 2016-2026 | Perimeter note only (file 30 §1); not a rule source |

## Open points to VERIFY before relying on them in client work
1. **Return instructions.** Get the QFCRA completion guidance for the INS return. It is the likely source of:
   - the 2 × largest-retention concentration fallback;
   - the derivative add-on treatment;
   - the definitions of the premium-liability and outstanding-claims inputs under IFRS 17;
   - the treatment of OCI reserves.
2. **FSR Schedule 3, Part 3, para 10.3.** Confirm the names of general insurance categories 3-18 behind PINS categories 2-4.
3. **Long-term provisions.** Is the 0.5-3% charge applied gross or net of reinsurance, and does it include CSM?
4. **Eligible capital.** How are reserves other than retained earnings treated: FVOCI, insurance finance, hedging, revaluation?
5. **Inadmissible assets.** Are right-of-use assets "tangible fixed assets"? Are IACF assets deducted as DAC?
6. **Reinsurance governance.** Do any QFCRA rules or notices outside PINS impose a rating floor, cession limits or finite-risk restrictions? Check CTRL, GENE, COND and the Islamic finance rules.
7. **IAIS MMoU signatory list** on the date of use, for the supervised / unsupervised reinsurer factor.
8. **Firm-specific SRR or MCR conditions.** Any insurer-specific SRR set under 3.3.2A(3), or an MCR imposed as a licence condition.
9. **Which returns are in force** (annual, biannual, quarterly) per the current notice under 1.4.1.
10. **Onshore Qatar.** Load QCB Decision 1/2016 and its solvency annexes and returns before answering for any QCB-licensed insurer.

## Maintenance rule
When a source is updated:
- change the affected rows in files 30-33;
- bump the layer version;
- add the new source here with its date;
- move resolved VERIFY items into the main text with their citation.

## Load-test questions (expected answer in brackets)
- **Q1.** A QFC LLC medical insurer has RBC of QAR 20m and eligible capital of QAR 38m. Is it compliant, and does a 30% QS help?
  - [Yes: MCR = 36m (floor) and SRR = 30m, so the floor binds. A QS cuts RBC but creates no headroom, because the 36m floor still binds.]
- **Q2.** What is the premium-risk factor for direct medical business, and can it be lowered?
  - [PINS cat 1: 16% of net premium liability. Can be lowered on application with morbidity data to no less than 12% (A3.7.3).]
- **Q3.** What does ceding to an A-rated reinsurer domiciled in a non-MMoU jurisdiction cost?
  - [4.8% of the reinsurance asset vs 4% if supervised by a subrule (2) regulator.]
- **Q4.** INS610 L20 is positive. Is the insurer necessarily compliant?
  - [No. L20 is eligible − MCR. The SRR (eligible ≥ 150% × RBC) must be checked separately.]
- **Q5.** A Qatari insurer licensed by QCB asks about its SRR.
  - [The QFC layer does not apply; no QCB layer is loaded.]


<!-- ===== FILE: references/templates/jurisdiction-overlay-template.md ===== -->

# Template: building a new jurisdiction overlay (KSA, Qatar, Oman, Bahrain, Kuwait, Egypt, Jordan ...)

Create the folder `references/<country-code>/` with the five files below, numbered like the UAE layer. Keep each file under ~8k tokens, so that one overlay plus the core files stays well within what LenAI can load at once. Use the same tags: [RULE], [TEMPLATE], [INTERP], VERIFY.

## x0-<cc>-legal-framework.md
- **Regulator(s)** and perimeter, including free zones excluded (e.g. QFC in Qatar, the KSA special zones if any).
- **Primary law(s), with the articles on:**
  - licensing, legal form and minimum capital;
  - technical provisions and solvency delegation;
  - reinsurance rules (local cession requirements, rating floors);
  - portfolio transfers;
  - intervention, resolution and creditor ranking;
  - dividends.
- **Table of instruments in force,** with effective dates.
- **Governance hooks:** actuary, ORSA or FCR, retention plan, board reporting.
- **Takaful or cooperative model specifics:** for KSA, the cooperative insurance surplus split and the cooperative law.

## x1-<cc>-solvency-requirements.md
- **Requirement layers** and which capital tier covers each.
- **Own-funds definition,** tiers and limits; admissibility.
- **Liability basis** for solvency (statutory or IFRS 17-based).
- **Formula, module by module:** factors, floors on net/gross, correlations, operational risk, catastrophe.
- **Breach ladder and timelines;** reporting and disclosure.
- **A worked example** in the same format as UAE file 11 §8.

## x2-<cc>-reinsurance-rules.md
- **Cession rules:**
  - local retention or cession quotas (KSA, for example, has local-cession requirements);
  - rating floors;
  - prohibited or finite structures;
  - approvals.
- **Capital credit by structure:** same table as UAE file 12 §2.
- **Screening checklist** adapted to local rules.

## x3-<cc>-ifrs17-bridge.md
- **Is the regulatory basis IFRS 17-based?** If yes, which adjustments (e.g. CSM treated as own funds or as a liability, RA recalibration)?
- **Line-by-line bridge table** and a practical equity-to-own-funds bridge.
- **Premium measures used** by the formula vs what IFRS 17 shows.
- **Accounting vs capital effects of common actions:** same table as UAE file 13 §5.

## x9-<cc>-source-register.md
- Sources with dates, an open VERIFY list, and the maintenance rule.

## When the overlay is added
1. Add the files to the routing table in SKILL.md §2.
2. Add any country-specific guardrail to SKILL.md §4.
3. Keep the core files jurisdiction-neutral. Move anything country-specific out of them.
4. Bump the skill version and note the overlay in the description line.


<!-- ===== FILE: references/uae/10-uae-legal-framework.md ===== -->

# UAE (onshore, CBUAE): legal and regulatory framework

As at: CBUAE Rulebook insurance-section export of 20 Oct 2026; Federal Decree-Law No. 6 of 2025.

Not covered: DIFC (regulated by the DFSA) and ADGM (regulated by the FSRA). Decree-Law 6/2025 does not apply to financial free zones (Art 2).

## 1. Regulator and the instrument hierarchy
1. **Federal Decree-Law No. 6 of 2025** regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business ("CB Law").
   - Issued 8 Sep 2025; in force from 16 Sep 2025.
   - It repeals Decretal Federal Law 14/2018 and Federal Decree-Law 48/2023 (insurance) (Art 185).
   - Insurance is a Licensed Financial Activity (Art 61(1)(j)) supervised by the CBUAE.
2. **Carried-forward instruments [RULE].** Regulations, decisions and circulars issued under the repealed laws stay in force until replaced (Art 183). This is why Insurance Authority (IA) Board decisions from 2014-2020 still govern solvency, reserving and reinsurance.
3. **Conformity window.** Persons subject to the CB Law had one year from entry into force to reconcile their positions, i.e. to about mid-September 2026. The Board may extend this (Art 184).
4. **CBUAE regulations, standards and notices** issued since the IA merged into the CBUAE, published in the Rulebook (Art 131).

## 2. CB Law articles that drive capital and reinsurance work [RULE]
| Art | Content | Why it matters |
|---|---|---|
| 69 | (Re)insurers must be public joint-stock companies (branches of foreign companies exempt per Board rules) | Capital-raising route |
| 70 | Board sets minimum capital and risk-based capital requirements, and the actions on shortfall | Basis for future solvency reform |
| 78, 80 | Two types: insurance of persons and fund accumulation (life, health) vs property and liability. New companies cannot combine them. Existing composites continue with complete technical, financial, IT, administrative and legal separation, and report consolidated and separately | Separate funds and separate investment portfolios |
| 82 | UAE risks must be insured with UAE-licensed insurers (exceptions where cover is unavailable). 82(2): an insurer may reinsure with reinsurers inside or outside the State or in a financial free zone | Offshore reinsurance permitted |
| 86 | Technical provisions, solvency margin and reserves as determined by the CBUAE, maintained in the State | Gateway to Decision 25/2014 |
| 87 | Appoint an actuary within one month of licensing | |
| 92 | Cash guarantee deposit with the CBUAE; replenish within 30 days if drawn | |
| 93 | Life companies keep funds in the State at least equal to the full mathematical reserve for contracts concluded or executed in the State, separate from other funds | Localisation of life assets |
| 94 | Reinsure only with a company licensed for that insurance type | |
| 95 | Foreign branches give an irrevocable bank guarantee; the CBUAE may count it as an acceptable asset for solvency | |
| 97-99 | Life: quarterly actuarial assessment of liabilities; actuary report within 3 months (+45 days); dividends only from the surplus certified by the actuary and approved by the CBUAE | Distribution constraint on life |
| 101-102 | Portfolio transfer: application, newspaper publication, 10 business days for objections, CBUAE approval if no adverse effect on either party | Portfolio/LPT-style deals |
| 104-105 | A takaful fund has independent legal personality and financial liability, is registered with and supervised by the CBUAE, and has its own articles | Takaful structure |
| 120-121 | Prior approval for controlling interests, and for branches or subsidiaries inside or outside the State | M&A, group structures |
| 124(3) | Financial position cannot go to the general assembly before CBUAE approval | Dividend and results timing |
| 125(1) | No merger or acquisition, nor transfer of **any part of its liabilities** to another person, without prior CBUAE approval | LPT, ADC, portfolio deals: pre-clear [INTERP whether it reaches ordinary reinsurance] |
| 128 | Board can issue prudential instructions on capital adequacy, liquidity and limits to an institution or a category | |
| 140(2) | CBUAE may refuse proposed dividends where provisions fall short, capital adequacy is below minimum, or there are auditor reservations | |
| 142 | Early intervention when a breach is likely. Insurer-specific (142(2)): suspend new business; cap premiums; ring-fence assets in the State; restrict solvency-related investments; **stop distributions on, and repurchases of, own-fund instruments**; suspend or revoke licence; restructure; liquidate | Consequences of a solvency breach |
| 143(10) | Resolution powers for (re)insurers, including writing down or converting insurance liabilities, portfolio transfer with associated reinsurance, run-off | |
| 144 | Creditor ranking in resolution: secured creditors, then 6 months' wages, then resolution costs, then **policyholders and beneficiaries** (technical provisions and related reinsurance collections allocated to them), then other creditors, then shareholders | Counterparty view of a weak cedant |
| 168 | Sanctions, including fines up to AED 1bn, bans on new contracts, premium caps, investment restrictions | |

The CBUAE has used new-business bans and line suspensions against insurers that breached solvency requirements. Treat a persistent breach as a commercial risk to treaty volumes.

## 3. Instruments in force that matter here (from the Rulebook export)
| Instrument | Effective | Subject |
|---|---|---|
| IA Board Decision 25/2014: Financial Regulations for Insurance Companies | 28 Dec 2014 | Investments (S1), solvency (S2), technical provisions (S3), asset valuation (S4), records (S5-6), accounts (S7) |
| IA Board Decision 26/2014: Financial Regulations for Takaful Insurance Companies | 28 Dec 2014 | Takaful equivalent of 25/2014 |
| IA eForms v1.7 (Financial Reporting Forms and User Instructions) | IA era; VERIFY the current version | The solvency template (SM-1 to SM-6) and regulatory returns |
| IA Board Decision 22/2017: application of investment limits | 17 Jul 2017 | Assets outside limits are not admissible; separate limits for associates |
| IA Board Decision 14/2018: solvency of foreign branches | 23 Jul 2018 | Parent net book value; guarantees |
| IA Board Decision 23/2019: Reinsurance Operations | 31 May 2019 | Finite ban, rating floor, retention plan, 0.5% provision (see file 12) |
| IA Board Decision 49/2019: life insurance and family takaful instructions | 9 Oct 2019 | Commission limits, churning, **actuarial funding not allowed** (technical provisions by cash allocation for initial units on unit-linked) |
| IA Board Decision 9/2017: licensing of actuaries | 28 Apr 2017 | |
| IA Board Decision 19/2020: guidance manual for supervisory reports | 31 Jul 2020 | Reporting manual referenced by later regulations |
| Cabinet Resolution 42/2009 (amended by 16/2017): minimum capital | | Paid-up capital floors |
| Corporate Governance Regulation (Circular 24/2022) | 2022 | Board duties; financial reporting and external audit governance (Art 9) |
| Risk Management and Internal Controls Regulation (Circular 25/2022) | 30 Dec 2022 | Key control functions; **independent actuarial function** (Art 10); written annual actuarial report to the Board |
| Financial Reporting and External Audit Regulation (C 5/2023) | 30 Apr 2024 | IFRS plus CBUAE instructions (2-10); valuation governance (2-11); **no distribution or repatriation of profits or regulatory capital without prior CBUAE no-objection** (2-7, 2-8); audit-firm rotation every 6 years, partner every 3 |
| Regulation Regarding Takaful Insurance (new) | 14 Sep 2026 | Supersedes the 2022 regulation (Art 28.1) |
| Takaful Insurance Operational Model Standard; Fund establishment standard | 15 Jul 2027 | Qard hasan mechanics, fund operations |
| Insurance Company Licensing Regulation (C 4/2026) | 14 Aug 2026 | Licensing framework; lists the instruments to read alongside |
| Representation Offices of foreign (re)insurers (C 1/2025) | Issued 13 Feb 2025 | |

## 4. Governance and process duties that create advisory hooks
- **Board-approved 3-year retention and reinsurance plan**, reviewed annually in the 3 months before each year (Decision 23/2019 Art 27). See file 12.
- **Investment governance** (Decision 25/2014 S1):
  - an investment committee (Art 1(3); Addendum 2);
  - an investment policy approved annually by the Board (Art 2(1));
  - stress testing at least annually (Art 2(5));
  - a contingency funding plan (Art 2(9));
  - quarterly and annual investment reporting (Art 10).
- **Actuary.**
  - Certifies technical provisions quarterly and annually.
  - Certifies the SCR quarterly.
  - Gives the regulator an annual report on immediate or future risks; the external auditor reviews it and gives its opinion to the regulator (S3 Art 4(5)-(6)).
  - Reports such risks directly to the Board on a timely basis; the Board forwards its recommendations to the regulator (S6 Art 4(4)).
  - Sources for the certification duties: 25/2014 S2 Art 9; S3 Arts 4-5.
  - The actuarial function must be independent (Circular 25/2022 Art 10).
- **Financial Condition Report** when required by the regulator (25/2014 S2 Art 10). It covers:
  - certification of technical provisions;
  - investment risk;
  - SCR analysis;
  - reinsurance structure;
  - underwriting;
  - pricing;
  - ERM.
- **ORSA [RULE]** (Circular 25/2022 Art 3(5)). The ORSA is run by the risk-management function and covers:
  - overall solvency needs;
  - ongoing compliance with the capital and technical-provision requirements;
  - how far the risk profile deviates from the SCR standard-formula assumptions.

  Results go to the CBUAE together with the annual business plan, on the CBUAE timetable. The first submissions were for YE2023, per notice 6163.
- **Dividends:** prior CBUAE no-objection (C 5/2023 2-7, 2-8). Life dividends are limited to the actuary-certified surplus (CB Law Art 99).

## 5. Takaful: structural rules that change the capital story
Sources: CB Law Arts 104-105; Regulation Regarding Takaful Insurance (in force from 14 Sep 2026); Takaful Operational Model Standard (effective 15 Jul 2027); Decision 26/2014.
- **Two pockets.**
  - The Takaful Insurance Fund (participants) is legally separate.
  - The shareholders' account earns the wakala fee and any mudaraba share. The wakala fee is set annually, approved by the Internal Shari'ah Supervision Committee, and subject to CBUAE limits.
- **Surplus.**
  - Distributed per an approved policy, after actuary approval and CBUAE approval.
  - The fund may grant 10% of surplus to the company for sound management. This must be stated in the Participation Membership Policy and decided when the surplus is achieved (Reg Art 20.5).
- **Qard hasan [RULE].**
  - If fund assets are insufficient, the shareholders must lend qard hasan to the fund, up to total shareholders' equity (Reg Art 21.1-21.2).
  - It is recoverable only from future surplus (21.3). Failure to provide it within 15 days of notification can lead to suspension (21.4).
  - The Operational Model Standard requires an unrecoverable qard to be written off in full three years after maturity (Std 18.6, from 2027).
- **Retakaful.**
  - Cede to retakaful or takaful companies.
  - Conventional reinsurers may be used where capacity is inadequate or for spread, under CBUAE standards (Reg Art 22.2).
  - **Reinsurance commissions must go to the fund, not the shareholders' account** (Reg Art 22.3). The eForms instructions say the same: ceded commissions only in the participants' fund.
- **Solvency** is assessed at company level on a consolidated basis (shareholders' account plus fund) under Decision 26/2014. Where a fund is in recurring deficit or relies on qard hasan, the CBUAE may require a separate fund-level assessment (Reg Art 24).
- **Implications [INTERP].**
  - Commission-based or financing reinsurance at a takaful operator improves the fund, not shareholders' P&L.
  - The shareholders benefit only through surplus share or qard repayment.
  - Shareholder capital is exposed through the qard obligation even though the fund is legally separate.


<!-- ===== FILE: references/uae/11-uae-solvency-template.md ===== -->

# UAE: solvency requirements, own funds, technical provisions and the solvency template

**Sources.**
- **[RULE]:** IA Board Decision 25/2014, Financial Regulations for Insurance Companies (S1-S4). Decision 26/2014 is the takaful twin with the same architecture.
- **[TEMPLATE]:** IA Financial Reporting eForms v1.7 and its User Instructions. Factors were verified against the v1.7 workbook formulas in Oct 2026.
- **VERIFY** which eForms version the company currently files before relying on a factor.

## 1. Architecture [RULE]
- **Solvency Margin.** The company must at all times hold own funds at least equal to the **largest of MCR, MGF and SCR** (S2 Art 8(1)).
- **MCR.** Minimum paid-up capital: **AED 100m for an insurer, AED 250m for a reinsurer** (S2 Art 1).
- **MGF.** At least ⅓ of SCR. It is built per type of business as the greater of an absolute minimum and a percentage of net earned premium or similar measure (S2 Art 2).
- **SCR** (S2 Art 4):
  - calibrated to the **99.5% one-year VaR of Basic Own Funds**, on a going-concern basis;
  - covers existing business plus new business expected over the next 12 months;
  - covers four risks: underwriting, market and liquidity (investment), credit, and operational;
  - calculated with the regulator's solvency template.
- **Level of calculation** (S2 Art 4(3)):
  - UAE level for branches of foreign (re)insurers;
  - group level for UAE companies with branches or subsidiaries abroad;
  - UAE level for all other companies.
  - Group requirement = sum of the consolidated insurers' requirements plus those of other regulated entities (Art 3).

## 2. Own funds [RULE]
**Basic Own Funds (BOF)** (S2 Art 7(2)):
- admissible assets less liabilities;
- **less treasury shares**;
- **plus subordinated liabilities**, which means **group-level debt in a holding company, with prior approval**.

**Ancillary Own Funds (AOF)** (Art 7(3)-(5)):
- what can count:
  - uncalled share capital;
  - **letters of credit and guarantees**;
  - other legally binding commitments receivable;
- conditions and treatment:
  - **prior approval** is required;
  - once called or paid, the item becomes an asset and leaves AOF;
- **[TEMPLATE]** in the eForms:
  - AOF lines are locked and unlocked by the regulator on approval;
  - funds must be restricted to UAE policyholder protection, and release needs approval;
  - v1.7 added an AOF line for **excess subordinated liabilities**.

**Eligibility** (Art 7(6)-(7)):
- the **MCR must be met 100% by BOF**;
- **SCR and MGF** are met by BOF plus **50% of AOF**.

**Borrowed funds** (bank loans, other debt) may not be used to invest for covering gross technical provisions, MCR, MGF or SCR (S1 Art 9). Surplus bonds issued in lieu of shares are excluded from this ban.
- **[INTERP]** A reinsurer-provided loan does not become own funds unless it is structured and approved as a qualifying subordinated or ancillary item.

**Admissibility** (S2 Art 11; S4 Art 2):
- invested assets count only within the S1 investment limits;
- other assets are valued "as required by the Authority".
- IA Decision 22/2017: assets outside the limits are **not admissible**.

## 3. The template, form by form [TEMPLATE, eForms v1.7]
### SM-1 Aggregation
- **SCR = BSCR + operational risk.**
- **BSCR = √(xᵀ C x)** over five modules: Non-life, Life, Health, Market, Credit.
- **Correlations:**
  - Non-life–Credit 0.50;
  - Non-life with Life, Health and Market 0;
  - every other pair 0.25.

### SM-2(H) Health underwriting
Segments: Individual, Group, and Non-proportional assumed.

| Sub-risk | Formula |
|---|---|
| Premium risk | gross written premium (last 12 months) × **max(net/gross, 50%)** × 5% (non-proportional assumed: 15%) |
| Reserve risk | gross technical provisions × **max(net/gross, 50%)** × 5% (non-proportional assumed: 20%) |
| Premium-reserve correlation; between segments | 0.5; 0.5 |
| Catastrophe | **net written premium × (1% mass accident + 1% accident concentration + 2% pandemic)** for UAE business. Higher factors for GCC, MENA and rest of world; regions combined by sum of squares |
| Lapse | 40% × expected profit in future business, with the profit ratio capped at 25% |
| Within-health correlations | premium/reserve with cat 0.25; lapse 0 |

**Implications [INTERP]:**
- **Cession beyond 50% earns no premium or reserve SCR credit.** Fronted gross premium still attracts charge at the 50% floor.
- **XoL and stop loss earn almost nothing.** They barely change net/gross.
- The only health SCR item that keeps falling with cession is catastrophe, because it is on net premium.

### SM-2(NL) Non-life underwriting
Same structure as health.
- **Net/gross floors:** 50% for fire, motor, liability and miscellaneous; 25% for marine, aviation, engineering and energy.
- **Premium factors:**
  - motor comprehensive 8%;
  - motor TPL 10%;
  - commercial motor 10%;
  - fire 8-10%;
  - marine and aviation 15%;
  - engineering and energy 17%;
  - miscellaneous 6%.
- **Reserve factors:** 8-16%.

### SM-2(L) Life underwriting
- **Group life (and group credit life) with term up to 1 year:**
  - premium risk 2%, reserve risk 1%;
  - **net/gross floor 85%**, so ceding more than 15% earns no premium or reserve credit.
- **Long-term life:** Solvency II-style shocks applied to **net** technical provisions. v1.7 corrected these from gross to net.
  - Sub-modules: mortality, longevity, morbidity, expense, lapse, catastrophe.
  - Non-unit reserves of unit-linked business (form LT-4 less LT-5) are included.
  - Mortality shocks can reduce the SCR where values are negative.
  - **No floor.** This is the one place a life quota share or coinsurance moves SCR materially.
  - Shock factors: read SM-2(L) of the version filed. They are not reproduced here.

### SM-3 Market (on admissible values)
| Sub-risk | Charge |
|---|---|
| Equity | listed 20%, unlisted 30% |
| Real estate | developed 20% (a cash-flow value is allowed for rented property); undeveloped 27.5%; under development 40% |
| Spread | factor by rating × duration |
| Concentration | thresholds: 3% of assets for issuers rated AAA-A, 1.5% for BBB and below. Excess charged at 12% (AAA-AA), 21% (A), 27% (BBB-BB), 73% (B or unrated) |
| Currency | net mismatch × 5% (MENA excluding GCC), 10% (rest of world) |
| Interest rate | uses the actuary's valuation discount rate (SM-3 line 17) and undiscounted liability cash flows (TP-12) against asset cash flows (INV-5). v1.7 allows a yield curve for life |

Correlations:
- interest rate with others 0.5;
- real estate–equity 0.75;
- equity–spread 0.5;
- concentration 0;
- currency 0.25.

### SM-4 Credit (counterparty)
**Reinsurance recoverables, derivatives, cash and other counterparties:**
- charge = **50% × (exposure − 80% × collateral) × probability of default (PD)**;
- PD by rating:
  - AAA 0.002%;
  - AA 0.01%;
  - A 0.05%;
  - BBB 0.24%;
  - BB 1.2%;
  - B or unrated 4.175%.
- Negligible for A-rated reinsurers.

**Receivables:**
- **within 3 months 15%**;
- **over 3 months 90%**;
- mortgages 100%.

**Aggregation:** √((reinsurance + derivatives + cash)² + receivables²).

### SM-5 Operational risk
- **Charge:** the higher of:
  - 5% × gross earned premium; and
  - technical-provision factors: 3% non-life, 0.5% life, 3% health.
- **Growth load:** added where premium growth exceeds 20%. v1.7 added limits to the growth component.
- **Cap:** 30% of BSCR.
- **Calculated on gross figures,** so reinsurance does not reduce it.

### SM-6 Minimum Guarantee Fund
- **Non-life and health:** net earned premium × factor, with a minimum amount per line.
  - Health 26%, minimum AED 3m.
  - Motor and fire 26-31%.
  - Marine, aviation, engineering and energy 31-36%.
  - v1.7 moved health into this section and added all-business rows based on the top 5 segments.
- **Life:** net sum at risk × 0.2-0.4%, minimum AED 1-1.5m.
- **MGF = max(sum of the above, ⅓ × SCR).**
- **It runs on NET premium with no floor**, so quota share reduces MGF dirham for dirham at the line factor.

### REINS-2 Admissibility of reinsurance receivables (aging from invoice date)
- **UAE reinsurers:** 100% up to 180 days; 75% at 181-270; 50% at 271-360; 0% after 360.
- **Outside the UAE:** 100% up to 90 days; 75% at 91-180; 50% at 181-270; 25% at 271-360; 0% after 360.

Slow technical-account settlement therefore destroys admissible assets. Put settlement terms in treaty design.

## 4. Statutory technical provisions [RULE] (S3 and Addendums)
These are the regulatory-basis reserves, distinct from the IFRS 17 LRC and LIC.

**Types** (Art 1): UPR, URR, OSLR, IBNR (including IBNER), ALAE/ULAE, mathematical reserve.

**UPR** (Art 3(1)):
- **linear pro-rata of gross premium** from risk inception;
- a larger reserve where risk is non-uniform (e.g. engineering);
- marine cargo (individual shipments) at least 25% of premium.

**URR:** by line where the UPR is inadequate. It must consider the cost of capital or other profit loadings.

**OSLR, IBNR and LAE:**
- actuary-certified at least annually;
- IBNR estimated by accident or underwriting year;
- **negative IBNR in total** is allowed only if actuarially justified, and **is never an admissible asset** (Add. 1).

**Mathematical reserve** (Add. 2):
- prospective, contract by contract;
- **prudent assumptions with margins for adverse deviation**;
- **negative reserves set to zero, or to the guaranteed surrender value**;
- unit-linked: mathematical reserve plus unit reserve must be at least the guaranteed surrender value;
- **no allowance for lapses where that would reduce the liability**;
- discounting on AAA sovereign yields, with USD AAA yields for long AED durations;
- unit-linked fund reserves are **excluded from technical provisions for solvency, except the guaranteed portion** (§19).

**Reinsurance** (Art 3(6)): technical provisions are computed gross and net of all applicable reinsurance. The actuary reviews both (Art 4).

**Localisation** (Art 2): investments equal to the following must be held in the UAE:
- **gross** UPR, URR and mathematical reserves; and
- **net** OSLR, IBNR and LAE.

Unit-linked is excluded from this requirement.

**Unit-linked** (IA Decision 49/2019): **actuarial funding is not allowed**. Provisions are by cash allocation for initial units.

## 5. Asset valuation and investment limits [RULE]
**Valuation** (S4 Addendum):
- listed securities at the lower of closing or latest quotation;
- unlisted at fair value (IFRS 13), or NAV if immaterial;
- **real estate:** market value by an independent qualified expert for admissible-asset purposes (S4 Add. 2(a)). The number of valuers is set in S1 Addendum 1(h): one below AED 30m, two above, and no valuer used for two consecutive periods;
- **real estate for the solvency margin: a discounted cash-flow basis.** Rental income over at most 30 years, net of vacancy, no inflation, discounted at the risk-free rate (S1 Add. 1(i)). Land and work in progress with no rent therefore have little or no solvency value [INTERP].
- **advance commission (DAC) valued at nil**, except first-year long-term life;
- (re)insurance balances at expected recoverable amounts, with impairment.

**Asset allocation limits** (S1 Art 3, applied to total invested assets; unit-linked excluded):

| Asset | Aggregate max | Single counterparty |
|---|---|---|
| Real estate | 30% (up to 40% with approval) | — |
| Equity, UAE (listed and unlisted) | 30% | 10% |
| Equity, outside UAE | 20% | 10% |
| UAE federal/emirate government | 100% | 25% |
| A-rated sovereigns | 80% | 25% |
| Cash and deposits with UAE banks | **minimum 5%** | 50% |
| Policy loans | 30% | — |
| Derivatives (hedging only) | 1% (more for FX hedging) | — |
| Rated (A or better) debt, secured loans, non-bank deposits | 30% | 20% |
| Other invested assets | 10% | — |
| Associates (IA Decision 22/2017) | 20% in UAE / 10% outside, separate category | — |

**Domicile** (S1 Art 6): assets held outside the UAE may not exceed the greater of 50% of total invested assets and 100% of technical provisions for policies outside the UAE.

## 6. Breach, recovery and reporting [RULE] (S2 Arts 8-9)
**MCR or SCR breach:**
- report immediately;
- recovery plan within **30 days**;
- compliance within **6 months** of observation.

**MGF breach:** plan within 30 days; compliance within **3 months**.

**Extension:** up to **3 months** in exceptional circumstances.

**Progress reports:** every 30 days (SCR/MGF), or as set by the regulator (MCR).

**Failure:** escalation to the regulator's Board for action "as per the Law's stipulations" (S2 Art 8(7)). Today that most likely means CB Law Art 142 [INTERP].

**Reporting:**
- **annual** solvency template certified by the actuary and the auditor, endorsed by the chairman:
  - within 4 months of year-end;
  - and at least 30 days before the general assembly invitation;
- **quarterly SCR** certified by the actuary within **45 days**;
- quarterly technical provisions within 45 days.

**Public disclosure:**
- the IFRS accounts disclose MCR, SCR, MGF, BOF and AOF with surplus or deficit (S7 note 3.11 template);
- listed insurers publish their latest solvency position, or the prior quarter's where the current one is not available (as observed in market practice since 2024; per the project notes, a CBUAE circular allowing a one-quarter lag). VERIFY the circular reference.

## 7. Foreign branches and takaful
- **Foreign branches** (IA Decision 14/2018) may rely on the parent's net book value only with one of:
  - funds transferred to the UAE;
  - a UAE bank guarantee;
  - another approved restricted guarantee.

  They must also file home-country solvency evidence annually. Combine this with the CB Law Art 95 guarantee.
- **Takaful:**
  - Decision 26/2014 applies the same template at company level, consolidated across the shareholders' account and the takaful fund (Takaful Regulation Art 24);
  - the regulator may require a separate fund assessment;
  - see file 10 §5.

## 8. Worked example (illustrative numbers, AED m, health only, diversification with other modules ignored)
**Inputs:**
- group medical gross written premium 400, ceded 60% (net/gross 40%);
- gross technical provisions 150;
- net written premium ≈ net earned premium = 160.

**Calculation:**
- **Premium risk** = 400 × max(0.40, 0.50) × 5% = **10.0**.
- **Reserve risk** = 150 × 0.50 × 5% = **3.75**.
- **Premium and reserve combined** = √(10² + 3.75² + 2×0.5×10×3.75) = √151.56 = **12.31**.
- **Catastrophe** = 160 × 4% = **6.40**.
- **Health underwriting** = √(12.31² + 6.40² + 2×0.25×12.31×6.40) = √231.9 = **15.23**.
- **MGF (health)** = 160 × 26% = **41.6**.

**Same company at 50% retention:**
- premium and reserve risk are unchanged (floor), so still 12.31;
- catastrophe = 200 × 4% = 8.0;
- health underwriting = **16.27** (+1.04);
- **MGF = 200 × 26% = 52.0 (+10.4)**.

**Reading [INTERP]:**
- The extra 10 points of cession beyond the floor buys almost nothing on SCR, but 10.4 on MGF.
- So size cession to the binding test:
  - if SCR binds, cede down to about 50% and no further;
  - if MGF binds or is about to, extra cession pays dirham for dirham;
  - if the MCR binds, cession does not help; capital or assets do.


<!-- ===== FILE: references/uae/12-uae-reinsurance-rules.md ===== -->

# UAE: reinsurance rules, capital credit by structure, and structured-solution screening

**Sources:**
- **[RULE]:**
  - IA Board Decision 23/2019, Instructions Organizing Reinsurance Operations. In force from 31 May 2019, carried forward by CB Law Art 183, and listed in C 4/2026.
  - CB Law Arts 94, 101-102, 125.
  - Takaful Regulation 2026, Art 22.
- **[TEMPLATE]:** eForms v1.7.

Article numbers below follow the Rulebook export (headings in the export appear after their text). VERIFY wording against the Rulebook before quoting.

## 1. Decision 23/2019: cession by a UAE insurer [RULE]
| Art | Requirement | Practical consequence |
|---|---|---|
| 24 | Cede only to a company licensed by its home regulator for that type and class | Licence check on every panel member |
| **25** | **The relationship may not be "finite reinsurance", where cedant and reinsurer are in a lender-borrower relationship** | A prohibition on the transaction, not a capital haircut. The test is economic substance |
| **26** (with Art 18) | Reinsurers must be rated at least S&P BBB / Moody's Baa / AM Best B+ / Fitch BBB. The rating must be granted on the basis of complete internal information. Ratings based only on published information are not accepted. The reinsurer's **domicile must be rated no lower**. Exempt: UAE-licensed insurers acting as reinsurers, pools and syndicates, and reinsurers exempted by the regulator. Foreign branches file an annual head-office certificate that cessions above retention are with compliant reinsurers | Panel eligibility. Ask for evidence that the rating is a full (non-public-information) rating. Downgrades must be monitored |
| **27** | **Board-approved 3-year retention and reinsurance plan** for each type and class, reviewed annually in the 3 months before the year. Minimum content: (a) retention and treaty limits and facultative; (b) treaty types (QS, surplus, XoL, stop loss); (c) local and foreign facultative and fac-obligatory; (d) **lead and following reinsurers, ratings, accumulation monitoring**; (e) brokers and reasons for selection; (f) accumulation and catastrophe protection; (g) **commissions: flat or variable by loss ratio, profit commissions and their rules** | Sliding-scale and profit commissions are expressly contemplated. The plan is the natural advisory entry point |
| **28** | Treaties must oblige the reinsurer to maintain unearned premium provisions on ceded premium | A UPR or premium-deposit clause. It is a reserving obligation, **not** a licence for the cedant to withhold premium [INTERP] |
| 29 | Unlimited direct liability needs unlimited reinsurance | Motor TPL and similar |
| 30 | Cession to pools needs prior approval; to Lloyd's-type syndicates it does not | |
| 31 | For tenders outside treaty capacity: lead reinsurer approval (rated per Art 18) before bidding; cover complete before inception | Facultative support for large group schemes |
| 32 | A takaful company ceding to a mixed conventional/retakaful reinsurer must require Sharia-compliant provisions | |
| 33 | Management must tell the Board and the regulator immediately of reinsurance problems: incomplete renewals, reinsurer distress or non-payment, uncovered liabilities, exhausted capacity, rating below minimum. The regulator can order the company to stop dealing with a reinsurer | |
| **34** | **Provision of 0.5% of total ceded reinsurance premium every year**, for reinsurer default. It accumulates and cannot be released without written approval (the regulator may stop accruals once adequate) | A permanent own-funds cost of high cession. Include it in treaty economics |
| 35 | Named reinsurance officer; **quarterly reports to the Board** on treaty, cover and facultative results | |
| 36 | Within 30 days of each underwriting year: lead reinsurer, completion-of-cover statement, reinsurer ratings | |
| 37 | **Inward treaty and facultative premium capped at 49% of total underwritten premium**, unless the regulator allows more | Limits a direct insurer's use as inward-fac capacity |

**Related CB Law:**
- **Art 94:** licence-type match.
- **Art 82(2):** offshore reinsurers allowed.
- **Arts 101-102:** portfolio transfer procedure.
- **Art 125(1):** prior approval for transferring any part of liabilities.

**Takaful** (Regulation Art 22):
- retakaful first; conventional reinsurers allowed under standards;
- **reinsurance commissions belong to the fund**.

## 2. Capital credit by structure [TEMPLATE + INTERP]
| Structure | SCR effect | MGF effect | MCR | Other template effects |
|---|---|---|---|---|
| Health QS up to 50% ceded | Premium and reserve risk fall to the floor; cat falls on net | Falls by 26% × the reduction in net earned premium | None | Operational risk unchanged (gross); counterparty charge tiny if rated A or better; 0.5% Art 34 provision |
| Health QS beyond 50% | **No premium or reserve credit**; cat only | **Keeps falling** | None | Same |
| Group life / credit life QS (≤1 yr) | Credit only up to 15% ceded (85% floor) | Small (life MGF on net sum at risk 0.2-0.4%) | None | Capacity and cat are the real value |
| Health or life XoL / stop loss / cat XoL | ≈ nil under the factor formula | ≈ nil | None | P&L volatility, rating view, capacity |
| Long-term life QS or coinsurance | **Full credit**: shocks on net technical provisions | Falls with net sum at risk | None | Coinsurance also gives reserve credit on the ceded mathematical reserve. Risk premium/YRT does not |
| LPT on short-tail reserves | Reserve risk on net (subject to floors) | Small | Indirect: BOF change = release of prudence margin less price | Art 125 approval; IFRS 17 para 65 day-1 loss if price exceeds FCF |
| ADC / aggregate cover above best estimate | Limited | — | BOF up only if the recoverable is valued on the same prudent basis as the gross reserve (VERIFY with the appointed actuary and eForm TP instructions) | Cash-light; passes risk transfer more easily than an LPT |
| Letter of credit / guarantee / uncalled capital (AOF) | Counts 50% towards SCR | Counts 50% towards MGF | **0%** | Prior approval, ring-fenced, locked eForm line |
| Funds withheld by cedant | Same underwriting credit as the underlying cession | Same | — | Reduces the counterparty charge (collateral credit 80%). Finite risk if principal return is guaranteed |
| Reinsurer-provided loan | None unless approved as a qualifying own-funds item. BOF admits only group holding-company subordinated debt with approval; borrowed funds cannot back requirements (S1 Art 9) | — | — | Structure with the regulator first |

## 3. Screening checklist for structured or "capital" reinsurance [INTERP]
1. **Art 25 finite test.** Is the reinsurer's recovery contingent on insurance experience, with a meaningful probability of loss and no recourse beyond the treaty? Run 10-10 and ERD (core file 01 §4) and write a risk-transfer memo.
   - **High risk:**
     - an upfront commission repaid from future profits;
     - VIF monetisation;
     - funds withheld with guaranteed repayment;
     - wide loss corridors or caps;
     - experience accounts returning all losses.
   - **Generally fine:**
     - proportional QS with genuine risk;
     - sliding-scale or profit commissions (Art 27(4)(g));
     - XoL.
2. **Art 125 / Arts 101-102.** Does it transfer liabilities (LPT, portfolio)? Pre-clear.
3. **Arts 24 and 26 panel.** Licence; full-information rating at least BBB-equivalent; domicile rating.
4. **Binding test.** Size the cession to the binding constraint (file 11 §8). Do not sell SCR relief above 50% health or 15% group life.
5. **Hidden costs.**
   - Art 34 provision (0.5% of ceded premium).
   - Operational risk unchanged.
   - Lower future net profit (own-funds build).
   - Settlement aging (REINS-2): put 90- or 180-day settlement terms in the treaty.
6. **IFRS 17 view.** See file 13 §5.
   - Day-1 gains deferred; past-event costs expensed.
   - Commission spread over coverage.
   - Loss-recovery timing for onerous groups.
7. **Takaful.**
   - Commissions go to the fund.
   - Shareholders benefit only through surplus share or qard repayment.
   - Sharia board approval.

## 4. Mechanisms that tested well in prior structuring work (generic, no client data) [INTERP]
- **Standby / coverage-linked quota share tranche.** Cession for the next period steps up by formula if the reported MGF or SCR cover falls below a trigger.
  - Cheap for the cedant and regulator-friendly; it can be written into the Art 27 plan.
  - The reinsurer prices the drawn tranche at a lower commission because draws follow bad years.
- **Solvency-triggered UPR commission facility.** A pre-agreed option to cede unearned premium with a provisional commission and a loss-contingent true-up. It acts as a bridge when coverage drops.
- **Prudence-layer ADC** (attaches at best estimate, exhausts at the statutory reserve).
  - It gives the most BOF per unit of cost and passes risk transfer comfortably, provided the reinsurance asset is valued on the same basis as the gross reserve.
  - The reserve stays with the cedant, so there is no liability transfer.
- **Narrow loss-ratio corridor inside a QS (with top-up above).**
  - Cuts commission leakage on profitable books.
  - Keep it narrow: wide corridors fail risk-transfer and look finite.
- **Convertible life treaty (YRT with an option to convert to coinsurance on a trigger).** A low-cost clause for new protection business; it unlocks reserve credit when needed.
- **QS plus reinsurer-provided capital (subordinated loan).** The only reinsurer-led route to a minimum capital problem. It needs credit structuring, plus regulatory approval of the instrument as own funds; see the borrowed-funds rule.

## 5. DIFC contrast (for routing only)
DIFC insurers are DFSA-regulated, under the Prudential Insurance Business module (PIN), not CBUAE rules.
- DFSA PIN contemplates finite risk reinsurance and capitalises it on the reinsurer side (App 4 A4.12.5).
- It requires risk-transfer evidence for insurance special purpose vehicles (PIN 5.8).

**Onshore UAE is a ban, not a charge.** Never transpose DIFC treatment onshore.


<!-- ===== FILE: references/uae/13-uae-ifrs17-bridge.md ===== -->

# UAE: how IFRS 17 interacts with the regulatory (solvency) basis

## 1. Status: two balance sheets
- **Published financial statements are on IFRS 17 from 1 January 2023**, with 2022 comparatives restated.
  - The legal hooks: IA Decision 25/2014 S7 Art 1 (financial statements per IFRS plus the regulator's forms), and C 5/2023 para 2-10 (IFRS plus CBUAE instructions, which may include guidance on applying specific IFRS in the UAE sector) [RULE].
- **Regulatory reporting stayed on the pre-IFRS 17 basis.** CBUAE annual notice 6163 (15 Dec 2023), as summarised by Milliman (Apr 2024), required:
  - an IFRS 17 actuarial certification of (re)insurance contract assets and liabilities;
  - completion of the eForms **"IFRS 4 to IFRS 17 reconciliation template"** with explanations of material changes;
  - continued regulatory reporting **on the current basis supported by the eForms**. The CBUAE would monitor IFRS 17 accounts and consider adopting IFRS 17 for regulatory reporting later.

  **VERIFY** whether any later notice moved regulatory reporting or the solvency template to an IFRS 17 basis. Until confirmed, assume it has not.
- **Consequence.** Solvency (SM-1 to SM-6) is computed from **statutory technical provisions** (UPR, URR, OSLR, IBNR, LAE, mathematical reserve; file 11 §4) and **admissible assets**. It is not computed from IFRS 17 LRC, LIC and CSM. IFRS 17 equity is not Basic Own Funds.

## 2. Line-by-line bridge [RULE for each basis; INTERP for direction]
| Item | Regulatory basis (Decision 25/2014 + eForms) | IFRS 17 | Typical gap and why |
|---|---|---|---|
| Unexpired cover, short-term | **UPR**: linear pro-rata of gross written premium, plus URR by line if inadequate | **LRC under PAA**: premiums received less IACF (if deferred) less revenue recognised, plus a loss component if onerous (paras 55-58) | IFRS nets premiums **not yet received** into the LRC and deducts deferred IACF. Statutory shows gross UPR, with the receivable as a separate asset subject to aging haircuts and DAC at nil. Compare only after grossing up |
| Incurred claims, short-term | OSLR + IBNR (including IBNER) + ALAE/ULAE, **undiscounted**, actuary-certified, often with implicit prudence | **LIC** = PV of future cash flows + **RA**. Discounting optional if paid within 1 year (para 59(b)) | IFRS can be higher (explicit RA) or lower (discounting, removal of implicit prudence). Claims-development tables show reserve strength |
| Long-term life | **Mathematical reserve**: prudent assumptions with margins, **negative reserves floored at zero or GSV, no lapse credit that lowers the liability**, AAA discount | **GMM**: BEL (can be negative) + RA + **CSM** | Statutory prudence ≈ IFRS RA + CSM, but not equal. IFRS recognises future profit inside the CSM; statutory recognises none (no VIF) |
| Unit-linked | Unit reserves **excluded** from technical provisions for solvency except guaranteed parts; non-unit reserve floored | Usually **VFA**, the full liability including CSM | Unit funds drop out of both assets and technical provisions on the solvency side |
| Reinsurance asset | Reinsurers' share of each provision (gross/net basis); reinsurance receivables aged (REINS-2 haircuts); counterparty charge SM-4 | **Reinsurance contracts held**: FCF including non-performance, RA = risk transferred, own CSM, loss-recovery component; ceded premiums payable and recoveries receivable sit inside the asset or liability | Aging and admissibility haircuts exist only on the regulatory side. Settlement terms matter for capital, not for IFRS |
| Acquisition costs | **DAC / advance commission = nil** (except first-year long-term life) | IACF deferred inside the LRC or as an asset (paras 28A-28F), or expensed under PAA | Always a regulatory deduction where deferred |
| Onerous business | URR (short-term) or reserve basis (life) | Loss component; immediate P&L loss; reinsurance loss-recovery offset | Timing differs |
| Assets | Admissible values: limits, concentration, real estate on a cash-flow basis, unlisted at fair value, related parties, impairment | IFRS 9 / IAS 40 carrying amounts | Inadmissible or haircut assets are often the largest leakage |
| Capital items | BOF = admissible assets − liabilities − **treasury shares** + approved holding-company subordinated debt; AOF (LoC, uncalled capital) at 50% for SCR/MGF | Equity; LoCs off balance sheet | |
| Takaful | Company-level consolidated solvency (shareholders + fund), Decision 26/2014 | Fund and shareholders presented separately; qard hasan; wakala | Fund deficit funded by qard hits shareholders' equity in both |

**Practical bridge from IFRS equity to BOF (order of adjustments):**
1. Start from IFRS total equity (including the fund deficit or surplus attributable, for takaful).
2. Replace IFRS insurance and reinsurance contract balances with statutory net technical provisions, statutory reinsurance recoverables and gross receivables and payables. The CSM is effectively replaced by statutory prudence.
3. Remove inadmissible assets:
   - DAC;
   - intangibles;
   - assets outside the investment limits;
   - property revalued to cash-flow value (land and work in progress are near nil);
   - aged receivables per admissibility rules;
   - negative IBNR.
4. Deduct treasury shares.
5. Add approved subordinated items.

The result should reproduce the disclosed BOF. Any residual is a plug to explain, not to ignore.

## 3. Premium measures: what the template uses vs what IFRS 17 shows
| Template input | Used in | Best source | Proxy from IFRS 17 accounts (estimate only) |
|---|---|---|---|
| Gross written premium, last 12 months | Health and non-life premium risk | eForm PRM-1; segment note or management commentary | Insurance revenue under PAA ≈ gross earned; adjust for growth to approximate written |
| Net written premium | Health catastrophe | PRM-1 less ceded | Insurance revenue less allocation of reinsurance premiums, growth-adjusted |
| Gross earned premium | Operational risk | PRM-2 | Insurance revenue (PAA lines) |
| Net earned premium | **MGF** | PRM-2 net | Insurance revenue less allocation of reinsurance premiums |
| Gross and net technical provisions | Reserve risk, operational risk, mathematical-reserve shocks | TP-4, LT-4, LT-5 | LIC (gross and reinsurance) adjusted for RA and discounting: rough only |
| Net sum at risk | Life MGF, life cat | PRM-4, LT-1 | Rarely disclosed |

Estimates from published IFRS 17 accounts carry a reconciliation plug. Calibrate the plug to the disclosed SCR and MGF before using the model to test levers.

## 4. Reading a UAE insurer's published accounts for the capital story (workflow)
1. **Solvency note.** It discloses MCR, SCR, MGF, BOF and AOF, with surplus or deficit; the position may be one quarter old.
   - Record the as-at date.
   - Identify the binding test.
   - Check the MCR test against BOF only.
2. **Rebuild modules** with file 11 factors from segment data. Reconcile to the disclosed SCR and MGF.
3. **Bridge equity to BOF** (§2). Look for:
   - treasury shares;
   - land and work in progress;
   - unlisted or concentrated holdings;
   - related-party balances;
   - intangibles.
4. **Earnings quality.**
   - Insurance service result vs investment and other income.
   - Onerous-contract losses.
   - Favourable prior-year development (claims-development note).
   - RA confidence level.
   - Net expense from reinsurance held.
   - CSM run-off (life).
5. **Reinsurance programme.** Ceded share by segment vs template floors (50% health, 85% group life). Over-ceding beyond the floor means MGF is the only capital lever left. Check reinsurer ratings and concentration.
6. **Trajectory.** Growth in net premium drives MGF up by 26% of the increase on health. Project when MGF overtakes SCR or the MCR.
7. **Conclusion:** binding test now and in 4-8 quarters, levers ranked, and data asks (eForms SM-1 to SM-6, TP-4, FS-6, REINS-2 and receivables aging, INV-7).

## 5. Accounting vs capital effects of common actions [INTERP unless a paragraph is cited]
| Action | Regulatory capital | IFRS 17 profit and equity |
|---|---|---|
| New health QS with flat commission | SCR relief down to the 50% floor; MGF relief on all ceded net earned premium; Art 34 0.5% provision. Whether commission lifts BOF on day 1 depends on how the regulatory balance sheet carries unearned commission: VERIFY against FS-1 / EXP forms | No day-1 gain. A commission not contingent on claims reduces ceded premium over the coverage (para 86). The treaty shows as a net reinsurance expense; RA reduced by the risk transferred (para 64) |
| Sliding-scale or profit commission | Same capital as the QS. Cost depends on loss ratio | Contingent amounts sit in recoveries (para 86): the treaty result moves with the loss ratio |
| Cession of in-force UPR with commission | Possible day-1 BOF gain on the statutory basis (VERIFY treatment) | Gain deferred: net gain sits in the reinsurance-held CSM, or is recognised over remaining coverage under PAA (paras 65, 69-70) |
| LPT of incurred claims | BOF change = statutory reserve released − price. Reserve risk falls on net. **Art 125 approval** | **Net cost relating to past events is expensed immediately** (para 65A). Day-1 loss = price − IFRS FCF of the LIC (best estimate + RA, discounted) |
| ADC on existing reserves | BOF up only if the recoverable is valued on the same prudent basis as the gross reserve (VERIFY) | Past-events cover: the cost above FCF is expensed day 1 (para 65A) |
| QS incepting with onerous business | No special template effect (URR on statutory) | **Loss-recovery component** offsets part of the onerous loss if the reinsurance is in place when the onerous group is recognised (paras 62A, 66A-66B, 70A) |
| Life coinsurance on new business | Reserve credit on the ceded mathematical reserve; life shocks on net. Eases new-business strain on BOF | The reinsurance-held CSM defers net gain or cost. For profitable business there is little IFRS "strain" to relieve, because the CSM absorbs it [INTERP]. Onerous groups still show a day-1 loss (para 47), which can be partly offset by the loss-recovery component |
| Life YRT / risk premium | Life shocks on net sum at risk; no reserve credit | Reinsurance held measured on its own FCF; usually a small net cost |
| VIF / financing reinsurance | **Art 25 finite risk**: pre-clear or avoid | If no significant insurance risk: a financial liability, not IFRS 17 |
| Letter of credit / guarantee (AOF) | +50% towards SCR and MGF; 0 for MCR | Off balance sheet; disclosure only |
| Equity raise, asset de-risking, receivables clean-up | Direct BOF and SCR effects | Equity change; fair-value effects |

**Worked LPT example (AED m, illustrative):**
- Statutory incurred-claims reserve 100; IFRS best estimate 92; RA 2.6% of best estimate; discounting ignored (short-tail); reinsurer price 98.
- **Regulatory basis:** about **+2.0** (100 released − 98 paid), less the Decision 23/2019 Art 34 provision if the LPT premium counts as ceded premium (0.5% × 98 ≈ 0.5), so about **+1.5**.
  - This assumes the reinsurance recoverable is credited at the full statutory reserve. VERIFY the valuation basis with the appointed actuary, as for an ADC.
- **IFRS 17:** FCF = 92 × 1.026 = 94.4. Day-1 expense = 98 − 94.4 = **−3.6** (para 65A).
- **Lesson:** price an LPT against the IFRS FCF, not just against statutory reserves. Otherwise management sees a loss for a "capital gain".

## 6. Distributions and other links
- **Dividends** need CBUAE no-objection (C 5/2023 2-7, 2-8). The CBUAE can refuse where capital adequacy is short (CB Law Art 140(2)).
  - Life dividends are limited to the actuary-certified surplus (Art 99).
  - IFRS 17 profit alone does not make a dividend possible: the solvency position on the regulatory basis decides.
- **Corporate tax** (9% UAE CT from June 2023) is computed from accounting profit, so IFRS 17 timing affects tax timing [INTERP: confirm with tax advisers].
- **Takaful under IFRS 17:** presentation of the fund vs shareholders' results, wakala and mudaraba fees, and qard hasan varies by entity. Read each company's accounting policy note. Do not assume a market convention.

## 7. Pitfalls to call out
1. Computing SCR or MGF from IFRS 17 insurance revenue without saying it is an estimate.
2. Treating IFRS 17 equity, or equity less goodwill, as own funds.
3. Claiming SCR credit for health cession above 50% or group-life cession above 15%.
4. Selling XoL or stop loss as capital relief under the UAE template.
5. Presenting LoCs as an MCR fix.
6. Ignoring the Art 34 provision and REINS-2 aging in treaty economics.
7. Showing a statutory day-1 gain to a board that reports on IFRS 17, without the IFRS view.
8. Forgetting that at takaful operators, commissions go to the fund.
9. Applying DIFC (DFSA) rules to onshore companies, or the reverse.


<!-- ===== FILE: references/uae/19-uae-source-register.md ===== -->

# UAE layer: source register and open verification points

UAE layer version 1.0, compiled 6 Nov 2026.

## Primary sources used
| # | Source | Date / version | Used for |
|---|---|---|---|
| S1 | Federal Decree-Law No. 6 of 2025 (CB Law), English translation | Issued 8 Sep 2025; in force 16 Sep 2025 | Arts 2, 61, 69-70, 78-105, 120-128, 140-144, 168, 183-185 |
| S2 | CBUAE Rulebook, insurance section, full export | Retrieved 20 Oct 2026 | In-force status and effective dates of all instruments; text of Decision 23/2019, Decision 14/2018, Decision 22/2017, Decision 49/2019, C 5/2023, Circulars 24/25 of 2022, Takaful Regulation 2026 and Standards, C 4/2026 |
| S3 | IA Board Decision 25/2014, Financial Regulations for Insurance Companies (CBUAE_EN_1087) | 28 Dec 2014 | Sections 1-4 and 7, all Addendums |
| S4 | IA Financial Reporting eForms, User Instructions v1.7, and the v1.7 workbook formulas | IA era (VERIFY current version) | SM-1 to SM-6 factors, REINS-2 admissibility, takaful commission rule, eForm list |
| S5 | IFRS 17 Insurance Contracts, including the 2020 amendments | Effective 1 Jan 2023 | Core file 00; paras 65, 66A-66B, 86 etc. |
| S6 | Milliman, "UAE Insurance Industry Update: Preliminary 2023" (Apr 2024), summarising CBUAE notice 6163 of 15 Dec 2023 | Apr 2024 | IFRS 17 vs regulatory reporting basis; ORSA; recovery plans |
| S7 | Hadef & Partners, CB Law 2026 developments | 2026 | In-force date (16 Sep 2025) and the September 2026 conformity deadline; list of 2026 regulations |
| S8 | DFSA Prudential Insurance Business module (PIN) | Version held in the project | DIFC contrast only |
| S9 | EU Delegated Regulation 2015/35, Arts 208-215 | — | Risk-mitigation principles borrowed for the risk-transfer memo |

## Open points to VERIFY before relying on them in client work
1. **eForms version.** Is v1.7 still the filed version, or has the CBUAE issued a later template? Factors may have changed.
2. **IFRS 17 and the regulatory basis.** Has any CBUAE notice after Dec 2023 moved the regulatory returns or the solvency template to IFRS 17?
3. **New solvency regime.** CB Law Art 70 empowers the Board to set risk-based capital requirements. Watch for a replacement of Decision 25/2014 Section 2.
4. **Unearned reinsurance commission on the regulatory balance sheet.** This decides whether QS or UPR commissions create day-1 BOF.
5. **Reinsurance asset valuation basis** for ADC or aggregate covers (best estimate vs prudent).
6. **Solvency disclosure circular** allowing a one-quarter lag. Confirm the reference and current wording.
7. **ORSA:** current submission cycle and format.
8. **Decision 23/2019 article numbering and wording** against the live Rulebook (the export's layout places headings after text).
9. **Long-term life shock factors in SM-2(L):** not reproduced here; read them from the template the company files.
10. **Takaful IFRS 17 accounting policy:** entity-specific.

## Maintenance rule
When a source is updated:
- change the affected rows in files 10-13;
- bump the layer version;
- add the new source here with its date;
- move resolved VERIFY items into the main text with their citation.
