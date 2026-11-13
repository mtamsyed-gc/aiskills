# Core: reinsurance and capital structures atlas (48 structures, 31 clauses)

Use to choose or design a structure: start from the cedant's objective (C0), read the candidate entries (C1-C6), add clauses (C8), then test capital credit (file 02 and the country files), IFRS 17 (files 00 and 04) and risk transfer (files 01 and 06). Lines: H health, L life, P property and casualty. Finite-risk flag: low / watch / high.

Notation: P premium; L gross loss ratio; q cession share; c commission rate; R retention; [P] premium flow, [R] recovery, [C] commission back, [S] structural flow, [F] friction (tax, brokerage, fees). Finite-risk flag: low / watch / high.
Risk-transfer tests: ERD = E[max(-RI result, 0)] / premium >= 1%; 10-10 = >= 10% chance the reinsurer loses >= 10% of premium; T1 = reinsurer result at its own 99.5th percentile; T2 = reinsurer result in the cedant's 1-in-200 years; T3 = cut in the cedant's 1-in-200 loss after the structure's cost (Solvency II risk-mitigating-effect reading). Finite definitions: EU Directive 2005/68/EC Art 2(1)(q), Solvency II Art 210(3), IAIS 2006.

### C0 Objective index (primary; secondary in brackets)
- Risk-based capital relief (SCR / RBC): qs, qsxol, xol_cat, coins, longevity, masslapse, lifecoins, bpa, corrsl, capreliefqs, lpt, adc, contcap, subloan, sidecar, catbond, portfolio (surplus, stoploss, yrt, modco, reservefin, corridorqs, aggqs, multiyear, grossbasis, retakaful)
- Premium-based test relief (e.g. UAE MGF): qs, corridorqs, capqs, slidingqs, marginlocked, capreliefqs (corrsl, grossbasis)
- Day-1 own funds / surplus: vif, reservefin, lifecoins, surplusrelief, prudenceadc, subloan, retakaful (lpt, contcap)
- Earnings volatility: qsxol, xol_risk, stoploss, aggxol, corrsl, aggqs, spreadloss, multiyear (qs, xol_cat, umbrella, topdrop, longevity, adc)
- Large single claims: surplus, fac, pool, qsxol, xol_risk, yrt (facoblig, aggxol)
- Catastrophe / accumulation: pool, xol_cat, umbrella, catbond, ilw, parametric (topdrop)
- Capacity and growth: qs, surplus, facoblig, fac, coins, bpa, sidecar (pool, fronting, yrt)
- New-business strain: coins, modco, cofw, vif (qs)
- Reserve release / exit: lpt, adc, portfolio (coins, reservefin, bpa, prudenceadc, commutation)
- Liquidity and cash: cofw, vif, parametric (surplusrelief, subloan, commutation)
- Counterparty risk: modco, cofw, commutation (catbond)
- Pricing support / know-how: yrt (qs, fac, captive)
- Market access / regulation: pool, fronting, retakaful (captive)
- Low cost of reinsurance: corridorqs, slidingqs, aggqs (xol_risk, corrsl, capqs, marginlocked, spreadloss, grossbasis, captive)
Reinsurer aims: margin / return on capital (xol_risk, xol_cat, yrt, longevity, vif, reservefin, bpa, corridorqs, slidingqs, marginlocked, adc); low-volatility income (corrsl, corridorqs, capqs, marginlocked, spreadloss); diversification (xol_risk, longevity); access / relationship (qs, surplus, fronting, yrt, capreliefqs, captive, retakaful, portfolio); investment assets (coins, bpa, lpt); fee income (contcap, sidecar); control and alignment (slidingqs, commutation).

### C1 Proportional
**qs - Quota share** (H/L/P, finite low). Reinsurer takes q of every premium and claim; pays commission for acquisition costs. Ceded = qP; recoveries = q x claims; commission = c x qP; RI result = qP(1-c) - q x claims - brokerage - tax. Flows: Cedant->RI q x premium [P] quarterly; RI->Cedant q x claims [R] quarterly or cash call; RI->Cedant commission [C]; RI->Broker brokerage [F]. Cedant: cuts net premium (MGF and other premium-based margins) and net reserves one-for-one, funds acquisition, capacity, imports know-how. RI: access at cedant's pricing, relationship anchor. Works: growing or new books, adequately priced books, premium-based tests. Weak: profitable mature books (gives away margin); loss-making books (needs loading or negative commission); retention floors (UAE 50% health/non-life, 85% group life) cap credit. Treatment: UAE credit to floor, Art 34 0.5% provision on ceded premium, reinsurer >= BBB (Art 26), 3-year retention plan (Art 27); KSA: skill `ksa-rbc-capital` file 28 and `reinsurance-pricing-knowledge` file 03; IFRS 17 para 86, 66A/70A; SII volume measures + counterparty. Add-ons: c_comm, c_slide, c_pc, c_corr, c_cap, c_fw, c_cashcall, c_basis, c_standby, c_tranche, c_portfolio, c_term. Variants: variable QS; standby tranche; NRP+loading vs gross+commission; QS + XoL on retention.
**surplus - Surplus treaty** (L/P, low). Cedant keeps one line per risk; RI takes surplus up to n lines; share_i = min(max(SI_i - line,0), n x line)/SI_i. Flows as QS by risk. Cedant keeps small-risk margin, caps net per risk. RI: large risks, admin and selection burden. Works: individual life, heterogeneous property. Weak: medical (claim size unknown up front; use per-person XoL).
**facoblig - Facultative-obligatory** (L/P, low). Cedant may cede, RI must accept. Capacity on demand; RI prices selection risk; for trusted cedants.
**fac - Facultative** (H/L/P, low). One risk negotiated (proportional share or XoL). Capacity and price discovery for large or unusual risks (corporate medical schemes, jumbo life). Costly for volumes of small risks. UAE inward business <= 49% (Art 37).
**pool - Pool / co-reinsurance** (H/P, low). Members share a class (high-cost medical cases, terror): member result = s_k x (pool premium - claims - expenses); pool buys its own XoL. Removes rare high-cost tail, stabilises community-rated pricing. Weak where claims controls differ (moral hazard).
**fronting - Fronting** (H/L/P, watch). Licensed insurer issues and cedes 90-100%, keeps fee f; credit risk on reinsurer; collateral to fronter [S]. Market access for captives, MGAs, multinationals. Gross-based charges (op risk, floors) make it capital-hungry; UAE Art 37.
**qsxol - QS with XoL on retention** (H/P, low). QS for capital, per-person XoL for large claims on (1-q) or inuring on 100%. Define inuring order or risk double counting / gaps.

### C2 Non-proportional
**xol_risk - Per-risk / per-person XoL** (H/L/P, low). Recovery per claim = min(max(X-R,0), Limit) x (1-co-participation), less AAD, capped by AAL; premium = rate x subject premium, M&D in instalments (e.g. Q1, Q3), swing or burning-cost adjustment after year-end. Flows: Cedant->RI M&D and adjustment [P]; RI->Cedant recoveries [R]; brokerage, WHT [F]. Cedant: stable net LR, cheap vs QS, high benefit limits. RI: defined-limit severity, experience rating. Weak: frequency or price-adequacy problems; little credit under premium/volume formulas (UAE none for non-prop health premium risk). Add-ons: c_aad, c_aal, c_reinst, c_swing, c_md, c_coins, c_index, c_cashcall, c_sunset, c_layers.
**xol_cat - Cat / per-event XoL** (H/L/P, low). Recovery = min(max(sum of event losses - R,0), Limit); event and hours clause; reinstatement premium. Group life / PA accumulation, pandemic cover. Medical events spread over months are hard to define. SII cat module credits directly; check local templates.
**stoploss - Aggregate stop loss** (H/P, low). Recovery = beta x min(max(L-A,0), U) x P; premium rP priced on E[recovery] + capital load; paid after the year on incurred incl. IBNR. Caps worst-year net LR; economic (1-in-200) relief. RI: tail and parameter uncertainty, moral hazard. Weak: volume/premium-based formulas give almost no credit; unlimited medical stop loss hard to place. Add-ons: c_coins, c_aal, c_sunset, c_commute, c_claimsco, c_multi.
**aggxol - Aggregate XoL** (H/P, low). Recovery on annual sum of claims above a per-claim deductible, above an aggregate retention. Fills the gap between per-claim XoL and stop loss (growing numbers of 50k-150k claims).
**umbrella - Umbrella / clash** (H/L/P, low). One event hitting several lines above underlying retentions. Composites with life, PA and medical.
**topdrop - Top-and-drop** (P, low). Unused top limit drops down for second events. Property towers.

### C3 Life and longevity
**yrt - Risk-premium basis (YRT)** (L, low). RI premium = q_x x ceded sum at risk; recovery = ceded sum at risk. Pure mortality/morbidity transfer, underwriting support. Does not fund strain. UAE group life 85% floor; long-term life credit on ceded reserves.
**coins - Coinsurance** (L, low). Share of premium, benefits, reserves and backing assets; allowance reimburses acquisition. Relieves reserve and capital strain; RI gets assets and spread. UAE long-term life full credit (no floor).
**modco - Modified coinsurance** (L, watch). Cedant keeps reserves and assets; modco adjustment = change in ceded reserve - interest on it [S]. No counterparty risk on reserves; credit depends on regime; Art 25 test.
**cofw - Coinsurance with funds withheld** (L, watch). FW balance = ceded reserves credited at rate i; net settlement. Keeps assets and cuts credit risk; finite if credited rate fixed and RI cannot lose.
**longevity - Longevity swap** (L, low). Cedant pays fixed leg (expected benefits x (1+fee)), RI pays actual benefits; two-way collateral. Large capital release in longevity regimes.
**masslapse - Mass lapse cover** (L, low). Recovery = min(max(lapse - threshold,0), limit) x amount per lapse. Cuts the mass-lapse shock (unit-linked, savings).
**vif - VIF monetisation / NB financing** (L, high). RI pays advance A day 1 [C], recovered from future profits of the block [P]; written off if experience is bad. Funds strain, converts VIF to own funds where admitted. Guaranteed repayment = loan: UAE Art 25 (KSA: skill `ksa-rbc-capital`); IFRS 17 may be a deposit.
**reservefin - Reserve financing** (L, high). RI takes statutory reserve above best estimate, funded by LoC/trust [S]; fee [F]. Only in prudent-reserve regimes and only with genuine risk; nil effect under IFRS 17 / SII.
**lifecoins - Long-term life coinsurance releasing prudence** (L, watch). Ceded = share x statutory reserve, priced at best estimate + margin; release ~ ceded x (1 - 1/(1+prudence)) - margin. Needs genuine mortality/lapse transfer; not for group life (85% floor).
**bpa - Asset-intensive / bulk annuity (funded) reinsurance** (L, low). Single premium in assets; RI reimburses annuities; collateral for recapture. Capacity for buy-ins; regulators watch funded-reinsurance concentration.

### C4 Structured and finite
**corrsl - Corridor QS with unlimited aggregate stop loss** (H, low). q% QS subject to a (B-A)% xs A% corridor, QS liability ceases at B%, unlimited stop loss xs B%. R_QS = q x min(L,A); corridor K = min(max(L-A,0), W), W = B-A (cedant 100%); R_SL = min(max(L-B,0), U). Net N(L): L<=A (1-q)L; A<L<=B (1-q)A + (L-A); L>B constant B - qA. Cedant net premium P[(1-q) - r + cq]; RI QS result q(1-c) - q min(L,A); RI SL result r - max(L-B,0). Crossover vs straight QS L* = (B-qA)/(1-q); better at the 1-in-200 iff q < (L200-B)/(L200-A). At 1-in-200 (L200 >= B): QS transfers qA, SL transfers L200-B; residual capital = corridor W + retained QS share + SL counterparty charge; SL limit irrelevant to 1-in-200 capital if U >= L200-B. Base case A 95%, B 115%, L200 135%: threshold q 50%; q 30/40/50/60/70% gives cap 86.5/77.0/67.5/58.0/48.5% vs straight QS net at L200 94.5/81.0/67.5/54.0/40.5%, L* 123.6/128.3/135.0/145.0/161.7%. Flows: Cedant->QS RI qP [P]; QS RI->Cedant cqP [C] and q min(L,A)P [R]; Cedant->SL RI rP [P]; SL RI->Cedant max(L-B,0)P [R] after the year. Pricing: SL r = E[max(L-B,0)](1+loadings) + cost of capital on the tail; unlimited SL priced on the whole tail beyond L200; QS reinsurer can pay higher c because its LR is capped at A. Placement: expect counter-offers of limit U, LR cap, co-participation beta, or M&D with adjustable rate; moral hazard (net flat above B) needs co-participation, claims control, profit commission; SL counterparty rating and collateral drive credit; same definitions (UW year, premium base, IBNR, LAE) in both contracts; keep any sliding scale below A. UAE: QS credited to floors; corridor and SL give little template credit; value visible on 1-in-200 basis; Art 25 substance requires QS reinsurer exposure below A. KSA: skill `ksa-rbc-capital`, file 28.
**corridorqs - Loss-corridor QS** (H/P, watch). Kept = s x min(max(L-A,0), B-A) x ceded premium; recoveries reduced by it. Lowers QS price, keeps premium credit. Sizing for transfer: width <= L200 - (1 - brokerage - tax) - X, X = loss RI must still suffer at 1-in-200. A corridor starting well below expected LR is pre-funding (finite).
**capqs - QS with LR cap** (H/P, high). Recoveries = q x min(L, cap) x P. Caps near the 1-in-200 fail tail tests and remove economic benefit; caps far above rarely bite.
**slidingqs - QS with sliding-scale commission** (H/P, watch). c(L) = c_max for L <= L1, c_min for L >= L2, linear between; provisional then trued up. UAE Art 27 permits sliding and profit commissions; contingent commission sits with recoveries under IFRS 17.
**aggqs - Aggregate (LR-triggered) QS** (H, low). No cession below trigger x; RI pays q x min(max(L-x,0), w) x P; fixed premium = E[recovery]/(1 - brokerage - tax - margin) plus capital load in practice. Cheapest cut in the 1-in-200 per unit of cost; passes every risk-transfer test; almost no credit under volume formulas; reject the switch-on variant (whole year ceded once triggered: cliff and disputes).
**marginlocked - Margin-locked QS** (H, high). F = 1 - brokerage - tax - m; U = alpha-quantile of L; L0 = (1-alpha)-quantile; corridor F to U, or sliding commission F - L0 at L0 to F - U at U. RI earns m in alpha of years; ERD ~ 0 so finite under ERD; a 99.5% design fails T1 by construction. Corridor and sliding versions cost the cedant the same.
**surplusrelief - Surplus-relief QS (UPR commission)** (H/P, high). Day-1 gain = UPR ceded x commission rate (own funds where DAC is nil); year-end true-up final commission = UPR x max(0, 1 - LR - margin). Bridge for thin own funds; unwinds as UPR earns; guaranteed return = loan; IFRS 17 spreads commission (nil day-1 equity).
**capreliefqs - Capital-relief QS with standby / automatic tranche** (H, low). Base cession at the floor plus a tranche switched on (or automatic: e.g. +2 pts cession per 1 pt of cover below trigger) at lower commission. Dial on MGF or another premium-based margin; no effect if MCR binds.
**lpt - Loss portfolio transfer** (H/P, watch). RI takes existing reserves for a price; statutory gain = ceded x (1 - price) where reserves are prudent; IFRS 17 para 65A expenses net cost (a gain is deferred in the CSM). Needs prior approval (UAE Decree-Law 6/2025 Art 125(1)); finite if price far below reserves without risk.
**adc - Adverse development cover** (H/P, low). Recovery = min(max(ultimate - attachment,0), limit) for past years. Caps reserve deterioration, pre-sale certainty; approval needed.
**prudenceadc - Prudence-layer ADC** (H/P, watch). Attaches at best estimate, exhausts at statutory reserve; own funds + layer - premium where the recoverable is valued on the prudent basis; genuine but limited risk.
**spreadloss - Spread-loss / experience account** (H/P, high). Account_t = Account_t-1 (1+i) + premium - margin - losses; balance returned at expiry, deficit borne up to a limit. Usually finite: prohibited in UAE (and in KSA: skill `ksa-rbc-capital`) unless RI has real chance of significant loss.
**multiyear - Multi-year aggregate** (H/P, watch). One aggregate limit over years/lines; cheaper via time diversification; one-year capital regimes may credit only the current year.
**grossbasis - NRP + loading vs gross + commission** (H, low). Equivalence GWP(1-c) ~ NRP(1+loading) at break-even; WHT and brokerage apply to the larger gross ceded premium (confirm WHT base); premium-risk volume = GWP - ceded premium (commission not deducted) so gross gives more volume credit; IFRS 17 para 86 nets non-contingent commission; gross exposes the cedant's loading and passes its pricing changes to reinsurers; commission above actual acquisition cost reads as financing.

### C5 Capital and ILS
**contcap - Contingent capital / LoC** (H/L/P, low). Commitment fee [F]; capital on draw [S]. UAE ancillary own funds count 50% for SCR and MGF with approval, 0% for MCR (Decision 25/2014).
**subloan - Subordinated loan / surplus note** (H/L/P, low). Principal in, coupon out; counts as own funds with approval (possibly MCR if Tier 1-like); UAE Art 142(2)(e) CBUAE may stop coupons. The external fix for MCR / BOF gaps; can be packaged with a QS by the same reinsurer.
**sidecar - Sidecar** (P/L, low). Investor-funded SPV takes a QS, fully collateralised; sponsor earns override and profit share.
**catbond - Cat / mortality bond** (P/L, low). SPV notes; principal pays on indemnity, index or parametric trigger; multi-year, no counterparty risk, basis risk with index triggers.
**ilw - Industry loss warranty** (P, low). Fixed pay-out if industry loss >= trigger (and own loss).
**parametric - Parametric cover** (H/L/P, low). Pay-out = f(index), cash within days; basis risk; may not count as reinsurance without indemnity.

### C6 Vehicles and transfers
**captive - Captive / protected cell** (H/L/P, low). Parent's employee medical fronted locally, ceded to captive, captive buys XoL/stop loss.
**retakaful - Retakaful and qard hasan** (H/L, low). Participants' fund cedes to retakaful [P], receives recoveries and commission [R]; deficits funded by qard hasan from shareholders [S], repaid from later surpluses. UAE Decision 26/2014: commissions land in the participants' fund.
**portfolio - Portfolio transfer / novation** (H/L/P, low). Policies move to an acquirer with approval; full release.
**commutation - Commutation** (H/L/P, low). Single payment = PV of outstanding recoverables - discount; removes counterparty, releases RI capital.

### C7 Placement realities common to all structures
Reinsurers need about a 3% margin on premium; brokerage QS ~2.5%, XoL 5-10%, stop loss ~10%; KSA withholding tax and local first refusal (`reinsurance-pricing-knowledge`, file 03); UAE reinsurer >= BBB, Art 34 0.5% provision, Art 37 inward <= 49%; remote tail layers are priced on capital and can quote several times expected loss.

### C8 Clauses and components (combine with C1-C6)
- c_comm flat ceding commission: c x ceded premium; above acquisition cost with repayment = finite.
- c_slide sliding-scale commission: c(L) between c_max at L1 and c_min at L2; provisional then true-up; UAE Art 27 permits.
- c_pc profit commission: s x max(0, ceded premium(1-e) - commission - recoveries - deficit b/f); unlimited carry-forward traps the cedant.
- c_corr loss corridor: kept = s x min(max(L-A,0), B-A) x ceded premium; keep it above expected LR.
- c_cap LR cap / aggregate limit on a QS: recoveries <= cap x ceded premium; low caps fail tail tests.
- c_coins co-participation beta in a layer: mitigates moral hazard above a retention.
- c_aad annual aggregate deductible; c_aal annual aggregate limit; c_reinst reinstatements (paid pro rata to amount); c_md minimum and deposit premium.
- c_swing swing rate / burning cost: final rate = min(max(layer losses / subject premium x loading (e.g. 100/90), min), max).
- c_fw funds withheld / premium deposit: cedant keeps premium, credits interest, settles net; liquidity and counterparty benefit; guaranteed deposit return with interest = loan; UAE Art 28.
- c_coll collateral (trust, LoC): exposure = max(recoverables - collateral credit, 0) (UAE stylised template 80% credit).
- c_cashcall cash call / simultaneous settlement; settlement days affect UAE recoverable admissibility (REINS-2: 100% to 180 days, 75% to 270, 50% to 360, nil after).
- c_sunset reporting deadline (e.g. 30 months); c_hours event definition; c_claimsco claims cooperation / control; c_index stability clause (R_t = R_0 x index_t / index_0).
- c_multi multi-year term; c_commute commutation clause; c_rateguar rate guarantee; c_interest interest credit on FW / modco; c_expacc experience account (usually finite).
- c_basis premium basis (NRP / GWP / GEP / NEP): same definition in every contract; c_frictions brokerage and WHT.
- c_standby standby tranche (elected at quarter-end); c_tranche coverage-linked automatic tranche; c_portfolio portfolio entry / withdrawal (clean cut vs run-off); c_term special termination (downgrade, change of control); c_layers layering; c_inure inuring order (for the cedant's account vs inures to the benefit of); c_trigger trigger design (indemnity, index, parametric, solvency).
