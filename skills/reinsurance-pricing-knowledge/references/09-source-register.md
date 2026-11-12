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
