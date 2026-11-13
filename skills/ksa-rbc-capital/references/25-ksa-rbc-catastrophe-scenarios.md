# KSA RBC: Catastrophe scenarios

Health pandemic, natural catastrophe (flood, earthquake, hail, sandstorm, windstorm) and man-made catastrophe (property fire, energy, motor, marine, aviation, credit and suretyship). Note for life and health books: the property-fire scenario and the sandstorm scenario both carry health and life losses, not only pandemic.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## 8. Catastrophe scenarios [Scenarios sheet]

General rules:
- A scenario may hit several lines; the company reflects every relevant impact (e.g. a life-only insurer exposed to the man-made property fire scenario considers deaths at its largest concentration of insured lives under a group policy).
- Exposure measure is **sum insured** (not PML), "unless a lower sub-limit applies for this CAT event".
- Reinsurance recoveries, reinstatement premiums and sliding-scale commission refundable are company inputs based on existing reinsurance.
- Generic net-of-reinsurance relation for every scenario/segment:
  `NetLoss = GrossLoss − ReinsuranceRecovery + ReinstatementPremium + SlidingScaleCommissionRefundable [− Salvage, motor only]`.
- The values carried to the RBC are the **after reinsurance, after geographical diversification** figures.
- The company documents the assumptions used for each scenario.

### 8.1 Health pandemic

Health portfolio (exposure: number of insured lives `N_h`; exclude Visitor Visa, Tourism Visa and Umrah products because pandemic is an exclusion there):

| Parameter | Value |
|---|---|
| Insureds infected | 2% |
| Rejection ratio (fall under Unified Health Insurance Policy exclusions) | 95% |
| Of infected: require hospitalisation | 10% |
| Of infected: require physician consultation | 90% |
| Cost of hospital treatment per patient | SAR 15,000 (15 in SR '000) |
| Cost of testing and physician consultation per patient | SAR 550 (0.55 in SR '000) |

```
GrossLoss_health = N_h × 2% × (1 − 95%) × (10% × 15 + 90% × 0.55)      [SR '000]  = N_h × 0.001995
NetLoss_health   = GrossLoss_health − Recovery + ReinstatementPremium + SlidingScaleCommission
```

Short-term group life (exposure: number of life-years `N_l`, average sum at risk `SAR_avg`; only where policy terms do not exclude pandemic death):

```
GrossLoss_life = N_l × SAR_avg × 0.06%
NetLoss_life   = GrossLoss_life − Recovery
Charge_Pandemic = NetLoss_health + NetLoss_life            (simple sum)
```

### 8.2 Natural CAT — common mechanics

Within KSA: `Loss = RegionWeight × BaseFactor × SumInsured` per LOB and region; regional losses (summed over LOBs) are aggregated with the peril's regional correlation matrix.

Outside KSA: `Loss_region = PremiumFactor × EarnedPremium_region` where EarnedPremium is the **premium earned during 2025** (past 12 months) for risks in that region; 18 regions (Appendix B); regional multiplier = 1 for every region. Diversification:

```
Outside_div = (Σ_r L_r) × ( 0.5 + 0.5 × Σ_r L_r² / (Σ_r L_r)² )          (0 if Σ = 0)
Peril_total = sqrt( KSA_div² + Outside_div² )
```

The calculation is run twice: on gross losses (before reinsurance) and on net losses (after reinsurance). The undiversified figure is the plain sum of regional losses.

### 8.3 Pluvial flood

Base factor within KSA 0.10% of sum insured; outside KSA 110% of earned premium.

| KSA region | Western | Central | Eastern | Northern | Southern |
|---|---|---|---|---|---|
| Risk weight | 4 | 2 | 1 | 1 | 4 |
| Effective % of sum insured | 0.40% | 0.20% | 0.10% | 0.10% | 0.40% |

LOBs within KSA and exposure:
- Property: sum insured **on the ground floor** × (1 + 10% business interruption uplift). Sum insured on higher floors is collected but carries zero weight.
- Onshore marine: sum insured.
- Energy: sum insured × (1 + 10% business interruption uplift).
- Engineering: sum insured.
- Motor: sums insured under Motor Comprehensive policies; net loss also deducts salvage.

Outside KSA segments: property, onshore marine, energy, engineering, motor vehicle — each 110% × earned premium by region.
Regional correlation within KSA: Matrix 11.

### 8.4 Earthquake

Scenario: Red Sea fault line, north-western KSA. Base factor within KSA 0.10% of sum insured; outside KSA 120% of earned premium.

| Location | Haql | Qiyal | Neom | Tabuk |
|---|---|---|---|---|
| Risk weight | 8 | 5 | 3 | 3 |
| Effective % of sum insured | 0.80% | 0.50% | 0.30% | 0.30% |

LOBs: property, energy, engineering (within KSA: sum insured by location, no BI uplift; outside KSA: earned premium by region). Onshore marine is not included. Location correlation: Matrix 12 (all 1 → simple sum across the four locations).

### 8.5 Hail

Base factor within KSA 0.05% of sum insured (0.01% × 5 multiplier for motor comprehensive); outside KSA 30% of earned premium.

| KSA region | Western | Central | Eastern | Northern | Southern |
|---|---|---|---|---|---|
| Risk weight | 2 | 1 | 1 | 3 | 3 |
| Effective % of sum insured | 0.10% | 0.05% | 0.05% | 0.15% | 0.15% |

LOB: motor only (sums insured under Motor Comprehensive within KSA; motor earned premium by region outside KSA). Net loss deducts salvage. Regional correlation: Matrix 13.

### 8.6 Sandstorm (KSA only)

| KSA region | Western | Central | Eastern | Northern | Southern |
|---|---|---|---|---|---|
| Risk weight | 1 | 3 | 3 | 5 | 5 |

- Property (power plants): `Loss = 0.03% × RegionWeight × SumInsured_powerplants × (1 + 10% BI uplift)`.
- Health: `Insureds needing emergency treatment = Insureds × 0.5% × RegionWeight` (0.5% = 10% × 5%); `Loss = that number × SAR 500` (0.5 in SR '000).
- Regional loss = property + health; aggregate regions with Matrix 14. No outside-KSA component.

### 8.7 Windstorm (outside KSA only)

`Loss_region = 175% × earned premium` for property, energy and engineering by region; diversification by the outside-KSA formula in 8.2. No KSA component.

### 8.8 Man-made CAT — Property (fire)

Scenario: fire at the single largest property risk covered under a reinsurance treaty (excluding facultative risks); health and life covers of people in the same property are also hit.

```
Property loss  = 100% of sum insured (or lower applicable sub-limit)
               + business interruption loss (company input: claim for 50% of the maximum number of days in the policy)
Health loss    = insured lives × 25% (injuries needing hospital treatment) × average cost per claim (input)
P&S loss       = insured lives × 5% (deaths) × average cost per claim (input)
Gross          = Property + BI + Health + P&S
Net            = Gross − Σ recoveries (property, health, P&S) + reinstatement premiums + sliding scale commission (property, health)
```

### 8.9 Man-made CAT — Energy

Scenario: explosion and fire at oil refineries in the company's largest concentration of gross energy exposures (e.g. Ras Tanura), treaty business excluding facultative; onshore and offshore both considered when identifying the concentration.

```
Gross = Total sum insured (or lower sub-limit)
      + business interruption claim (input: 50% of the maximum number of days in the policy)
      + cost of environmental clean-up (input: 50% of the benefit limit unless excluded)
Net   = Gross − recovery + reinstatement premium + sliding scale commission
```

### 8.10 Man-made CAT — Motor liability & event cancellation

Scenario: collision between an insured car and a coach carrying European football league players; 5 passengers permanently disabled; match cancelled. Applicability flag (Yes/No) is a company input — the loss is zero when "No".

```
Liability for disability = 5 injured × SAR 2,000,000 average claim = 10,000 (SR '000)
Gross = Liability for disability + liability claim for event cancellation (input, if written)
Net   = Gross − recovery + reinstatement premium + sliding scale commission
```

### 8.11 Man-made CAT — Marine

Scenario: insured oil tanker collides with a cruise ship; all cruise passengers are US citizens (US litigation); hull, liability, wreck removal and pollution.

```
Death claims   = 50 deaths × SAR 300,000 = 15,000 (SR '000)
Injury claims  = 500 injured × SAR 500,000 = 250,000 (SR '000)
Gross = max marine hull exposure to a single tanker (input)
      + max marine cargo exposure to a tanker (input)
      + death claims + injury claims
      + wreck removal (input: 50% of benefit limit unless excluded)
      + oil pollution clean-up (input: 50% of benefit limit unless excluded)
      + US litigation cost (input: 10% of total injury claims cost, subject to policy cap)
Gross is set to 0 if hull + cargo exposure = 0.
Net   = Gross − recovery + reinstatement premium + sliding scale commission
```

### 8.12 Man-made CAT — Aviation

Scenario: two fully occupied passenger aircraft of two domestic airlines (Saudi Airlines and Fly Nas) collide over Riyadh airport; airport closed for days; the pilot of the aircraft insured by the company is held responsible.

```
Compensation to heirs = (350 + 150 deaths) × SAR 300,000 = 150,000 (SR '000)
Gross = hull loss airline 1 (input) + hull loss airline 2 (input) + compensation to heirs
      + business interruption at Riyadh airport (input: 5% of the BI benefit limit unless excluded)
Gross is set to 0 if both hull losses are 0.
Net   = Gross − recovery + reinstatement premium + sliding scale commission
```

### 8.13 Man-made CAT — Credit & suretyship

```
Default loss (gross) = 10% × exposure under the two largest trade credit & surety policies
Default loss (net)   = gross − recovery + reinstatement premium + sliding scale commission
Recession loss       = 100% × premium expected to be earned on trade credit & surety policies in the next 12 months
Gross = sqrt( DefaultGross² + Recession² )
Net   = sqrt( DefaultNet² + Recession² )
Undiversified (net) = DefaultNet + Recession
```

### 8.14 CAT aggregation

```
ManMadeCAT = sqrt( Energy² + Property² + Motor² + Marine² + Aviation² + Credit² )      (M8 = identity)
NatCAT     = sqrt( Flood² + Earthquake² + Hail² + Sandstorm² + Windstorm² )            (M9 = identity)
CAT        = sqrt( ManMadeCAT² + Pandemic² + NatCAT² )                                 (M10 = identity)
```
