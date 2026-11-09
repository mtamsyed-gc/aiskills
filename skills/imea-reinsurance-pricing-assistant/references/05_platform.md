# 05 LenAI / LenWork: what it can do for him (probe CP1.1, 6 Nov 2026)

- Models: Claude Haiku 4.5 (default) and Claude Sonnet 5. Use Sonnet for judgement work (triage, mapping proposals).
- No cross-chat memory; this skill is loaded per chat with `/imea-reinsurance-pricing-assistant`. A small Preference
  Store (`memory_save_learning`) persists user-saved learnings.
- Integrations: Microsoft 365 (Calendar, Email, Teams, SharePoint/OneDrive links, OneNote read-only). `webfetch`
  cannot read GitHub. His repos (ete-dashboard, pricing-workbench, merit-ai, xolpricing) are reached only through files
  he uploads or through a connector.
- Python sandbox: no network, ~1-2 GB RAM, 1 CPU; pandas / numpy / scipy / openpyxl / xlsxwriter / matplotlib; no
  pyarrow, polars, xlrd, pyxlsb. Heavy work runs natively on his laptop (`py <script>` via the PowerShell tool, or a
  connector tool).
- Connectors (LenWork > Customize > Connectors): local stdio `py <script>.py` servers work; launched once per chat;
  calls of 300 s and returns of 256 KB are fine (UI shows ~16 KB inline, the rest via retrieve_output); every call
  carries extra `action_summary` / `reasoning` arguments; the process is elevated and nothing prompts before a write,
  so each tool enforces its own folder allow-list and makes no network calls.
- Data boundary: real cedant data stays inside LenAI. Outbound messages (email, digest to Claude) are data-free.
- Working loop with Claude (outside GC): Claude builds and tests on synthetic data in the repo; files reach the GC
  laptop by email (personal -> work); results return as data-free plain-text digests.
