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
