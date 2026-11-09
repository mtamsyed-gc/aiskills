# Qatar (QFC): MCR, SRR, eligible capital, risk-based capital and the INS600/INS610 template

**Sources:**
- **[RULE]:** PINS V20 Chapters 3-4 and Schedule 3.
- **[TEMPLATE]:** the QFCRA INS prudential return workbook (taxonomy 2.0.0), forms INS600 and INS610.x.

Factors below were checked in Nov 2026 against both the rule text and the template formulas. Where they differ, see §6.

## 1. Architecture [RULE]
Applies to QFC-incorporated insurers only; not branches or captives (file 30 §2).

| Test | Requirement | Rule | Consequence of breach |
|---|---|---|---|
| **MCR** | Eligible capital ≥ **max(QAR 36m, risk-based capital requirement)** | 3.2.1, 3.3.1 | Stop writing new business |
| **SRR** (from 1 Aug 2024) | Eligible capital ≥ **150% × risk-based capital requirement**. The Authority may set a different SRR, taking account of: retail or catastrophe volatility, market importance, investment geography, risk management, ORSA, strategy and rating | 3.3.2A | Board-approved action plan; no stop-writing |
| Firm-specific | The Authority may impose a higher MCR as a licence condition (3.3.1 note 2) | | |

**Which test binds [INTERP]:**
- SRR binds whenever 1.5 × RBC > max(36m, RBC). That means whenever **RBC > QAR 24m**.
- Below QAR 24m RBC the QAR 36m floor binds. There, reducing RBC creates **no** headroom.
- From QAR 24m RBC upwards, each QAR 1 of RBC saved frees **QAR 1.5** of required capital.
- Always state both covers: eligible ÷ MCR, and eligible ÷ (1.5 × RBC).

**Risk-based capital requirement (RBC)** (3.4.1):
- **RBC = IRR + InsRR + ORR**: investment risk + insurance risk + operational risk.
- **Simple sum: no correlation or diversification credit.**
- An internal model approved by the Authority can replace the whole RBC or individual components (3.8). The insurer's home or group regulator must also have approved it.
- [TEMPLATE] INS610 L17 holds the internal-model figure. L18 MCR = MAX(base, RBC, internal model).

## 2. Eligible capital (4.2.2 table) [RULE] = template INS600
| Line | Item | Notes |
|---|---|---|
| A Tier 1 | Permanent share capital | Fully paid, undated, non-cumulative, first loss (4.3.1(a)) |
| | Audited reserves | Retained profits after tax and dividends. Includes capital contributions meeting (a), notified 1 month ahead (4.3.1(b)-(c)) |
| | Share premium | |
| | Externally verified interim net profits | **Auditor-verified only** (4.3.1(e)). Unverified quarter profits do not count |
| | Fund for future appropriations | |
| | Owners' equity | **Takaful only** |
| B Deductions from tier 1 | Own shares; **intangibles** (goodwill, capitalised development, brands, licences); interim net losses | Cumulative losses and negative reserves are deducted (4.3.1(i)) |
| C | Tier 1 after deductions = A − B | |
| D Upper tier 2 | Perpetual qualifying hybrids (unsecured, subordinated, perpetual, loss-absorbing); fixed-dividend ordinary shares | 4.4.1 |
| E Lower tier 2 | Subordinated debt; fixed-term preference shares | Sub debt conditions in 4.4.2. **≥5-year original maturity**; no step-ups in the first 5 years; no payment while in MCR breach; 30-day no-objection notice. **Amortised 20% a year over the last 4 years** (4.4.3). External legal opinion needed (4.5.1) |
| Limits | **Lower T2 ≤ 50% of C** (4.7.2); **total T2 ≤ 100% of C** (4.7.1) | [TEMPLATE] INS600 L18 = ROUND(MIN(L16+L17, L12/2)); L19 = MIN(L15+L18, L12) |
| G Deductions from T1+T2 | Investments in subsidiaries and associates; connected lending of a capital nature; **inadmissible assets**; zakah fund (takaful) | 4.6 |
| H | **Eligible capital = C + D + E − G** | INS600 L26 → INS610 L19 |

**Inadmissible assets** (4.6.4), deducted in full:
- tangible fixed assets, including inventories, plant, equipment and vehicles;
- **deferred acquisition costs**;
- **deferred tax assets**;
- deficiencies of net assets in subsidiaries;
- a subsidiary's holding of the insurer's own shares;
- investments not readily realisable.

Assets deducted here carry **no** asset risk charge (A3.2.4).

**There is no ancillary-capital tier.** Letters of credit, guarantees and uncalled capital do not appear in the table. The Authority may recognise other instruments that meet international standards (4.2.1 guidance). **[INTERP]:** an LoC is not capital without specific QFCRA recognition. It can still reduce asset risk as collateral or guarantee (A3.2.2).

## 3. Risk-based capital: module by module [RULE, Schedule 3]
### 3.1 Counterparty grades (A3.1.1-A3.1.2)
| Grade | S&P / Fitch | Moody's | AM Best |
|---|---|---|---|
| 1 | AAA | Aaa | A++ |
| 2 | AA+ to AA- | Aa1-Aa3 | A+ |
| 3 | A+ to A- | A1-A3 | A, A- |
| 4 | BBB+ to BBB- | Baa1-Baa3 | B++, B+ |
| 5 | BB+ and below | Ba1 and below | B and below |

- **Unrated = grade 4.**
- Use one agency consistently. If ratings differ, **use the one giving the highest charge**.
- Only the four listed agencies may be used, unless the Authority permits another.

### 3.2 Investment risk requirement (IRR) = asset + off-balance-sheet asset + off-balance-sheet liability components (3.5.1)
**Asset risk** = Σ value × factor (A3.2.1). INS610.10 lines 1-43.

| Factor | Non-reinsurance assets (Table A3.2.1A) |
|---|---|
| 0.5% | Cash, bank deposits and cash equivalents; grade 1 sovereign bonds |
| 1% | Bonds < 1 yr (grade 1-2); cash management trusts (grade 1-2) |
| 2% | Unpaid premiums ≤ 6 months due from grade 1-3 counterparties; bonds ≥ 1 yr (grade 1-2) |
| 4% | Unpaid premiums ≤ 6 months (unrated or grade 4-5); bonds grade 3; cash management trusts grade 3; secured loans |
| 6% | Unpaid premiums > 6 months (grade 1-3); bonds grade 4; cash management trusts grade 4 |
| 8% | Unpaid premiums > 6 months (unrated or grade 4-5); bonds grade 5; cash management trusts grade 5; listed subordinated debt |
| 10% | Unlisted subordinated debt; preference shares |
| 16% | Listed equity (includes collective investment funds, joint ventures, mudaraba/musharaka certificates per the glossary); listed trusts |
| 20% | Real estate (direct); unlisted equity; unlisted trusts; **any other non-reinsurance asset** |
| 100% | Loans to directors (and their related parties or dependants); unsecured staff loans (except under QAR 3,600); assets under a fixed or floating charge |

**Reinsurance assets** (Tables A3.2.1B/C):

| Grade | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Reinsurer supervised by a "subrule (2) regulator" | 1% | 2% | 4% | 6% | 8% |
| Reinsurer not supervised by one | 1.2% | 2.4% | 4.8% | 7.2% | 9.6% |

- **Subrule (2) regulators:** Qatar, EU member states, Australia, Canada, Hong Kong, Iceland, Japan, Norway, Singapore, Switzerland, USA, **or any signatory of the IAIS Multilateral MoU**.
- **[INTERP]:** most GCC regulators that have signed the IAIS MMoU qualify. **VERIFY** the signatory list on the date of use.

**Asset risk adjustments:**
- **Guarantee** (A3.2.2(1)): explicit, unconditional and irrevocable for the full term, from an unrelated guarantor rated grade 1-3. The asset takes the guarantor's charge.
- **Collateral** (A3.2.2(2)): cash or grade 1-3 debt. The covered part takes the collateral's charge.
- **Charged or mortgaged assets** (A3.2.3): 100% charge to the extent of the secured debt. If the security backs insurance liabilities, only the excess of market value over the supported liabilities is charged.

**Off-balance-sheet asset risk, derivatives** (A3.4):
- Excluded: put options serving as guarantees; FX contracts with original maturity ≤ 14 days; exchange-traded contracts that are marked to market daily.
- **Rule:** asset-equivalent value × the counterparty's asset-risk %, where asset-equivalent value = positive MTM + notional × add-on.

| Add-on | IR | FX & gold | Equity | Precious metals (not gold) | Other |
|---|---|---|---|---|---|
| < 1 yr | 0 | 1% | 6% | 7% | 10% |
| 1-5 yrs | 0.5% | 5% | 8% | 7% | 12% |
| ≥ 5 yrs | 1.5% | 7.5% | 10% | 8% | 15% |

**Off-balance-sheet liability risk** (A3.5):
- Face value of credit substitutes issued (LoCs, guarantees, put options serving as guarantees) × the asset charge of the underlying obligation.
- Collateral and guarantee relief applies.
- Credit and surety **insurance** is not a credit substitute.

### 3.3 Insurance risk requirement (InsRR) = premium + outstanding claims + long-term + concentration (3.6.1)
**Premium risk** (A3.7, general business):
- **Net premium liability** by PINS category × factor.
- Net premium liability = premium liability (8.6.7: the value of future claims and settlement costs on in-force cover) less expected reinsurance and other recoveries.

**Outstanding claims risk** (A3.8):
- **Net outstanding claims liability** (8.6.8: reported claims, IBNR and loss adjustment expenses, less expected recoveries) × factor.

| PINS cat | Premium: direct | Premium: prop. reins. | Premium: non-prop. reins. | Claims: direct | Claims: prop. | Claims: non-prop. |
|---|---|---|---|---|---|---|
| 1 (accident, sickness) | **16%** | 18% | 21% | **11%** | 12% | 14% |
| 2 | 13% | 15% | 18% | 9% | 10% | 12% |
| 3 | 16% | 18% | 21% | 11% | 12% | 14% |
| 4 | 21% | 23% | 26% | 14% | 15% | 17% |

- **The factors apply to NET liabilities, with no net/gross floor.** Contrast the UAE 50% floor.
- **The "reinsurance" columns are for inward reinsurance written**, by type. They are not a credit for outward cover.
- **Lower factors on application for medical business (lever):**
  - **PINS 1 premium factors** can be reduced with written consent where mortality and morbidity data support actuarial reliance. Floor: **12%** (direct and proportional), **16%** (non-proportional) (A3.7.3).
  - **Outstanding-claims factors** for any category can be reduced the same way, to a floor of **8%** (A3.8.3).
- Long-term contracts in PINS 1 use the long-term component instead (A3.7.4, A3.8.4).

**Long-term insurance risk** (A3.9) = Σ of:

| Item | Factor |
|---|---|
| Provisions: investment-linked with capital guarantee | 1.25% |
| Provisions: investment-linked without guarantee | 0.5% |
| Provisions: all other long-term business | 3% |
| Capital at risk (CAR) | **0.1%** |
| Mortality-contingent policies | Claims cost of a **+0.5 per mille** increase in the death rate over the next year |

- **CAR** = sums assured less mathematical reserves less **expected reinsurance recoveries**, floored at 0 per contract. For annuities, the sum assured is the PV of the annuity payments.
- [TEMPLATE] INS610.60 implements the mortality item as **0.05% × CAR of mortality-contingent policies**.
- **Whether "provisions" are gross or net of reinsurance is not stated.** VERIFY in the return instructions.

**Insurance concentration risk** (A3.10, general business):
- Charge = **MER + CoR − RP**.
  - **MER**: the maximum event retention net of reinsurance, for a single extreme event, at a **≥ 1-in-250** return period. Take the largest MER across events. The approved actuary's advice is required for portfolios that are unlimited, multi-line or complex.
  - **CoR**: the contractual (or estimated, but not below the original rate) cost of one reinstatement.
  - **RP**: inward reinstatement premiums under binding netting arrangements, for insurers that write reinsurance.
- Guidance names medical insurers: common-source claims (for example, a class action from one faulty procedure in a large scheme) are concentration risk even without a natural catastrophe.

### 3.4 Operational risk requirement (ORR) (3.7.1)
- **ORR = min[ 2% × max(GWP over the last 12 months, gross technical provisions), (IRR + InsRR) × 15/85 ]**.
- **The basis is gross, but the cap moves with net risk.** For an insurer whose cap binds, cutting InsRR also cuts ORR.

## 4. Worked example (QAR '000, illustrative; medical-focused QFC LLC)
**Inputs and asset risk:**

| Asset | Value | Factor | Charge |
|---|---|---|---|
| Cash and deposits | 150,000 | 0.5% | 750 |
| Bonds, grade 2, ≥ 1 yr | 100,000 | 2% | 2,000 |
| Listed equity | 30,000 | 16% | 4,800 |
| Unpaid premiums ≤ 6 months, unrated | 40,000 | 4% | 1,600 |
| Reinsurance assets, grade 3, supervised | 60,000 | 4% | 2,400 |
| **IRR** | | | **11,550** |

**Insurance risk:**
- Net premium liability PINS 1, direct: 50,000 × 16% = 8,000.
- Net outstanding claims PINS 1, direct: 70,000 × 11% = 7,700.
- Concentration: MER 5,000 + CoR 1,000 = 6,000.
- **InsRR = 21,700.**

**Operational risk:**
- 2% × max(GWP 300,000; gross technical provisions 220,000) = 6,000.
- Cap = 33,250 × 15/85 = 5,868.
- **ORR = 5,868** (the cap binds).

**Result:**
- **RBC** = 11,550 + 21,700 + 5,868 = **39,118**.
- **MCR** = max(36,000; 39,118) = 39,118.
- **SRR** = 1.5 × 39,118 = **58,677**.
- **Eligible capital** = share capital 60,000 + audited reserves 20,000 − intangibles 2,000 − inadmissible assets (DTA 500, fixed assets 1,500) 2,000 = **76,000**.
- **Cover:** MCR 194%; SRR 130% (= 194% / 150%). **SRR binds**, with headroom of 17,323.

**Adding a 30% medical quota share** (reinsurer grade 3, supervised; premium and claims liabilities ceded pro rata):
- Premium risk: 35,000 × 16% = 5,600.
- Claims risk: 49,000 × 11% = 5,390.
- InsRR = 16,990, assuming MER unchanged.
- Reinsurance assets rise by 36,000, at 4% = +1,440. IRR = 12,990.
- Cap = 29,980 × 15/85 = 5,291. **ORR = 5,291** (falls, because the cap binds).
- **RBC = 35,271** (−3,847). **SRR = 52,907.** Required capital falls by **5,770**.

Ignored here: cash ceded, commission, and IFRS 17 effects (file 33). Ceding to an unsupervised reinsurer would cost 4.8% instead of 4% on the recoverable.

## 5. Template map (INS workbook) [TEMPLATE]
Calculation order:

INS610.10 → .20 → .30 → .40 → .50 → .60 → .70 → INS610 → (with INS600) result.

| Form | Content | Feeds |
|---|---|---|
| INS600 | Eligible capital L1-L26 | INS610 L19 |
| INS610.10 | Asset risk: 28 non-reinsurance lines + 10 reinsurance lines (supervised and unsupervised, by grade). H = ROUND(value × factor) | INS610 L3 |
| INS610.20 | Derivative add-on grid (5 contract types × 3 maturities) | L4 |
| INS610.30 | Credit substitutes: value × manually entered %, per row | L5 |
| INS610.40 / .50 | Net premium liability / net outstanding claims, by PINS category 1-4 × direct / prop. / non-prop. | L7 / L8 |
| INS610.60 | Long-term (hidden if no long-term business) | L9 |
| INS610.70 | Concentration: cat cover yes/no | L10 |
| INS610 | L1 type (LLC or branch, from DECLARATIONFORM), L2 base capital 36,000 (branch 0); L6 IRR, L11 InsRR, L12-L15 ORR with cap; L16 RBC; L17 internal model; **L18 MCR = MAX(L2, L16, L17)**; L19 eligible capital; **L20 = L19 − L18** | Result |
| INS620 | Intermediary capital (base QAR 1.8m with client money / 0.9m without / 0.18m captive manager; paid-up capital test; adjusted net assets ≥ 50% of base) | Standalone, not the insurer test |

**Related disclosure forms (no formula feed into RBC):**
- INS100 balance sheet;
- INS130 investment concentration and geography;
- INS300 premiums by line of business, location, channel and fac/treaty;
- INS320 claims by line of business;
- INS340 reinsurance (10 largest reinsurers with rating and collateral; treaty limits and retentions by line);
- INS350 largest clients;
- INS700.10 intra-group.

**Every capital input is keyed by hand.** No formula links INS300, INS320 or INS100 to INS610.x. The filer must reconcile them.

## 6. Template vs rule: points to watch (VERIFY with the QFCRA return instructions)
1. **SRR is not computed in the workbook.** L20 shows only the surplus over MCR. Compute **eligible − 1.5 × L16** separately. A positive L20 can coexist with an SRR breach.
2. **INS610.70 has a fallback the rule does not contain.** If there is no cat reinsurance, the charge is **2 × largest per-risk retention**. This presumably comes from the return instructions. With cat cover: MER + CoR − RP, as in the rule.
3. **INS610.20 applies the add-on % to notional as the charge.** The rule adds positive MTM and then applies the counterparty's asset-risk %. Follow the instructions of the version filed.
4. **INS610.60 uses 0.1% CAR and 0.05% × mortality-contingent CAR.** This matches A3.9.2(d)-(e) as an approximation. Line 1 "annuity and pensions" uses 3%, matching (c).
5. **Prior-period comparatives carry hard-coded dates.** Do not treat them as linked.
6. **ORR GWP and gross technical provisions are entered by hand,** not pulled from INS200 or INS300.
