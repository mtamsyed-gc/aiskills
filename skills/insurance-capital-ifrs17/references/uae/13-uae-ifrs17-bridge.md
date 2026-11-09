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
