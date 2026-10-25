# Release evidence

Release date: 25 October 2026

## Reproduce

```bash
python3 tests/run_all_tests.py
python3 agent/cli.py --dry-run --output evidence/offline-evidence.json
```

## Verified results

- Tests: **21 executed, 0 failures, 0 errors**.
- Offline workflow: explicit `OFFLINE_SIMULATION`.
- Consensus fixture: VWAP **67,450.66**, post-filter spread **0.09 bps**, risk regime **CALM**.
- Included fixture venues: BINANCE, COINBASE, OKX.
- Rejected fixture venue: ANOMALY_DEX.
- Meterless receipt: engine name, implementation profile, official specification URL, stored/retrieved memory IDs, retrieval strategy, ledger-entry count and ledger-head SHA-256.
- Evidence record: payload-level SHA-256 integrity digest.

## Live release gate

The end-to-end path is not described as live until a current Zetaris environment produces a redacted successful query receipt. Required runtime values are documented in `.env.example`; secrets must never be committed.
