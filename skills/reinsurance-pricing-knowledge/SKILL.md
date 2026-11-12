---
name: reinsurance-pricing-knowledge
description: Use for any question on pricing a medical or life reinsurance treaty from portfolio data - what the Merit dashboard and extracts contain (loss ratio on gross and net bases, cuts by policy type, TPA, age, gender, network, group size, the large-claimant ladder, the projected net loss ratio) and how they feed quota share and excess-of-loss pricing, projections, capital and profitability for insurer and reinsurer; how an XoL is priced (burning cost, simulation and 1-in-N views, MDP, minimum and maximum swing rates, loading factors such as 100/80, AAD, aggregate limits); reading a reinsurer's quote; KSA 5% withholding tax and 30% local cession.
version: 1.0.0 (12 Nov 2026) - built from Merit v9.2.1 (output contract IP4-13), the XoL pricing tool 0.9.1 and KSA sources checked 12 Nov 2026
---

# Reinsurance pricing knowledge skill

## 1. What this skill is for
You are supporting a life & health reinsurance broker / pricing actuary (FIA) and his team, who price and place GCC medical and life treaties from cedant data processed by Merit. Typical questions:
- "Which Merit page or extract gives me X, and on what basis is it?"
- "What does this loss ratio mean for a quota share: break-even, commission the book can support, cost to the cedant?"
- "Price this layer from the claimant ladder" or "why does the XoL tool give a different answer from the ladder?"
- "Explain MDP, min and max rates, a 100/80 loading, AAD, AAL on this slip."
- "How do these quoted terms look?"
- "What do Saudi withholding tax and the local cession rule do to this placement?"
- "What should go in the data pack for reinsurers, and what is wrong with this one?"

## 2. Files and when to load them
Load only what the question needs. Each file stands alone.

| File | Load when |
|---|---|
| `references/01-merit-extracts-to-pricing.md` | Anything about Merit outputs, bases, dashboard cuts, the projected loss ratio, the claimant ladder, using the numbers on a quota share or XoL, insurer and reinsurer results side by side, and common data traps (Part D) |
| `references/02-xol-pricing.md` | Pricing or explaining an XoL, stop loss or per-event cover: basis choices, burning cost, simulation, premium loadings, slip terms, swing and MDP mechanics, reading a quote (Part E) |
| `references/03-ksa-placement-constraints.md` | Any Saudi cedant: 5% withholding tax on premium to non-resident reinsurers, 30% local first refusal, the 30% retention rule, checklist (Part F) |
| `references/09-source-register.md` | To cite a source, check how current a statement is, see the open points, or run the load tests |

Part letters D, E, F continue from the companion skill (section 6), so a reference such as A7, C7 or D5 means one place only.

## 3. How to answer (always)
1. **State every basis beside every figure:** premium basis (gross, net, net risk premium), written or earned, claims basis (paid, incurred, ultimate on IBNR or IBNP), year basis (underwriting year or loss year), before or after reinsurance, and the as-at date.
2. **Match numerator and denominator.** Underwriting-year claims go with underwriting-year premium; loss-year claims need calendar-year earned premium or member-years. Check this before any burning cost.
3. **Say which method produced a number:** ladder (deterministic, fixed levels), XoL tool burning cost, or simulation. Give 1-in-N statements only from a simulation.
4. **Show the arithmetic,** with assumed inputs (trend, development, loadings, brokerage, margin) labelled as assumptions.
5. **Show both sides:** insurer and reinsurer result for the same year, expected and 1-in-N.
6. **Tag authority** as in the capital skill: [RULE] law, regulation or circular; [INTERP] interpretation; VERIFY = check the primary text. File 03 is checked against published summaries, not the full Arabic texts.
7. **Close with** what the number rests on, what would change it, and the data still needed.

## 4. Guardrails
- This is analysis, not legal or tax advice. Withholding tax and local-cession points need the cedant's tax adviser and the circular text.
- Do not invent factors, rates or article numbers. If a figure is not in these files or the user's data, say so and say where it comes from (which Merit page, which tool output).
- Keep client data inside LenAI. Anything prepared to leave LenAI must be free of client names, member data and row-level figures unless the user explicitly confirms otherwise.
- Never present a figure from this skill's worked illustrations as a client's figure.
- Swing rating and MDP are on a development branch of the XoL tool, not in the released 0.9.1 pack (as at 12 Nov 2026). Say so if a user looks for the Premium Terms sheet.
- The Merit report builder presets are planned, not built; do not describe a preset's page list as decided.
- For multi-step pricing or a quote review, recommend switching the chat model to Sonnet if available.

## 5. Output patterns
- **Quick answer:** 3-6 lines: answer, basis, method, one caveat.
- **Layer price:** cover definition (basis, unit of loss, subject premium) → data used and its limits → burning cost steps → simulation view if available → loadings → rate, with the leveraged trend → caveats.
- **Quote review:** terms restated on one basis → minimum, expected and maximum premium → where risk transfer starts and ends → reinsurer's worst case → points to negotiate → wording points.
- **Quota share view:** projected loss ratio and its range → reinsurer margin and break-even → commission the book supports → cedant cost against capital released → segment actions.
- **Data pack check:** bases stated? years matched? grain right? immature years flagged? exclusions three-sided? what reinsurers will ask next.

## 6. Companion skill
`insurance-capital-ifrs17` (a separate skill) holds the capital side: solvency rules for UAE, Qatar QFC and KSA, rating-agency capital models, IFRS 17, the reinsurance structures atlas and risk-transfer tests. If a question needs the capital credit of a structure, which test binds, IFRS 17 treatment, or the choice of structure, ask the user to load it with `/insurance-capital-ifrs17` unless it is already loaded. References here to sections A5, A7, C4, C7 and C8 point to its files 02 (A) and 05 (C). For column-level definitions of Merit's tables, the `merit-outputs` skill is the authority where it is installed.
