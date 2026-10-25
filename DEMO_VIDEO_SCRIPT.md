# Final demo script

## 00:00–00:25 — Problem

“Execution reviewers need evidence for why one market observation was accepted and another rejected. VELQIRIS turns that decision into an inspectable, reproducible chain.”

## 00:25–01:10 — Zetaris

“The official Zetaris local platform passes all nine checks. VELQIRIS logs in with a short-lived session and executes Lightning SQL through the UI, API, driver and Spark. This four-row scenario is deliberately synthetic and declared directly in SQL; it proves live platform execution without pretending to use production exchange feeds.”

Show the live receipt: one connectivity row, four scenario rows, fresh request IDs, and client-side timing.

## 01:10–01:55 — VELQIRIS decision

“VELQIRIS computes a robust MAD consensus. Three venues remain in the verified set. The anomalous venue is rejected because its deviation exceeds the ceiling. The post-filter consensus VWAP is 67,450.6642 and the verified spread is 0.09 basis points.”

## 01:55–02:40 — Meterless H-MEM

“The observation and the derived decision are stored in the official Meterless H-MEM reference engine. The hybrid ranker retrieves both memories with explicit scores, and the local append-only ledger records two creates and two reads. The official conformance suite passes 13 out of 13.”

## 02:40–03:15 — Evidence and boundaries

“The repository contains redaction-safe receipts, 24 passing Python tests, the 13-of-13 Meterless scorecard, and full pre-existing-code disclosure. SHA-256 values are integrity digests, not digital signatures. No production feed, provider-cost, external-model, or single-digit-latency claim is made.”

## 03:15–03:30 — Close

“VELQIRIS makes a market-consensus decision explainable from query to memory trace to audit evidence.”
