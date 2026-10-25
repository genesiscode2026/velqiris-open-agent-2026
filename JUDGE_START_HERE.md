# Judge start here — VELQIRIS

## Current, evidence-backed status

VELQIRIS is a prototype evidence agent for Track 02. The current repository demonstrates the local mathematical and orchestration path, with explicit separation between fixtures and live services.

```bash
python3 tests/run_all_tests.py
python3 agent/cli.py --dry-run
```

The test suite contains 21 local tests. The dry run uses built-in fixture rows and a labelled placeholder model response. It does **not** call a live Zetaris environment or external model. It does execute the local-first Meterless H-MEM profile and records its receipt in the evidence payload.

## Fail-closed live mode

```bash
python3 agent/cli.py
```

Without valid Zetaris credentials, a Zetaris organization ID, a model API key, and an exact current model identifier, the command exits non-zero and does not synthesize a successful result.

## What remains before submission

1. Execute and preserve a redacted live Zetaris query receipt.
2. Integrate a real Meterless engine into the product workflow.
3. Optionally execute a currently available external model and preserve a redacted receipt; no provider-specific model output is required for the verified local H-MEM profile.
4. Record a new 1–4 minute demo showing those live integrations.
5. Publish this event-specific code in the repository linked from HackOS.
6. Disclose all pre-existing product code and identify work completed during the official build window.

See `VERIFICATION_STATUS.md` for the evidence matrix and `PREEXISTING_TECHNOLOGY.md` for the required disclosure.
