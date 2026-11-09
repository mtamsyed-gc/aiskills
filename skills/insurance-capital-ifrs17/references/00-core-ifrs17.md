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
