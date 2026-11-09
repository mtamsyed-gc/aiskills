# Template: building a new jurisdiction overlay (KSA, Qatar, Oman, Bahrain, Kuwait, Egypt, Jordan ...)

Create the folder `references/<country-code>/` with the five files below, numbered like the UAE layer. Keep each file under ~8k tokens, so that one overlay plus the core files stays well within what LenAI can load at once. Use the same tags: [RULE], [TEMPLATE], [INTERP], VERIFY.

## x0-<cc>-legal-framework.md
- **Regulator(s)** and perimeter, including free zones excluded (e.g. QFC in Qatar, the KSA special zones if any).
- **Primary law(s), with the articles on:**
  - licensing, legal form and minimum capital;
  - technical provisions and solvency delegation;
  - reinsurance rules (local cession requirements, rating floors);
  - portfolio transfers;
  - intervention, resolution and creditor ranking;
  - dividends.
- **Table of instruments in force,** with effective dates.
- **Governance hooks:** actuary, ORSA or FCR, retention plan, board reporting.
- **Takaful or cooperative model specifics:** for KSA, the cooperative insurance surplus split and the cooperative law.

## x1-<cc>-solvency-requirements.md
- **Requirement layers** and which capital tier covers each.
- **Own-funds definition,** tiers and limits; admissibility.
- **Liability basis** for solvency (statutory or IFRS 17-based).
- **Formula, module by module:** factors, floors on net/gross, correlations, operational risk, catastrophe.
- **Breach ladder and timelines;** reporting and disclosure.
- **A worked example** in the same format as UAE file 11 §8.

## x2-<cc>-reinsurance-rules.md
- **Cession rules:**
  - local retention or cession quotas (KSA, for example, has local-cession requirements);
  - rating floors;
  - prohibited or finite structures;
  - approvals.
- **Capital credit by structure:** same table as UAE file 12 §2.
- **Screening checklist** adapted to local rules.

## x3-<cc>-ifrs17-bridge.md
- **Is the regulatory basis IFRS 17-based?** If yes, which adjustments (e.g. CSM treated as own funds or as a liability, RA recalibration)?
- **Line-by-line bridge table** and a practical equity-to-own-funds bridge.
- **Premium measures used** by the formula vs what IFRS 17 shows.
- **Accounting vs capital effects of common actions:** same table as UAE file 13 §5.

## x9-<cc>-source-register.md
- Sources with dates, an open VERIFY list, and the maintenance rule.

## When the overlay is added
1. Add the files to the routing table in SKILL.md §2.
2. Add any country-specific guardrail to SKILL.md §4.
3. Keep the core files jurisdiction-neutral. Move anything country-specific out of them.
4. Bump the skill version and note the overlay in the description line.
