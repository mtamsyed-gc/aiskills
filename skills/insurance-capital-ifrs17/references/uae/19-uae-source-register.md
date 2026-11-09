# UAE layer: source register and open verification points

UAE layer version 1.0, compiled 6 Nov 2026.

## Primary sources used
| # | Source | Date / version | Used for |
|---|---|---|---|
| S1 | Federal Decree-Law No. 6 of 2025 (CB Law), English translation | Issued 8 Sep 2025; in force 16 Sep 2025 | Arts 2, 61, 69-70, 78-105, 120-128, 140-144, 168, 183-185 |
| S2 | CBUAE Rulebook, insurance section, full export | Retrieved 20 Oct 2026 | In-force status and effective dates of all instruments; text of Decision 23/2019, Decision 14/2018, Decision 22/2017, Decision 49/2019, C 5/2023, Circulars 24/25 of 2022, Takaful Regulation 2026 and Standards, C 4/2026 |
| S3 | IA Board Decision 25/2014, Financial Regulations for Insurance Companies (CBUAE_EN_1087) | 28 Dec 2014 | Sections 1-4 and 7, all Addendums |
| S4 | IA Financial Reporting eForms, User Instructions v1.7, and the v1.7 workbook formulas | IA era (VERIFY current version) | SM-1 to SM-6 factors, REINS-2 admissibility, takaful commission rule, eForm list |
| S5 | IFRS 17 Insurance Contracts, including the 2020 amendments | Effective 1 Jan 2023 | Core file 00; paras 65, 66A-66B, 86 etc. |
| S6 | Milliman, "UAE Insurance Industry Update: Preliminary 2023" (Apr 2024), summarising CBUAE notice 6163 of 15 Dec 2023 | Apr 2024 | IFRS 17 vs regulatory reporting basis; ORSA; recovery plans |
| S7 | Hadef & Partners, CB Law 2026 developments | 2026 | In-force date (16 Sep 2025) and the September 2026 conformity deadline; list of 2026 regulations |
| S8 | DFSA Prudential Insurance Business module (PIN) | Version held in the project | DIFC contrast only |
| S9 | EU Delegated Regulation 2015/35, Arts 208-215 | — | Risk-mitigation principles borrowed for the risk-transfer memo |

## Open points to VERIFY before relying on them in client work
1. **eForms version.** Is v1.7 still the filed version, or has the CBUAE issued a later template? Factors may have changed.
2. **IFRS 17 and the regulatory basis.** Has any CBUAE notice after Dec 2023 moved the regulatory returns or the solvency template to IFRS 17?
3. **New solvency regime.** CB Law Art 70 empowers the Board to set risk-based capital requirements. Watch for a replacement of Decision 25/2014 Section 2.
4. **Unearned reinsurance commission on the regulatory balance sheet.** This decides whether QS or UPR commissions create day-1 BOF.
5. **Reinsurance asset valuation basis** for ADC or aggregate covers (best estimate vs prudent).
6. **Solvency disclosure circular** allowing a one-quarter lag. Confirm the reference and current wording.
7. **ORSA:** current submission cycle and format.
8. **Decision 23/2019 article numbering and wording** against the live Rulebook (the export's layout places headings after text).
9. **Long-term life shock factors in SM-2(L):** not reproduced here; read them from the template the company files.
10. **Takaful IFRS 17 accounting policy:** entity-specific.

## Maintenance rule
When a source is updated:
- change the affected rows in files 10-13;
- bump the layer version;
- add the new source here with its date;
- move resolved VERIFY items into the main text with their citation.
