# Truthful slide-deck outline

This outline is safe only after replacing each `PENDING` item with verified evidence.

## Slide 1 — Problem and users

- Problem: evidence gaps in multi-source execution decisions.
- Users: routing engineers, market-risk analysts, and audit teams.
- Avoid unsupported regulatory or catastrophic-loss claims.

## Slide 2 — Prototype solution

- Query records through a data adapter.
- Compute a MAD-based consensus.
- Generate an evidence-grounded explanation.
- Attach a SHA-256 integrity digest.

## Slide 3 — Workflow

1. Retrieve data.
2. Validate and filter.
3. Explain from supplied evidence.
4. Persist an integrity-checkable record.

Clearly label fixture mode and live mode.

## Slide 4 — Technical stack

- Python standard library.
- Zetaris REST adapter — live receipt `PENDING`.
- Meterless engine — integration `PENDING`.
- External model adapter — optional, no live provider output claimed.
- SHA-256 integrity digest — verified locally.

## Slide 5 — Sponsor technology

Show only actual, recorded integration points. The project-local governor is not Meterless and must not be presented as such.

## Slide 6 — What is new during the build window

- pre-existing base prototype: disclose explicitly;
- 25 October fail-closed hardening: include only after it is adopted with commit provenance;
- real sponsor integration: `PENDING`.

## Slide 7 — Evidence

- 21/21 local tests;
- Meterless H-MEM canonical records, hierarchical layers, hybrid retrieval trace and hash-chained trust ledger;
- redacted live Zetaris receipt `PENDING`;
- Meterless trace `PENDING`;
- live Nemotron receipt `PENDING`;
- final demo and repository URLs `PENDING`.

## Slide 8 — Limitations and next work

- offline fixtures are not live-market evidence;
- provider cost is not verified;
- no digital signature exists;
- latency is not yet benchmarked;
- broader input validation and live failure testing remain.
