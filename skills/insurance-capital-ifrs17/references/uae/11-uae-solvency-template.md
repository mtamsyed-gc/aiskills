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
