# Demo recording gate and script

Do not record the final competition demo until live Zetaris, real Meterless engine usage, and the selected current Nemotron model have reproducible redacted receipts.

## Required evidence before recording

- successful live Zetaris query against an identified non-secret source;
- measured client-side request duration from the recorded run;
- real Meterless engine present in the workflow, with an execution trace;
- exact Nemotron model ID and successful non-simulated response;
- no credentials, tokens or private endpoints visible;
- the event-specific repository and its release artifacts;
- truthful disclosure of pre-existing code.

## 2–3 minute script template

### 00:00–00:25 — Problem

"Execution systems combine fragmented market observations, but operators need evidence for why one source was accepted and another rejected. VELQIRIS demonstrates a reproducible investigation path for that decision."

### 00:25–01:05 — Architecture

Show the repository and name each component precisely:

- Zetaris: the recorded live query and returned rows;
- Meterless: the actual engine used and the trace it produces;
- the mathematical layer: MAD outlier isolation and consensus;
- Meterless H-MEM: provenance capture, hybrid retrieval trace and trust-ledger receipt.

Avoid adjectives such as "single-digit", "real-time", "cryptographically signed", or "under USD 0.05" unless the same recording displays valid supporting evidence.

### 01:05–02:10 — Live workflow

Run the live command. Show:

1. execution mode `LIVE`;
2. data-source mode `LIVE_ZETARIS`;
3. redacted request ID and measured elapsed time;
4. included and rejected records;
5. model-response mode `LIVE_MODEL_API`;
6. the Meterless trace.

If any component falls back to simulation, stop and do not present the run as the final demo.

### 02:10–02:40 — Evidence and limitation

"The output is stored with a SHA-256 integrity digest. This detects payload changes; it is not a digital signature. The demo shows one validated path, and the repository documents its limitations and pre-existing components."

### 02:40–03:00 — Close

Summarize the user value without making unmeasured performance, security, or cost claims.
