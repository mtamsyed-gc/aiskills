# Core: IFRS 17 worked numbers for reinsurance held and issued

Use with `00-core-ifrs17.md` when a user wants to see the entries: where each line goes, the loss-recovery offset on an onerous book, retroactive cover, and the reinsurer's side of the same treaty.

### B5 Worked numbers
Source: the IFRS 17 rules in `00-core-ifrs17.md` (paragraphs cited), applied 12 Nov 2026 to stylised figures. Illustrative arithmetic, not a client and not an accounting opinion. Per 100 of gross premium, one-year medical cover under the PAA unless stated, experience as expected, no discounting, RA ignored. QS = 50% with a 10% ceding commission that does not depend on claims, unless stated.

**Case 1. Profitable book with a QS: where each line goes (82, 86).** Claims 80, expenses 12.
| Line | Amount | Rule |
|---|---|---|
| Insurance revenue | 100 | Ceded premium is never netted against it (86) |
| Insurance service expenses | -92 | Claims 80 + expenses 12 |
| Insurance service result | 8 | |
| Allocation of reinsurance premium | -45 | Ceded 50 less commission 5: non-contingent commission reduces the premium (86) |
| Recoveries | +40 | 50% x 80 |
| Net result from reinsurance held | -5 | Shown separately (82) |
| Net | 3 | Check: retained margin 10 + commission 5 - expenses 12 |
- Same book with a sliding scale paying 15% in total, of which 5% is a guaranteed minimum: the minimum (2.5) reduces the premium to 47.5; the claim-dependent part (5.0) sits with recoveries, 45. Net reinsurance result -2.5, net 5.5. The split changes the two lines, not the total.
- Upfront commission on ceded unearned premium (surplus relief): statutory own funds rise on day 1 where DAC is nil; under IFRS 17 it is part of the reinsurance premium allocated over the cover, so day-1 equity moves by nil.

**Case 2. Onerous book with a QS: the loss-recovery offset (57-58, 66A, 70A, B119C-F).** Claims 98, expenses 10. Fulfilment cash flows for remaining cover 108 exceed the PAA liability 100, so a loss of 8 is booked when the group is recognised.
| | Day 1 | Rest of year | Year |
|---|---|---|---|
| Underlying | -8 | 0 (revenue 100; claims and expenses 108 less loss component released 8) | -8 |
| Reinsurance held | +4 loss-recovery income = 8 x 50% | 0 (recoveries 49 - premium 45 - reversal of the loss-recovery component 4) | +4 |
| Net | -4 | 0 | -4 |
- The income is the underlying loss x the share of underlying claims expected to be recovered (B119D). It is a timing item: it reverses as the loss component runs off.
- No commission instead: day 1 still -4, rest of year -5, year -9. The formula does not look at whether the treaty itself is priced at a cost.
- Treaty signed after the underlying group was recognised: no day-1 income (B119C). Day 1 -8, rest of year +4, same year total. Signing order moves the loss between reporting periods.
- Under the PAA the asset for remaining coverage is adjusted, not a CSM (70A).
- Regime link (KSA): the Saudi RBC adds the loss component to premium-risk exposure (skill `ksa-rbc-capital`, file 24), so an onerous book costs equity and capital requirement together; the QS offset helps equity only.

**Case 3. Onerous book with an XoL or stop loss: the recovery share is small (B119D).** Same book, per-person XoL: premium 4, expected recoveries 3.
- Recovery share = 3 / 98 = 3.1%. Loss-recovery income = 8 x 3.1% = 0.24.
- Day 1 -7.76, rest of year -1.24, year -9.
- A stop loss attaching above the expected loss ratio has an even smaller expected recovery share, so almost no day-1 offset, although it protects against exactly the deterioration that made the book onerous. The share comes from the pricing model: document it and keep it consistent with the quote.

**Case 4. Corridor QS with stop loss (C4 corrsl): two held groups (61, 65).**
- The QS and the stop loss are measured separately. Recovery share for each: QS = q x E[min(L, A)] / E[L]; stop loss = E[max(L - B, 0)] / E[L].
- Stop-loss premium 1.5 against expected recoveries 0.4: net cost 1.1 is spread over the cover, not expensed on day 1 (65).
- Stop loss bought below expected recoveries: the net gain is deferred as well. There is no day-1 gain from buying reinsurance.
- The corridor is the cedant's own retained loss: it appears as lower recoveries, with no separate line.

**Case 5. Retroactive cover (65A).** Incurred claims of 100 ceded in a loss portfolio transfer.
| Price paid | IFRS 17 | Statutory, where reserves are prudent |
|---|---|---|
| 104 | Net cost 4 relates to past events: expensed at once | Loss of 4 |
| 96 | Net gain 4 deferred and released over the settlement period | Gain of 4 on day 1 (C4 lpt) |

**Case 6. Long-term treaty under the general model (63-65).** Coinsurance: PV of premiums ceded 100, PV of recoveries 90, risk adjustment transferred 6.
- Net cost = 100 - 90 - 6 = 4: held as the reinsurance CSM and released over the cover.
- PV of recoveries 97: net gain 3, deferred the same way.
- A change in the reinsurer's non-performance risk goes to profit or loss, never to the CSM (67).

**Case 7. The reinsurer's side of case 2 (section 7 of the summary; 25, 47).** Its 50% share: premium 50 less commission 5 = revenue 45 over the year; expected claims 49; brokerage and own expenses 1.5.
- Outflows 50.5 against inflows 45: the inward treaty is onerous. Loss of 5.5 on day 1, recognised when the treaty becomes onerous, which can be before cover starts.
- So at signing the cedant books +4 and the reinsurer -5.5 on the same treaty. This is the accounting reason a reinsurer asks for a loading, a corridor or a lower commission on a loss-making book.
- A 12-month risks-attaching treaty over annual policies has about two years of cover: test PAA eligibility on the treaty itself, for cedant and reinsurer alike (69-70).
