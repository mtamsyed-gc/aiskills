---
name: reinsurance-pricing-knowledge
description: Use for any question on pricing a medical or life reinsurance treaty from portfolio data - what the Merit dashboard and extracts contain (loss ratio on gross and net bases, cuts by policy type, TPA, age, gender, network, group size, the large-claimant ladder, the projected net loss ratio) and how they feed quota share and excess-of-loss pricing, projections, capital and profitability for insurer and reinsurer; how an XoL is priced (burning cost, simulation and 1-in-N views, MDP, minimum and maximum swing rates, loading factors such as 100/80, AAD, aggregate limits); reading a reinsurer's quote; KSA 5% withholding tax and 30% local cession.
version: 1.0.0 (12 Nov 2026) - built from Merit v9.2.1 (output contract IP4-13), the XoL pricing tool 0.9.1 and KSA sources checked 12 Nov 2026
---

# Reinsurance pricing knowledge skill

## 1. What this skill is for
You are supporting a life & health reinsurance broker / pricing actuary (FIA) and his team, who price and place GCC medical and life treaties from cedant data processed by Merit. Typical questions:
- "Which Merit page or extract gives me X, and on what basis is it?"
- "What does this loss ratio mean for a quota share: break-even, commission the book can support, cost to the cedant?"
- "Price this layer from the claimant ladder" or "why does the XoL tool give a different answer from the ladder?"
- "Explain MDP, min and max rates, a 100/80 loading, AAD, AAL on this slip."
- "How do these quoted terms look?"
- "What do Saudi withholding tax and the local cession rule do to this placement?"
- "What should go in the data pack for reinsurers, and what is wrong with this one?"

## 2. Files and when to load them
Load only what the question needs. Each file stands alone.

| File | Load when |
|---|---|
| `references/01-merit-extracts-to-pricing.md` | Anything about Merit outputs, bases, dashboard cuts, the projected loss ratio, the claimant ladder, using the numbers on a quota share or XoL, insurer and reinsurer results side by side, and common data traps (Part D) |
| `references/02-xol-pricing.md` | Pricing or explaining an XoL, stop loss or per-event cover: basis choices, burning cost, simulation, premium loadings, slip terms, swing and MDP mechanics, reading a quote (Part E) |
| `references/03-ksa-placement-constraints.md` | Any Saudi cedant: 5% withholding tax on premium to non-resident reinsurers, 30% local first refusal, the 30% retention rule, checklist (Part F) |
| `references/09-source-register.md` | To cite a source, check how current a statement is, see the open points, or run the load tests |

Part letters D, E, F continue from the companion skill (section 6), so a reference such as A7, C7 or D5 means one place only.

## 3. How to answer (always)
1. **State every basis beside every figure:** premium basis (gross, net, net risk premium), written or earned, claims basis (paid, incurred, ultimate on IBNR or IBNP), year basis (underwriting year or loss year), before or after reinsurance, and the as-at date.
2. **Match numerator and denominator.** Underwriting-year claims go with underwriting-year premium; loss-year claims need calendar-year earned premium or member-years. Check this before any burning cost.
3. **Say which method produced a number:** ladder (deterministic, fixed levels), XoL tool burning cost, or simulation. Give 1-in-N statements only from a simulation.
4. **Show the arithmetic,** with assumed inputs (trend, development, loadings, brokerage, margin) labelled as assumptions.
5. **Show both sides:** insurer and reinsurer result for the same year, expected and 1-in-N.
6. **Tag authority** as in the capital skill: [RULE] law, regulation or circular; [INTERP] interpretation; VERIFY = check the primary text. File 03 is checked against published summaries, not the full Arabic texts.
7. **Close with** what the number rests on, what would change it, and the data still needed.

## 4. Guardrails
- This is analysis, not legal or tax advice. Withholding tax and local-cession points need the cedant's tax adviser and the circular text.
- Do not invent factors, rates or article numbers. If a figure is not in these files or the user's data, say so and say where it comes from (which Merit page, which tool output).
- Keep client data inside LenAI. Anything prepared to leave LenAI must be free of client names, member data and row-level figures unless the user explicitly confirms otherwise.
- Never present a figure from this skill's worked illustrations as a client's figure.
- Swing rating and MDP are on a development branch of the XoL tool, not in the released 0.9.1 pack (as at 12 Nov 2026). Say so if a user looks for the Premium Terms sheet.
- The Merit report builder presets are planned, not built; do not describe a preset's page list as decided.
- For multi-step pricing or a quote review, recommend switching the chat model to Sonnet if available.

## 5. Output patterns
- **Quick answer:** 3-6 lines: answer, basis, method, one caveat.
- **Layer price:** cover definition (basis, unit of loss, subject premium) → data used and its limits → burning cost steps → simulation view if available → loadings → rate, with the leveraged trend → caveats.
- **Quote review:** terms restated on one basis → minimum, expected and maximum premium → where risk transfer starts and ends → reinsurer's worst case → points to negotiate → wording points.
- **Quota share view:** projected loss ratio and its range → reinsurer margin and break-even → commission the book supports → cedant cost against capital released → segment actions.
- **Data pack check:** bases stated? years matched? grain right? immature years flagged? exclusions three-sided? what reinsurers will ask next.

## 6. Companion skill
`insurance-capital-ifrs17` (a separate skill) holds the capital side: solvency rules for UAE, Qatar QFC and KSA, rating-agency capital models, IFRS 17, the reinsurance structures atlas and risk-transfer tests. If a question needs the capital credit of a structure, which test binds, IFRS 17 treatment, or the choice of structure, ask the user to load it with `/insurance-capital-ifrs17` unless it is already loaded. References here to sections A5, A7, C4, C7 and C8 point to its files 02 (A) and 05 (C). For column-level definitions of Merit's tables, the `merit-outputs` skill is the authority where it is installed.


<!-- ===== FILE: references/01-merit-extracts-to-pricing.md ===== -->

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


<!-- ===== FILE: references/02-xol-pricing.md ===== -->

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


<!-- ===== FILE: references/03-ksa-placement-constraints.md ===== -->

# Part F - KSA placement constraints: withholding tax and local cession
As at 12 Nov 2026. Checked against ZATCA's WHT circular and published summaries of the Insurance Authority (IA) circulars, not against the full Arabic texts: VERIFY the primary document and take tax advice before a client relies on it. Analysis, not legal or tax advice. The one-line versions of these rules sit in `insurance-capital-ifrs17` (file 02 section A7, file 05 section C7).

### F1 Withholding tax: 5% on reinsurance premium to non-residents
- [RULE] A Saudi-resident insurer paying reinsurance premium to a non-resident reinsurer withholds 5% of the premium and remits it to ZATCA (Income Tax Implementing Regulations Art 63(1) rate, Art 5(2) source rule; VERIFY article numbers). The premium is Saudi-source because the cedant is Saudi-resident.
- [RULE] Due within the first 10 days of the month after payment. Each payment is its own event: every deposit instalment and every adjustment premium. Claims recoveries are not subject to WHT.
- A reinsurer licensed and resident in the Kingdom takes no WHT. A non-resident with a permanent establishment is taxed on the PE's profit instead; conducting reinsurance in the Kingdom through an agent can itself create a PE (VERIFY).
- A double tax treaty can reduce or remove the 5%, on the reinsurer's tax-residence certificate: check per reinsurer domicile (VERIFY; ZATCA circular on WHT under double tax agreements).
- Base = the premium paid. Whether ceding commission netted in the account reduces the base is not settled here: confirm (`insurance-capital-ifrs17` file 05, C4 grossbasis). A gross-plus-commission QS carries more WHT than NRP-plus-loading for the same economics.
- **Who bears it is a wording point.** Borne by the reinsurer (deducted from premium; the owner's working convention): its income is 95 per 100 ceded, so its break-even loss ratio falls 5 points and it prices for that through lower commission, a higher rate or a loading. Grossed up by the cedant: cost rises by 1 / 0.95 - 1 = 5.26% of that premium.
- Panel effect: friction per 100 of treaty premium = 5 x non-resident share (70% non-resident = 3.5). Put it in every reinsurer-side result (D6, D8) on the non-resident share only.
- Structure effect [INTERP]: WHT scales with premium ceded, so for the same tail protection a low-premium structure (XoL, aggregate QS, stop loss) carries less of it than a high-volume QS; on a swing layer it applies to the minimum, the adjustment and the maximum alike.

### F2 Local cession: 30% offered to Saudi-licensed reinsurers first
- [RULE] Circular of 26 Oct 2022 (issued under SAMA, now with the IA): treaty cessions, 20% from 1 Jan 2023, 25% from 1 Jan 2024, 30% from 1 Jan 2025. IA circular of Nov 2024: 30% from 1 Jan 2025 on treaty and facultative, proportional and non-proportional, with procedures and record-keeping.
- Mechanics as published: before going to international reinsurers the insurer offers at least 30% of the cession to reinsurers licensed in the Kingdom, directly or through its broker; they may accept or decline; the insurer keeps evidence of the offer; brokers must show the business to the local market first; the reinsurance strategy filed with the regulator reflects it.
- It is a first-refusal rule, not a guaranteed 30% line: if local capacity declines or accepts less, the balance can go abroad, with the evidence on file. Whether 30% is tested per treaty, per class or overall, and whether a local reinsurer must follow the lead's terms: VERIFY in the circular.
- Separate rule, do not confuse: Implementing Regulations Art 40 makes the insurer retain at least 30% of total premium, so no more than 70% of an own book can be ceded in total.
- Consequences for a placement [INTERP]:
  - Sequence: local market approached first and documented, before or alongside the lead.
  - A local line carries no WHT (F1), so the same gross terms are worth about 5 points more to it than to a non-resident.
  - Counterparty charge follows the local reinsurer's rating; note the KSA-RBC cliff between BBB and below (`insurance-capital-ifrs17` file 02, A5). Few local reinsurers means concentration: check the IA's current list of licensed reinsurers.
  - Model the panel as shares by residency and rating (TSM does this per layer): results, WHT and credit charge all move with the split.
  - A structure the local market will not write (unlimited stop loss, novel structured terms) still has to be offered; allow time for a documented decline.

### F3 Checklist for a KSA treaty
1. Art 40 retention met (cession no more than 70% of total premium).
2. 30% offered locally first; evidence kept; broker's process documented.
3. Each reinsurer: resident or not, treaty relief or not, WHT borne by whom, stated in the wording.
4. Rating at or above the regime minimum and the counterparty charge (`insurance-capital-ifrs17` file 02, A7 and A5).
5. Finite-risk test (Art 19) on any corridor, cap, sliding scale or swing terms; reportable features (Art 18).
6. Reinsurer-side results shown net of brokerage and WHT; cedant-side cost shown gross of any gross-up.


<!-- ===== FILE: references/09-source-register.md ===== -->

# Source register, open points and load tests

As at 12 Nov 2026 (skill v1.0.0).

## Sources
| File | Built from | Version / date | Notes |
|---|---|---|---|
| 01 Merit extracts to pricing | Merit code and documents: output contract, measure catalogue, report page list, extract builder, user manual; Treaty Structure Metrics design | Merit v9.2.1, contract IP4-13; TSM TW-1.2 | Page titles and measures change with Merit releases: recheck at each release |
| 02 XoL pricing | XoL pricing tool mechanics and methodology notes | Tool 0.9.1 | Swing rating and MDP described from the development branch, not yet in the released pack |
| 03 KSA placement constraints | ZATCA circular on withholding tax under double tax agreements; published summaries of the Saudi circulars on local reinsurance cession (26 Oct 2022 and Nov 2024) | Checked 12 Nov 2026 | Secondary sources for the mechanics: read the circular text before a client relies on it |

## Open points (VERIFY)
1. KSA local cession: whether 30% is tested per treaty, per class or overall; whether a local reinsurer must follow the lead's terms.
2. KSA withholding tax: the base when ceding commission is netted in the account; treaty relief by reinsurer domicile; the article numbers cited (Implementing Regulations Art 5(2), Art 63(1)); the agent permanent-establishment rule.
3. Merit: per-claim-per-year and losses-occurring switches on the claimant ladder are queued, not built; report-builder presets are not defined.
4. XoL tool: swing rating and MDP not yet on the released branch.

## Maintenance rule
- This skill mirrors the owner's Claude-side reference of the same name. When that reference changes, regenerate the affected file, bump the version and add a line here.
- Update file 01 when Merit's output contract, page list or ladder levels change; file 02 when the XoL tool's method or released features change; file 03 when a ZATCA or Insurance Authority rule changes or a VERIFY point is settled.
- No client names, engagement notes or deal terms. Lessons from client work go in as general rules (file 01 section D9, file 02 section E7).
- This skill cites `insurance-capital-ifrs17` by section code (A5, A7, C4 grossbasis, C7, C8 c_inure). If a code changes there, update it here.

## Load-test questions (expected answer in brackets)
- **T1.** The claimant ladder for one underwriting year shows excess removed of 3.0m above 250k and 0.8m above 500k; earned premium is 200m. What is the burn of a 250k xs 250k per-person layer?
  - [E(250k) - E(500k) = 2.2m = 1.1% of earned premium. Must add: untrended, undeveloped, incurred at face value, underwriting-year (risks attaching) view. File 01, D5.]
- **T2.** Swing-rated layer: loading 100/80, minimum rate 1.0%, maximum 3.5%, subject premium 100m. What is the premium if layer losses are 0.5m, 2.0m and 4.0m, and at what recoveries does the maximum bind?
  - [Loading 1.25. 0.625% is below the minimum, so 1.0m; 2.5%, so 2.5m; 5% is above the maximum, so 3.5m. Maximum binds at 3.5m / 1.25 = 2.8m of losses. File 02, E5-E6.]
- **T3.** MDP is 85% of a 2.0m deposit premium. What is paid if the adjusted premium comes to 1.5m, and to 2.3m?
  - [MDP 1.7m. At 1.5m the cedant still pays 1.7m, nothing returned. At 2.3m it pays a further 0.6m. File 02, E5-E6.]
- **T4.** Projected ceded loss ratio 88%, brokerage 2.5%, 70% of the panel non-resident on a Saudi treaty with tax borne by reinsurers, reinsurer margin 3%. What ceding commission can the book support?
  - [100 - 88 - 2.5 - 3.5 (5% x 70%) - 3 = 3.0%. File 01, D6 and file 03, F1.]
- **T5.** "Show me the loss ratio gross and net." What must be clarified?
  - [Two meanings: premium basis (gross premium vs net or net risk premium), or before vs after reinsurance (portfolio vs reinsured book vs ceded share). Also the claims basis and whether earned. File 01, D2.]
- **T6.** Must a Saudi insurer place 30% of every treaty with a local reinsurer, and how much can it cede in total?
  - [It must offer at least 30% to Saudi-licensed reinsurers first; they may decline, and evidence of the offer is kept. Separately it must retain at least 30% of total premium, so no more than 70% ceded. Per-treaty vs overall testing is a VERIFY point. File 03, F2.]
- **T7.** A reinsurer data pack shows recoveries by loss year divided by underwriting-year premium. Is that a problem?
  - [Yes: bases do not match, and every column built on the ratio (minimum, maximum, loading, treaty result) inherits it. Fix by keying recoveries to underwriting year or adding calendar-year earned premium. File 01, D9.]
- **T8.** Can the expected premium of a swing-rated layer be worked out from the expected layer loss alone?
  - [No. It depends on how often the minimum and maximum bind, so it needs the distribution of annual recoveries. File 02, E6.]
