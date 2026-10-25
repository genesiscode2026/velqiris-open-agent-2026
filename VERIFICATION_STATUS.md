# Verification status — 25 October 2026

| Claim | Status | Evidence |
|---|---|---|
| Zetaris platform | Verified live | Official `verify.sh`: 9/9 PASS |
| Zetaris query route | Verified live | UI -> API -> driver -> Spark |
| Zetaris connectivity query | Verified live | `SELECT 7 AS seven`, one row |
| Zetaris market scenario | Verified live | Four declared synthetic SQL rows returned by live Zetaris |
| Production exchange feeds | Not claimed | Scenario is explicitly synthetic |
| Meterless H-MEM runtime | Verified live/local | Official reference stored/retrieved evidence and persisted four ledger events |
| Meterless conformance | Verified | Official suite: 13/13 PASS |
| Python project tests | Verified | 24/24 PASS |
| Single-digit latency | Not claimed | Observed local durations are recorded, not benchmarked |
| Cost below USD 0.05 | Not claimed | Project-local estimate is not provider billing telemetry |
| NVIDIA Nemotron output | Not claimed | No external model was invoked in the live receipt |
| SHA-256 integrity digest | Verified | Query-response and ledger digests are recorded |
| Digital signature | Not implemented | No signing key or signer identity exists |
| Public repository | Verified | `genesiscode2026/velqiris-open-agent-2026` |
| Demo video | Verified artifact | MP4, 1–4 minute requirement |
| Pitch deck | Verified artifact | PPTX included in repository |
| HackOS submission | Pending final platform action | Form must be checked, then submitted |

## Release boundary

The sponsor integration is verified. The demo must say that the SQL scenario uses declared synthetic market rows and that no production exchange feed or external model is claimed.
