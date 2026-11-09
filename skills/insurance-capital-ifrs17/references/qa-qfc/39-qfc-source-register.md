# Qatar (QFC) layer: source register and open verification points

QFC layer version 1.0, compiled 9 Nov 2026. It covers **QFCRA-authorised insurers only**. The onshore QCB regime is not loaded.

## Primary sources used
| # | Source | Date / version | Used for |
|---|---|---|---|
| Q1 | QFCRA Insurance Business Rules 2006 (PINS), Version 20 (file QFCRA_4538_VER20) | Effective 1 Oct 2025; includes QFCRA Rules 2024-4 and 2025-1 | Ch 1-6, 8-12; Schedule 3 (all RBC factors); glossary |
| Q2 | QFCRA insurance prudential return workbook, structural and formula extraction (XBRL taxonomy `QFCRA_INS` 2.0.0, 2025 namespace; Q3 2026 specimen with no data) | Q3 2026 | INS600/INS610.x formulas, INS620, scope flags, disclosure-form layout, template vs rule differences (file 31 §6) |
| Q3 | IFRS 17 Insurance Contracts, including the 2020 amendments | Effective 1 Jan 2023 | File 33 |
| Q4 | Public reporting on QCB Governor Decision 1/2016 (Gulf Times, Peninsula, MEIR, Al Tamimi practice guide) | 2016-2026 | Perimeter note only (file 30 §1); not a rule source |

## Open points to VERIFY before relying on them in client work
1. **Return instructions.** Get the QFCRA completion guidance for the INS return. It is the likely source of:
   - the 2 × largest-retention concentration fallback;
   - the derivative add-on treatment;
   - the definitions of the premium-liability and outstanding-claims inputs under IFRS 17;
   - the treatment of OCI reserves.
2. **FSR Schedule 3, Part 3, para 10.3.** Confirm the names of general insurance categories 3-18 behind PINS categories 2-4.
3. **Long-term provisions.** Is the 0.5-3% charge applied gross or net of reinsurance, and does it include CSM?
4. **Eligible capital.** How are reserves other than retained earnings treated: FVOCI, insurance finance, hedging, revaluation?
5. **Inadmissible assets.** Are right-of-use assets "tangible fixed assets"? Are IACF assets deducted as DAC?
6. **Reinsurance governance.** Do any QFCRA rules or notices outside PINS impose a rating floor, cession limits or finite-risk restrictions? Check CTRL, GENE, COND and the Islamic finance rules.
7. **IAIS MMoU signatory list** on the date of use, for the supervised / unsupervised reinsurer factor.
8. **Firm-specific SRR or MCR conditions.** Any insurer-specific SRR set under 3.3.2A(3), or an MCR imposed as a licence condition.
9. **Which returns are in force** (annual, biannual, quarterly) per the current notice under 1.4.1.
10. **Onshore Qatar.** Load QCB Decision 1/2016 and its solvency annexes and returns before answering for any QCB-licensed insurer.

## Maintenance rule
When a source is updated:
- change the affected rows in files 30-33;
- bump the layer version;
- add the new source here with its date;
- move resolved VERIFY items into the main text with their citation.

## Load-test questions (expected answer in brackets)
- **Q1.** A QFC LLC medical insurer has RBC of QAR 20m and eligible capital of QAR 38m. Is it compliant, and does a 30% QS help?
  - [Yes: MCR = 36m (floor) and SRR = 30m, so the floor binds. A QS cuts RBC but creates no headroom, because the 36m floor still binds.]
- **Q2.** What is the premium-risk factor for direct medical business, and can it be lowered?
  - [PINS cat 1: 16% of net premium liability. Can be lowered on application with morbidity data to no less than 12% (A3.7.3).]
- **Q3.** What does ceding to an A-rated reinsurer domiciled in a non-MMoU jurisdiction cost?
  - [4.8% of the reinsurance asset vs 4% if supervised by a subrule (2) regulator.]
- **Q4.** INS610 L20 is positive. Is the insurer necessarily compliant?
  - [No. L20 is eligible − MCR. The SRR (eligible ≥ 150% × RBC) must be checked separately.]
- **Q5.** A Qatari insurer licensed by QCB asks about its SRR.
  - [The QFC layer does not apply; no QCB layer is loaded.]
