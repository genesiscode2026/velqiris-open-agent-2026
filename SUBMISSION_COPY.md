# HackOS submission copy

## Project name

VELQIRIS — The Agent That Can Explain Why

## One-line description

Evidence-first market consensus agent that links governed Zetaris data access to Meterless H-MEM context, explicit MAD outlier logic, and tamper-evident receipts.

## Project description

VELQIRIS helps institutional risk and execution reviewers understand not only what a multi-venue consensus is, but why it is defensible. The agent queries governed rows through a fail-closed Zetaris adapter, computes a robust post-filter consensus with Median Absolute Deviation, captures the observation and derived finding in Meterless H-MEM, retrieves provenance-bearing context with explicit ranking traces, and seals the evidence record with a SHA-256 payload digest and H-MEM trust-ledger head.

The current release verifies 21 local tests with zero failures. Meterless H-MEM is integrated as a local-first implementation profile covering canonical records with lineage, hierarchical memory, hybrid retrieval, trace metadata and an append-only hash-chained trust ledger. Dreaming, sleep and conflict-resolution services are outside this profile and are not claimed.

The repository also contains a generic Zetaris REST adapter with unique request IDs and fail-closed behavior. A live Zetaris execution must be evidenced with current credentials and a redacted receipt before the end-to-end path is described as live. The included deterministic fixture is available only with `--dry-run` and is always labelled `OFFLINE_SIMULATION`.

## Sponsor integration

### Zetaris

`agent/zetaris_client.py` sends Lightning SQL to the configured REST endpoint using a bearer key, organization ID and fresh `X-Request-ID`. Missing credentials never fall back to fixtures in live mode. The fixture path is explicit and separately labelled.

### Meterless

`agent/meterless_hmem.py` implements the H-MEM profile used by VELQIRIS from the official Meterless engine specification: provenance-bearing canonical records, `working` and `long_term` layers, multi-signal retrieval, per-memory trace reasons, local persistence and a tamper-evident trust ledger.

## Verification summary

- 21 / 21 local tests passing.
- H-MEM provenance, retrieval, persistence and ledger tamper detection verified.
- MAD consensus and post-filter spread verified.
- Live mode fails closed without current credentials.
- SHA-256 is described as an integrity digest, not a digital signature.
- Offline fixture values are never presented as live market data.

## Pre-existing technology disclosure

The VELQIRIS brand, initial Python adapters, fixture workflow, MAD consensus logic, local prompt/cost governor and original tests predate the current build window. The H-MEM integration, fail-closed hardening, claim-boundary documentation, evidence receipts and expanded 21-test suite were completed during the current competition window. See `PREEXISTING_TECHNOLOGY.md`.
