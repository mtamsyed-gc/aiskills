# KSA RBC: Counterparty default risk module

Type 1 (reinsurers, banks), Type 2 (brokers, agents, TPAs, policyholders), the catastrophe risk-mitigating effect and the aggregation. The reinsurer charge on any treaty starts here.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 5. Counterparty default risk module [Counterparty Default sheet]

Scope: loss from default of counterparties. Receivables from the KSA Government are excluded (unless there are known disputes).

### 5.1 Type 1 — reinsurers, banks and other financial institutions

| Rating | Stress factor | Risk-mitigating-effect multiplier (= 50% × factor) |
|---|---|---|
| AAA | 1.5% | 0.75% |
| AA | 1.5% | 0.75% |
| A | 5% | 2.5% |
| BBB | 5% | 2.5% |
| BB | 50% | 25% |
| B | 50% | 25% |
| Other (incl. unrated) | 50% | 25% |

Inputs per counterparty row (up to 300 rows): type, name, rating; for banks/financial institutions — deposits (incl. term deposits) `Dep`; for reinsurers — discounted ceded technical provisions (claim reserves + UPR, **net of RA**) `CTP`, ceded pipeline claims `Pipe`, reinsurance commission `Comm`, share of risk-mitigating effect in CAT scenarios `RME`; for all — collateral/guarantee `Coll`, payable to the counterparty `Pay`, expected credit loss `ECL`.

```
GrossExposure = (CTP + Pipe + Comm − ECL)   if Reinsurer
              = (Dep − ECL)                 otherwise
NetExposure   = GrossExposure − Pay − Coll                               (reported; not used in the loss)
GrossLoss     = Factor(rating) × GrossExposure + [Reinsurer only] Multiplier(rating) × RME
NetLoss       = max( GrossLoss − Pay − Coll , 0 )
Type1_gross = sqrt( Gᵀ · M17 · G ),  Type1_net = sqrt( Nᵀ · M17 · N )
   M17: 1 on the diagonal, 0.25 between any two different counterparty rows
   ⇒ closed form: sqrt( 0.75 × Σ x_i² + 0.25 × (Σ x_i)² )
Charge_Type1 = Type1_net                                                  [C11]
```

Rules:
- Payables may be entered only if (i) the company has a legal right of offset against the receivables, and (ii) the receivables from the counterparty fall due before the payables.
- Ceded technical provisions are net of RA: on a reinsurer default the company bears ceded claim reserves and unearned ceded premium only, and RA/CSM already receive credit in available capital.
- `RME` per reinsurer = (reinsurer's % share of total assumed recoveries in the CAT scenarios) × (diversified risk-mitigating effect from all CAT scenarios, `TotalRME`).
- `TotalRME` [C8] = sqrt( Σ_s Rec_s² ), where `Rec_s` is the total reinsurance recovery assumed in scenario s, for s ∈ {health pandemic (health + life), flood (KSA + outside), earthquake (KSA + outside), hail (KSA + outside), sandstorm, man-made property (property + health + P&S), energy, motor, marine, aviation, credit & suretyship}.
- Check: Σ RME over reinsurers must be within 1% of TotalRME.

### 5.2 Type 2 — other counterparties

| Counterparty | <90 days past due | 90–180 days | >180 days |
|---|---|---|---|
| Broker | 15% | 45% | 90% |
| Agent | 15% | 45% | 90% |
| TPA | 3.75% | 7.5% | 15% |
| Policyholder | 3.75% | 7.5% | 15% |
| Insurance Company | 3.75% | 7.5% | 15% |
| Others | 3.75% | 7.5% | 15% |

Inputs per counterparty row (up to 300): type, name, receivables **net of ECL** in each ageing bucket `R1, R2, R3`, payables `Pay`.

```
GrossLoss = f1 × R1 + f2 × R2 + f3 × R3
NetLoss   = max( GrossLoss − Pay , 0 )
Charge_Type2_gross = Σ GrossLoss  [D9]        Charge_Type2 = Σ NetLoss  [D11]      (no diversification)
```

Rules:
- Ageing starts immediately from the payment due date, not from the end of any grace period.
- Follow the counterparty classification and balances in the company's SOFP.
- Salvage and subrogation receivables (including IBNR, positive or negative) belong in Type 2, split by counterparty.
- Payables: same two offset conditions as Type 1.

### 5.3 Aggregation

```
Charge_CD = sqrt( T1² + T2² + 2 × 0.75 × T1 × T2 )        (M4)
```
