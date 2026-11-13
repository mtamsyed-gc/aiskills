# KSA RBC: Correlation matrices and regions

All 17 correlation matrices, the KSA regions and earthquake locations, the 7 premium/reserve regions and the 18 natural-catastrophe regions outside KSA.

Source: Insurance Authority (IA) "Solvency and Capital Template 2026", version SCA.04 (issued 2026-02-25), workbook `20260226_Solvency_and_Capital_Template_2026_vSCA.04.xlsx`, run "Risk Based Capital 5th Dry Run (2025YE)", as restated in the owner's rules specification `KSA_RBC_Rules_vSCA04.md` (13 Nov 2026). Every value is **[DRY RUN]**: it can change before the final 2027 regulation. Section numbers (1-17, Appendices A-E) are the specification's; SKILL.md section 2 says which file holds each one. Cell references such as `[RBC!S65]` trace to the workbook.

---

## Appendix A — Correlation matrices

**Matrix 1 — Market**

| | IR | Equity | Property | Spread | Concentration | Currency |
|---|---|---|---|---|---|---|
| IR | 1 | 0.5 | 0.5 | 0.5 | 0 | 0.25 |
| Equity | 0.5 | 1 | 0.75 | 0.75 | 0 | 0.25 |
| Property | 0.5 | 0.75 | 1 | 0.5 | 0 | 0.25 |
| Spread | 0.5 | 0.75 | 0.5 | 1 | 0 | 0.25 |
| Concentration | 0 | 0 | 0 | 0 | 1 | 0 |
| Currency | 0.25 | 0.25 | 0.25 | 0.25 | 0 | 1 |

**Matrix 2 — Life UW**

| | Mortality | Lapse | Expenses | Morbidity |
|---|---|---|---|---|
| Mortality | 1 | 0 | 0.25 | 0.25 |
| Lapse | 0 | 1 | 0.5 | 0 |
| Expenses | 0.25 | 0.5 | 1 | 0.5 |
| Morbidity | 0.25 | 0 | 0.5 | 1 |

**Matrix 3 — Non-Life UW**

| | Premium | Reserve | CAT |
|---|---|---|---|
| Premium | 1 | 0.75 | 0.25 |
| Reserve | 0.75 | 1 | 0.25 |
| CAT | 0.25 | 0.25 | 1 |

**Matrix 4 — Counterparty default:** Type 1 – Type 2 = 0.75.

**Matrix 5 — Basic RBC**

| | Market | CD | Life UW | Non-Life UW |
|---|---|---|---|---|
| Market | 1 | 0.25 | 0.25 | 0.25 |
| CD | 0.25 | 1 | 0.25 | 0.5 |
| Life UW | 0.25 | 0.25 | 1 | 0 |
| Non-Life UW | 0.25 | 0.5 | 0 | 1 |

**Matrix 6 — Equity**

| | TASI | Nomu | Unlisted/other KSA | Listed OECD | Other outside KSA |
|---|---|---|---|---|---|
| TASI | 1 | 0.75 | 0.5 | 0.5 | 0.25 |
| Nomu | 0.75 | 1 | 0.5 | 0.5 | 0.25 |
| Unlisted/other KSA | 0.5 | 0.5 | 1 | 0.25 | 0.25 |
| Listed OECD | 0.5 | 0.5 | 0.25 | 1 | 0.5 |
| Other outside KSA | 0.25 | 0.25 | 0.25 | 0.5 | 1 |

**Matrix 7 — Property (KSA):** Residential–Commercial 0.75; Residential–Agricultural 0.25; Commercial–Agricultural 0.25.

**Matrix 8 — Man-made CAT (6×6), Matrix 9 — Natural CAT (5×5), Matrix 10 — CAT (3×3):** identity (all off-diagonals 0).

**Matrix 11 — Pluvial flood regions, and Matrix 13 — Hail regions (identical)**

| | W | C | E | N | S |
|---|---|---|---|---|---|
| W | 1 | 0.5 | 0 | 0.5 | 0.75 |
| C | 0.5 | 1 | 0.5 | 0.25 | 0 |
| E | 0 | 0.5 | 1 | 0.25 | 0 |
| N | 0.5 | 0.25 | 0.25 | 1 | 0 |
| S | 0.75 | 0 | 0 | 0 | 1 |

**Matrix 12 — Earthquake locations (Haql, Qiyal, Neom, Tabuk):** all entries 1.

**Matrix 14 — Sandstorm regions**

| | W | C | E | N | S |
|---|---|---|---|---|---|
| W | 1 | 0.25 | 0 | 0.5 | 0.25 |
| C | 0.25 | 1 | 0.75 | 0.5 | 0.25 |
| E | 0 | 0.75 | 1 | 0.25 | 0 |
| N | 0.5 | 0.5 | 0.25 | 1 | 0 |
| S | 0.25 | 0.25 | 0 | 0 | 1 |

**Matrix 15 — Premium risk by LOB.** Default 0.25 for every pair, except:

| Pair | Correlation |
|---|---|
| LOB2–LOB3 (Motor Compulsory – Motor Compulsory + Others) | 0.75 |
| LOB1–LOB9 (Accident & Liability – Health) | 0.5 |
| LOB2–LOB9, LOB3–LOB9 (Motor – Health) | 0.5 |
| LOB4–LOB8 (Property – Engineering) | 0.5 |
| LOB5–LOB7 (Marine – Energy) | 0.5 |
| LOB11–LOB12 (Group Life – Group Credit Life) | 0.75 |
| LOB11–LOB13, LOB12–LOB13 | 0.5 |

**Matrix 16 — Reserve risk by LOB.** Identical to Matrix 15 **except LOB1–LOB9 = 0.25** (not 0.5).

**Matrix 17 — Type 1 counterparties (300×300):** 1 on the diagonal, 0.25 everywhere else.

---

## Appendix B — Regions

**KSA regions (flood, hail, sandstorm):** Western, Central, Eastern, Northern, Southern. **Earthquake locations:** Haql, Qiyal, Neom, Tabuk.

**Premium/reserve risk regions (7):** KSA; Asia excluding KSA; Europe; Africa; South America; North America; Australia.

**Natural CAT regions outside KSA (18):**

1. Northern Europe — Denmark (except Greenland), Estonia, Finland, Guernsey, Iceland, Ireland, Isle of Man, Jersey, Latvia, Lithuania, Norway, Sweden, United Kingdom (except overseas territories).
2. Western Europe — Austria, Belgium, France (except overseas territories), Germany, Liechtenstein, Luxembourg, Monaco, Netherlands (except Caribbean territories), Switzerland.
3. Eastern Europe — Belarus, Bulgaria, Czech Republic, Hungary, Moldova, Poland, Romania, Russia, Slovakia, Ukraine.
4. Southern Europe — Albania, Andorra, Bosnia and Herzegovina, Croatia, Cyprus, North Macedonia, Gibraltar, Greece, Italy, Malta, Montenegro, Portugal, San Marino, Serbia, Slovenia, Spain, Vatican City.
5. Central and Western Asia (excluding KSA) — Armenia, Azerbaijan, Bahrain, Georgia, Iraq, Israel, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Lebanon, Oman, Qatar, Syria, Tajikistan, Turkey, Turkmenistan, United Arab Emirates, Uzbekistan, Yemen.
6. Eastern Asia — China, Japan, Mongolia, North Korea, South Korea, Taiwan.
7. South and South-Eastern Asia — Afghanistan, Bangladesh, Bhutan, Brunei, Myanmar, Cambodia, India, Indonesia, Iran, Laos, Malaysia, Maldives, Nepal, Pakistan, Philippines, Singapore, Sri Lanka, Thailand, East Timor, Vietnam.
8. Oceania — American Samoa, Australia, Cook Islands, Fiji, French Polynesia, Guam, Kiribati, Marshall Islands, Micronesia, Nauru, New Caledonia, New Zealand, Niue, Northern Mariana Islands, Palau, Papua New Guinea, Pitcairn Islands, Samoa, Solomon Islands, Tonga, Tuvalu, Vanuatu, Wallis and Futuna.
9. Northern Africa — Algeria, Benin, Burkina Faso, Cameroon, Cape Verde, Central African Republic, Chad, Côte d'Ivoire, Egypt, Gambia, Ghana, Guinea, Guinea-Bissau, Liberia, Libya, Mali, Mauritania, Morocco, Niger, Nigeria, Saint Helena, Senegal, Sierra Leone, South Sudan, Sudan, Togo, Tunisia.
10. Southern Africa — Angola, Botswana, Burundi, Comoros, DR Congo, Djibouti, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Kenya, Lesotho, Madagascar, Malawi, Mauritius, Mayotte, Mozambique, Namibia, Congo, Réunion, Rwanda, São Tomé and Príncipe, Seychelles, Somalia, South Africa, Swaziland, Uganda, Tanzania, Zambia, Zimbabwe.
11. Northern America (excluding USA) — Bermuda, Canada, Greenland, Saint Pierre and Miquelon.
12. Caribbean and Central America — Anguilla, Antigua & Barbuda, Aruba, Bahamas, Barbados, Belize, Bonaire, British Virgin Islands, Cayman Islands, Costa Rica, Cuba, Curaçao, Dominica, Dominican Republic, El Salvador, Grenada, Guadeloupe, Guatemala, Haiti, Honduras, Jamaica, Martinique, Mexico, Montserrat, Nicaragua, Panama, Puerto Rico, Saint Barthélemy, Saba, Saint Kitts and Nevis, Saint Lucia, Saint Martin, Saint Vincent and the Grenadines, Sint Eustatius, Sint Maarten, Trinidad and Tobago, Turks and Caicos Islands, US Virgin Islands.
13. Eastern South America — Brazil, Falkland Islands, French Guiana, Guyana, Paraguay, Suriname, Uruguay.
14. Northern, Southern and Western South America — Argentina, Bolivia, Chile, Colombia, Ecuador, Peru, Venezuela.
15. North-east USA — Connecticut, Delaware, District of Columbia, Maine, Maryland, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont.
16. South-east USA — Alabama, Arkansas, Florida, Georgia, Kentucky, Louisiana, Mississippi, North Carolina, Puerto Rico, South Carolina, Tennessee, Virginia, West Virginia.
17. Mid-west USA — Illinois, Indiana, Iowa, Kansas, Michigan, Minnesota, Missouri, Nebraska, North Dakota, Ohio, Oklahoma, South Dakota, Wisconsin.
18. Western USA — Alaska, Arizona, California, Colorado, Hawaii, Idaho, Montana, Nevada, New Mexico, Oregon, Texas, Utah, Washington, Wyoming.

(Puerto Rico appears in both region 12 and region 16 in the template.)
