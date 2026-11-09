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
