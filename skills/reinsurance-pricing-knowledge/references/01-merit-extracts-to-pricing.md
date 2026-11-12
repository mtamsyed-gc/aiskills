# Part D - Merit extracts: what they hold and how they feed pricing, projections and capital
Source: Merit v9.2.1, repo `mtamsyed-gc/ete-dashboard`, `side_tools/merit` (output contract IP4-13; measures in `powerbi/MEASURES.md`; pages in `powerbi/build/build_report.py`; the Merit user manual ships in each Merit pack). As at 12 Nov 2026. Merit turns a cedant's raw premium, membership and claims files (per payer and TPA) into one set of tables, an aggregated extract and a Power BI dashboard. This part says what exists and how to use it; read the repo for exact definitions.

### D1 Outputs and grain
| Output | Grain | Holds |
|---|---|---|
| `dim_life` | Life-period: payer, TPA, policy, member x UW year | Payer, RI name, TPA, policy type, policy, master contract, plan / category, network, region group, nationality group, gender, marital status, relation, age at inception and age band, group size and band, new / renewal, joiner / leaver, tenure, distribution, five optional fields, cover dates, written and earned premium and life-years (gross, net), Reinsured %, treaty ceded %, ceded %, scope status |
| `fact_member_month` | Life-period x calendar month | Written premium (booking month) and earned premium, gross and net; written and earned life-years |
| `fact_claims` | Claim line | Claimed, approved, payer share, paid, outstanding (OS); capped and excess amounts under a CAP rule; treatment date, incurred / reported / paid month and lags; status class and claim type; provider, provider type and region; ICD code and chapter; benefit (FOB / FOC); large-claim flag; match to its life-period; line-level ultimates and factors (IBNR and IBNP basis); in-cover, in-experience and scope flags |
| `ultimates`, `cf_selected` | Payer x TPA x incurred month x UW year; TPA x basis x measure x lag 0-12 | Reported, paid, OS, IBNR, IBNP, ultimate claims and counts, method (chain ladder, BF, no factor); completion factors derived, overridden and used, with a credibility flag |
| `Merit_Extract` (.xlsx, .csv) | Attribute set x exposure month | The aggregate to share or email. Keys: payer, RI name, TPA, policy type, UW year and month, exposure month, master contract, policy, gender, marital status, nationality, region, age band, new / renewal, renewed / non-renewed, group-size band, network, currency. Measures: written and earned premium (gross, net, gross-net), admin fee, TPA fee, broker commission, ERP (earned life-years), paid / OS / reported claims and visit counts. Shares: Reinsured %, Treaty Ceded %, Ceded %, plus a 'Ceded by reinsurer' sheet |
| `Merit_PNLR_Base`, `Merit_TreatyMetrics` | TPA x policy type (and treaty segment) | Base of the projected net loss ratio; annualised treaty metrics (IBNR ultimate only) |
| `recon_*`, `exceptions*`, `run_manifest*`, diagnostics | Run | Reconciliation to the raw files, message codes, valuation and extract dates, currency, default premium basis |

### D2 Bases: state every one of them beside a figure
- **Premium basis:** Gross or Net on the dashboard (run default Net); the extract also carries Gross-Net and the fees. "Net" is whatever the cedant's file maps to it, often the net risk premium (gross less loadings). Confirm it, because the treaty premium base (GNPI / NWPI) must be the same thing.
- **Written vs earned:** written sits in the booking month; earned and life-years run to the valuation or Experience-to date. Zero-premium life-periods give no exposure.
- **Claims basis:** Paid; Incurred = paid + OS; Ultimate. Reserve basis for the ultimate: IBNR (develops paid + OS) or IBNP (develops paid, OS set to 0). Pre-adjudication OS can count Full, Expected, Excluded or Custom.
- **Year:** UW year = year of the policy coverage start (a risks-attaching view). Claims enter the experience by treatment month.
- **Before or after reinsurance:** the RI book slicer (Reinsured / Retained / Not known) and three views side by side: portfolio, reinsured book at 100%, ceded share (each life's amount x Reinsured % x the treaty's non-retained shares). "Gross vs net" therefore has two meanings: premium basis, or before vs after reinsurance. Say which.
- **Adjustments in force:** per-UW-year premium and ultimate factors (as-if rate or development loads), the what-if cap per life-period, scope rules (EXCLUDE, CARVEOUT, RESHARE, CAP), the Experience-to cut-off.
- **Ultimate below TPA level:** development factors are per TPA x lag, so an ultimate cut by age, network or plan assumes the segment develops like its TPA. Say so, or show incurred.

### D3 Cuts (dashboard pages) and what each is for
| Pages | Cut | Use in QS work | Use in XoL / stop-loss work |
|---|---|---|---|
| Executive summary; Portfolio headline; Loss Ratio by Cohort | UW year (and inception cohort): premium, claims, loss ratio on the selected bases | The headline L and its history; cohort maturity | The premium and life-year base for burning cost |
| RI - Reinsured book | Portfolio, reinsured book, ceded share by UW year | Subject premium, ceded premium and the ceded loss ratio the reinsurer actually bears | Whether the XoL sits on the gross book or on a QS retention |
| Segment relativities; Region; Network; Gender and age; Group size band; Jumbo groups; New vs renewal; Retention; Benefit mix; Optional fields | Policy type (Group / SME / Individual), TPA, region or emirate, network or plan, gender x age band, group-size band, new vs renewal, benefit | Where the loss ratio comes from: carve-outs, different cession by segment, segment caps, referral rules, rate action by cell | Which segments carry exposure above the attachment; mix shift that changes large-claim frequency |
| Frequency and severity; Calendar trend; Providers; Diagnoses; Monitoring pages | Claimants, visits, cost per claimant; top providers, policyholders, members; ICD groups | Split of trend into frequency and severity; claims-control arguments | Severity drivers, clustering by provider or scheme |
| Large claims and concentration; Large claimant sensitivity | Top-10 and top-1% claimant share; the cap ladder | Volatility of the QS result; case for a per-member cap | D5: the deterministic XoL basis |
| Inception and earning profile; Volume vs EPI | Written by inception month; written % of EPI, annualised | EPI credibility, earning pattern, cash-flow timing | Sizing the deposit premium; exposure for the quote year |
| Development and IBNR | Completion factors, IBNR / IBNP, completion % | Maturity of each UW year; the load a reinsurer will add | Development of immature years (layers develop more than ground-up) |
| Loss ratio bridge | Prior to latest UW year: mix effect vs within-segment effect | Explains deterioration: mix (underwriting) vs rate adequacy | Same, for the claims base |
| Rate adequacy; PNLR; PNLR scenarios | As-if LR at proposed rates; required rate change; projected net LR | D4: the projected L for terms and commission | Projected premium base and expected claims |
| Data quality pages; reconciliation; Leakage chain | Red flags, match rates, recon to raw files | Read first; carry the caveats into the pack | Same |

Development and IBNR, Leakage chain, Calendar trend and Retention are hidden pages by default. The Merit report builder (presets such as Full, QS Analytics, XoL Analytics) is planned, not built, and the owner has not fixed which pages each preset holds: do not present a preset list as decided.

### D4 Projection: next year's loss ratio and volume
- **PNLR (projected net loss ratio)**, per TPA x policy type and rolled up:
  - expiring LR = ultimate / net earned premium of the latest UW year, credibility-weighted with the prior year trended
  - renewal claims = expiring NWP x retention x expiring LR x (1 + trend); renewal premium = expiring NWP x retention x (1 + R)
  - R = (1 + trend passed on)(1 + global increase)(1 + haircut x residual) - 1; residual = the increase still needed to reach the target LR after trend and the global increase (floor 0)
  - retention falls linearly with the increase beyond trend; new business = expiring NWP x NB share by policy type, at the expiring LR trended, on its own tariff
  - expiring NWP is annualised: written x 12 / months elapsed
  - defaults when nothing is set: target 95%, trend 8%, haircut 1.0, credibility 1.0, NB share 0%. These are settings, not findings: state the ones used.
  - the PNLR bridge gives the steps: expiring LR, trend, trend passed on, global increase, residual to target, lapse mix, new business.
- **Rate adequacy:** required rate change = (1 + trend) x LR / target - 1; gap = required - proposed.
- **TSM, the Treaty Structure Metrics kit** (`side_tools/treaty_workbench`, TW-1.2) builds next year's P&L and solvency per scenario from Merit's tables:
  - ultimate per TPA x UW year = first available of IBNR ultimate, IBNP ultimate, paid + OS, paid
  - volumes annualised (prior-year booking pattern, else x 12 / months); annualising never changes the loss ratio
  - books = Merit treaty segments; cells = TPA x policy type; projected LR = the PNLR method on those ultimates; EPI from the same projection or an override
  - claims range: large claimants from the xolpricing severity curve when supplied, else the Merit claimant ladder (D5); attritional = expected claims - expected large claims, lognormal
  - outputs: expected and 1-in-10 / 1-in-50 / 1-in-200 P&L per scenario; capital requirement with and without reinsurance (UAE SCR / MGF / MCR; Saudi margin, RBC proxy indicative); own-funds roll-forward; cost of capital relief = net reinsurance cost / capital relief.

### D5 The claimant ladder: deterministic XoL from history
- **What it is:** on the Large claimant sensitivity page each life-period's claims total (claimant x UW year) is capped at a ladder of levels: 100k, 250k, 500k, 750k, 1m, 1.5m, 2m, 2.5m, 3m, 4m, 5m (run currency). Per level and UW year, and under any slicer cut: claimants above N(t), excess removed E(t), capped loss ratio, loss-ratio points removed. Amounts are incurred (paid + OS), or paid when the claims basis is Paid; never ultimate.
- **Why it prices XoL:** E(t) is the burn of an unlimited per-person layer xs t in that UW year.
  - layer L xs R: loss = E(R) - E(R + L); claimants reaching it = N(R)
  - burning cost = layer loss / earned premium of the same UW year, or / earned life-years for a per-life rate
  - loss-ratio points removed at t = the gross benefit of a retention at t
- **Between and above ladder points** (Workbench method): between two populated levels the count follows a Pareto, N(t) = N_i (t / t_i)^-a with a = ln(N_i / N_i+1) / ln(t_i+1 / t_i); above the top populated level, a = 1 + t N / E.
- **To the quote year:** trend f acts on the claim, not on the layer, so E_f(t) = f x E(t / f): a layer trends faster than ground-up claims. Benefit cap B: E_B(t) = E_f(t) - E_f(B). Then weight the years per life-year and multiply by projected life-years.
- **Limits:** fixed levels (an attachment between two levels needs the interpolation or the XoL tool); per life-period on the UW-year view only (risks attaching, per person per year); OS at face value; the latest UW year is immature and only part earned. Switches for per-claim-per-year and losses-occurring are queued, not built (12 Nov 2026).
- **Companion cuts:** Large claims and concentration, Diagnoses, Providers, Jumbo groups (1,501+ lives). The run's large-claim flag is per visit, a different grain from the ladder.

### D6 Using the numbers on a quota share (per 100 of ceded premium)
- Take L = projected ceded loss ratio (D4) on the treaty's premium base, and the spread of L from the UW-year history, the PNLR scenarios or TSM's range mode.
- Reinsurer margin = 100 - L - c - brokerage - WHT (non-resident share only, Part F). Break-even L* = 100 - c - brokerage - WHT - target margin (about 3: `insurance-capital-ifrs17` file 05, C7).
- Highest commission the book supports: c_max = 100 - L - brokerage - WHT - margin. Negative c_max means rate action, an NRP-plus-loading basis, a corridor or cap, or a lower cession, not a plain QS.
- With no ceding commission the pack's loss ratio is the reinsurer's technical result before brokerage: say that in the pack rather than leave reinsurers to assume a commission.
- Cedant cost of the QS = q x (100 - L - c) of subject premium given away in an expected year, against the capital released (`insurance-capital-ifrs17`, file 02) and the volatility ceded.
- Calibrate a sliding scale, profit commission or corridor on the distribution of L, not on one year; check the pieces do not overlap (a sliding scale ranging above a corridor floor makes the cedant pay twice for the same deterioration).
- Segment cuts decide scope: a segment that drives the loss ratio can be carved out, ceded at a lower share, capped as a share of EPI or put under referral.

### D7 Using the numbers on an XoL or stop loss
- Per-person XoL: ladder (D5) for a first deterministic read; the XoL tool (Part E) for anything quoted. The tool reads `dim_life`, `fact_member_month` and `fact_claims` as written and applies its own trend and completion; it does not use Merit's ultimates.
- Subject premium and lives for the quote year: EPI and life-years from D4, on the slip's basis.
- Stop loss and corridors: need the whole-year loss-ratio distribution, so use TSM or the XoL tool's stop-loss stage (attritional + large), not the ladder.
- QS then XoL: the XoL acts on (1 - q) x each claimant's total; state the inuring order (`insurance-capital-ifrs17` file 05, C8 c_inure).

### D8 Capital and profitability, both sides
| Structure | Insurer (cedant) | Reinsurer | Numbers from |
|---|---|---|---|
| QS | Net premium and reserves fall by q down to the regime floor (`insurance-capital-ifrs17`, file 02); gives away q x (100 - L - c) in an expected year; volatility falls pro rata | Result = ceded premium x (1 - c - brokerage - WHT) - q x claims; capital on its share; needs L below break-even with a believable projection | RI book, PNLR, TSM |
| Per-person XoL | Net loss ratio stabilised above the attachment; little credit in the volume-based capital formulas (`insurance-capital-ifrs17` file 02, A7), so the value is retained volatility; cost = premium - expected recoveries | Result = premium x (1 - brokerage - WHT) - recoveries; priced on E[L] + risk load + loadings; worst case = aggregate limit - premium | Ladder, XoL tool C1 / C2 |
| Stop loss, corridor, aggregate QS | Caps the bad year: relief shows at 1-in-200, hardly in volume formulas | Tail and parameter risk, priced on capital | Treaty Structure Metrics kit, range mode |

Always show the same year both ways: expected year and the 1-in-N year, cedant column beside reinsurer column.

### D9 Traps met in client work
- **Year basis must match.** UW-year premium goes with UW-year (risks-attaching) claims; loss-year claims need calendar-year earned premium or member-years. A page that divides loss-year recoveries by UW-year premium is wrong in every column built on it (min, max, loading, treaty result), not only in the burning-cost column.
- **Row grain.** Claim line, claimant, and claimant x year give different layer losses. Check what "per claim" means in the wording before choosing the cut.
- **Immature years.** Large-claimant counts in the latest UW year keep growing for many months; a part-earned year also needs annualising.
- **OS quality.** Pre-approvals and pending lines can sit in OS. Where the treaty pays on paid claims with a sunset, OS counts only as payments expected before the sunset.
- **What is inside claims:** VAT, TPA fees, cancelled or reversed lines. Fix the treaty basis first, then the extract.
- **Exclusions are three-sided:** remove an exceptional policy or an out-of-treaty product from premium, exposure and claims together.
- **Group-size bands** count every member ever on the policy, so they overstate size for high-turnover groups.
- **A very low loss ratio can be real** (a low-utilisation product), not a data gap: check before excluding.
- **Linear annualising** (x 12 / months) misleads when inception is seasonal.
- **Merit vs the cedant's own figures:** keep both, with the gap and its reason; never net them.
