# Part F - KSA placement constraints: withholding tax and local cession
As at 12 Nov 2026. Checked against ZATCA's WHT circular and published summaries of the Insurance Authority (IA) circulars, not against the full Arabic texts: VERIFY the primary document and take tax advice before a client relies on it. Analysis, not legal or tax advice. The one-line versions of these rules sit in `ksa-rbc-capital` (file 28, K3) and `insurance-capital-ifrs17` (file 05 section C7).

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
  - Counterparty charge follows the local reinsurer's rating; note the KSA-RBC cliff between BBB (5%) and BB or unrated (50%) (`ksa-rbc-capital`, file 22). Few local reinsurers means concentration: check the IA's current list of licensed reinsurers.
  - Model the panel as shares by residency and rating (TSM does this per layer): results, WHT and credit charge all move with the split.
  - A structure the local market will not write (unlimited stop loss, novel structured terms) still has to be offered; allow time for a documented decline.

### F3 Checklist for a KSA treaty
1. Art 40 retention met (cession no more than 70% of total premium).
2. 30% offered locally first; evidence kept; broker's process documented.
3. Each reinsurer: resident or not, treaty relief or not, WHT borne by whom, stated in the wording.
4. Rating at or above the regime minimum and the counterparty charge (`ksa-rbc-capital`, file 28 K3 and file 22).
5. Finite-risk test (Art 19) on any corridor, cap, sliding scale or swing terms; reportable features (Art 18).
6. Reinsurer-side results shown net of brokerage and WHT; cedant-side cost shown gross of any gross-up.
