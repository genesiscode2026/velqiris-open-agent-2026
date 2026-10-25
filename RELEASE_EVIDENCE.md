# Release evidence

Release date: 25 October 2026

## Verified results

- Zetaris official verifier: **9/9 PASS**.
- Zetaris live connectivity query: `SELECT 7 AS seven`, one returned row.
- Zetaris live scenario: four declared synthetic rows executed by the live engine, four returned rows.
- VELQIRIS result: consensus VWAP **67,450.6642**, post-filter spread **0.09 bps**, one MAD outlier rejected.
- Meterless H-MEM official reference: two memories stored and retrieved; four append-only ledger events persisted.
- Meterless official conformance suite: **13/13 PASS**.
- Python project suite: **24/24 PASS**.
- Credentials and session tokens: excluded from all repository evidence.
- Final PPTX SHA-256: `410ef7eec99211cc415a5aa1fb30d142f14c5b9d8b346970fcd0410322252020`.
- Final MP4 SHA-256: `aeae20c818e9bd0def868466b1000bb8648734f3a23775b569daeb1cec83fb89`.

## Primary evidence files

- `evidence/zetaris-platform-verification.json`
- `evidence/zetaris-live-receipt.json`
- `evidence/meterless-hmem-live-receipt.json`
- `evidence/meterless-hmem-conformance.json`
- `evidence/meterless-hmem-runtime/state.json`
- `evidence/meterless-hmem-runtime/ledger.jsonl`

## Claim boundaries

The live scenario proves Zetaris SQL execution and VELQIRIS processing. Its four market rows are deterministic synthetic inputs expressed directly in SQL; they are not production exchange feeds. Timings are client-side observations from one local run, not benchmarks. No external model was called. SHA-256 values are integrity digests, not digital signatures.
