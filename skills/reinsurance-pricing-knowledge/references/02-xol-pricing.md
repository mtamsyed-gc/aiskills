# Part E - Pricing an XoL (per person, per event, stop loss)
Source: XoL pricing tool 0.9.1, repo `mtamsyed-gc/xolpricing` (`docs/XOL_MECHANICS.md`, `docs/methodology.md`; Python route only). As at 12 Nov 2026. The tool is broker-side: expected claims cost, indicative reinsurance cost, cedant impact. Capital and risk transfer are questions for the Treaty Structure Metrics kit and the skill `insurance-capital-ifrs17`. Swing rating and MDP (the Premium Terms sheet) are on branch `swing-mdp`, not on main at this date: check before telling a user the released pack has them.

### E1 Settle the cover first (from the slip)
| Choice | Options | Effect |
|---|---|---|
| Basis | RA / RAD (risks attaching): claim follows the policy inception year, exposure = written. LO / LOD (losses occurring): claim follows the treatment date (or payment date), exposure = earned | Decides which premium and which claims form a year (D9) |
| Unit of loss | Per person per year (member x treaty year, default); member x policy x year; per claim; per event | The amount the retention applies to |
| Subject premium | GNPI / NWPI / EPI, gross or net risk premium; or lives for a PPPY rate | The rate's denominator; must equal the Merit basis used |
| Existing QS | XoL on the cedant's retained share: every amount x retention % first | Layer loss falls more than pro rata |
| Limits | Benefit limit per plan or member, policy limit | Caps each unit; a layer can run "to the benefit limit" |
| Claims counted | Paid or incurred, sunset (e.g. only losses paid within 30 months), reporting cut-off, VAT, excluded products | Which amounts reach the layer |

### E2 Deterministic price (burning cost)
1. Units: sum claim lines to the unit of loss; amount = paid + OS.
2. Trend to the quote year Q: T(ty) = I_Q / I_ty from yearly trend rates, with one-off steps for tariff or benefit changes.
3. Pre-attachment completion: IBNR x unearned (RA only) x unwritten, applied to each unit's amount.
4. Cap: adj = min(amount x T x P, benefit limit, policy limit), with T the trend factor and P the completion product of step 3.
5. Layer loss per unit: xl = max(0, min(L, adj - AP)) x (1 - co-participation), with L the layer limit here.
6. Post-attachment completion on layer loss and on count: units not yet reported, and units still below the attachment today. Higher layers develop more, so factors can vary by attachment band.
7. Year total: min(max(sum of xl - AAD, 0), AAL); AAL = (1 + reinstatements) x L when reinstatements are limited.
8. Burning cost per year: per life = year total / full-year life-years; % of premium = year total / (full-year premium trended to Q).
9. Weight the years (tool defaults, oldest to newest: 5 years 10/15/20/30/25%, 4 years 15/20/35/30%, 3 years 25/40/35%, 2 years 50/50%, each scaled by months complete / 12). Outliers are not removed: their layer loss is spread evenly over the years.
10. E_det = weighted burning cost x lives_Q x incidence adjustment (1 unless a benefit or network change is justified).
- Credibility: Z = min(1, sqrt(units reaching the layer / full-credibility count)), tool default count 64.
- Leveraged trend = layer loss at Q / layer loss at Q - 1, minus 1. Report it: it explains why the layer rate moves faster than medical trend.
- The Merit ladder (D5) is the quick form of steps 1, 5 and 8 on fixed levels with no completion or cap.

### E3 Stochastic price (1-in-N views)
- Severity above a threshold u (default the lowest attachment): fit lognormal, gamma, Weibull, Pareto and GPD by censored, truncated maximum likelihood; pick the lowest AIC among proper fits; test with the mean excess at each attachment (fit within 0.8 to 1.25 of the data).
- Frequency: lambda = weighted units above u per life-year x lives_Q; Poisson, or negative binomial when year-to-year counts are over-dispersed.
- Each simulated year: draw the count, draw each claim, cap it at a benefit limit drawn from the book's mix, cut the layers, apply AAD / AAL, record reinstatement usage.
- Outputs: mean, SD, P50 to P99.5 and the 999 quantiles of annual recovery per layer and per option. The 1-in-N year is the quantile at 1 - 1/N (1-in-200 = 99.5%).
- Blend: E[L] = Z x E_det + (1 - Z) x E_stoch below the largest observed claim M, plus E_stoch above M in full. Experience says nothing about claims larger than any seen, so that part is never credibility-weighted away.
- Stop loss: gross year = attritional (lognormal on cost per life, CoV with a floor) + simulated large claims; recovery = min(max(base - AP, 0), L) x (1 - co-participation) on gross or net-of-XoL claims.
- Per event: events from clustered claim lines or from scenarios (lives x cost per life at a return period).
- **When to use which:** deterministic for a well-populated working layer and for as-if tests of expiring terms; stochastic for thin or high layers, for AAD / AAL / reinstatements / swing terms (they depend on the distribution, not the mean), for stop loss, and for any return-period statement.

### E4 From expected loss to premium
- P_target = (E[L] + k x SD) / (1 - sum of loadings); loadings = reinsurer expenses, brokerage, profit, premium tax; k = risk load on the SD of annual recoveries.
- Paid reinstatements: upfront P = P_target / (1 + E[r]), E[r] = expected reinstatement usage as a share of the upfront premium.
- Rates: per life = P / lives_Q; % EPI = P / EPI; per exposed life counts only lives whose benefit limit exceeds the attachment.
- Exhibit C1 (structures): premium, expected recoveries, expected cost of cover = P + E[reinstatement premium] - E[L], and "recoveries exceed premium 1 in N years".
- Exhibit C2 (cedant impact): surplus = budget - (net claims + premiums + reinstatement premiums) in the average year and at the chosen return periods.
- Expiring comparison: expiring rate restated at Q and trended by the leveraged trend, against the indicated premium; as-if results by year.
- Exhibits C1 and C2 are the tool's own sheet names, not sections C1 and C2 of the structures atlas in `insurance-capital-ifrs17`.

### E5 Slip terms
| Term | Meaning | Check |
|---|---|---|
| Priority / deductible / attachment point (AP), limit | "L xs R": the reinsurer pays the part of a unit's loss between R and R + L | The unit of loss (E1) |
| GNPI, NWPI, EPI | Subject premium the rate applies to; EPI is the estimate, adjusted to actual | Definition, and whether it changed from expiring (a wider base at a lower rate can cost more cash) |
| Fixed rate; PPPY rate | Premium = rate x subject premium; or an amount per person per year x lives | Lives in force or ever; member-years |
| MDP / M&D (minimum and deposit premium) | Paid up front in instalments, not returnable. Final premium = max(MDP, rate x actual base); the excess is the adjustment premium | MDP as % of the estimated premium (e.g. 85%); instalment dates; whether MDP equals the minimum-rate premium |
| Swing (burning-cost) rate | Rate = losses to the layer x loading / subject premium, never below the min rate nor above the max rate | E6 |
| Loading factor 100/80 | Multiplier on layer losses: 100/80 = 1.25, 100/90 = 1.111. Inside the band the reinsurer's loss ratio is 80% (or 90%) | With brokerage b inside the load, its loss ratio on premium net of brokerage is 80% / (1 - b) |
| Min rate, max rate, provisional rate | Floor and cap on the swing rate; the provisional rate is the deposit rate until adjustment | Recoveries at which the max binds = max premium / loading |
| AAD | Annual aggregate deductible: the cedant keeps the first amount of the year's layer losses | Applied before the AAL |
| AAL / aggregate limit | Most the layer pays in a year | Reinsurer's worst case = AAL - premium |
| Reinstatements | Number of times the limit refills, each at a cost % of premium pro rata to the amount used | Number; free or paid; how they sit with a swing rate (E6) |
| Co-participation | Cedant's share inside the layer | Taken off the layer loss, not the attachment |
| Sunset, reporting cut-off | Losses count only if paid or reported by a date | Drives how OS is treated |
| Stability / index clause | Retention moves with an index | Whether one applies |
| Brokerage | % of reinsurance premium, per layer (`insurance-capital-ifrs17` file 05, C7) | Inside or outside the loading |

### E6 Swing and MDP mechanics
- Swing premium in a year = min(max(l x layer losses, min rate x X), max rate x X); X = subject premium or lives; l = loading. Working convention: the numerator is that layer's losses only, capped at its aggregate limit.
- Three zones: below min premium / l the cedant pays the minimum whatever happens; inside the band the cedant funds its own layer losses at l times; above max premium / l the reinsurer bears the excess, up to the AAL. Real risk transfer sits only between max premium / l and the AAL.
- Expected swing premium = average of the formula over the simulated years (the tool uses the 999 recovery quantiles). Report: P(min applies), P(max applies), reinsurer's expected loss ratio = mean recoveries / expected swing premium, swing premium at each return period, expected adjustment against the provisional premium.
- Break-even min rate: the min rate at which the expected swing premium equals the flat technical premium, for a given loading and max. "Not binding" = swing already earns more at any min; "not reachable" = the max is too low.
- In the tool a swing-rated option carries no paid reinstatements, so it is compared with the flat premium including expected reinstatement premium.
- MDP = MDP % x deposit premium (provisional premium for swing, upfront premium for flat), in 1, 2, 4 or 12 instalments. Final at exposure change s: flat max(MDP, (1 + s) x P); swing = average of max(MDP, (1 + s) x swing premium). The tool has no exposure volatility: it shows a grid (default -20% to +20%) and assumes losses move with exposure.
- A swing cannot be valued from the mean loss: two books with the same expected recovery and different volatility pay different expected premiums. Use the simulation.

### E7 Reading a quote
- Is the minimum premium the same number as the MDP? Then the deposit is the floor.
- Where does the expected swing premium sit between min and max, and how often does each bind?
- Max / min multiple, and the recoveries at which the max binds, against the 1-in-N recoveries.
- Reinsurer's net worst case = AAL - max premium: is the AAL low enough that it, not the max rate, is the real cap?
- Rate change vs cash change: restate expiring on the new base.
- Do option-to-option rate relativities simply mirror the data pack's untrended recoveries? Then trend and development are not in the price; compare with E2 / E3.
- Under LOD, which premium measures the swing and when is it closed?
- Loading with brokerage inside vs outside.
- WHT and the local share (Part F).
