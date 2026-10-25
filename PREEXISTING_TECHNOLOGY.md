# Pre-existing technology disclosure

**Submission:** VELQIRIS — The Agent That Can Explain Why  
**Current official build window:** 22 October 2026, 00:00 UTC to 27 October 2026, 23:45 UTC

## Disclosure

The base files in `competition_submissions/open_agent_2026/` have local modification timestamps from 15 October 2026, before the current official build window. They must therefore be treated as pre-existing product code unless stronger provenance proves otherwise.

Pre-existing material includes:

- the VELQIRIS brand and broader product concepts;
- the initial Python adapters and local fixture workflow;
- the initial MAD consensus logic;
- the original local prompt/cost governor;
- the original tests and draft documentation.

## Work completed during the current window

Record only changes with verifiable provenance dated within the official build window. The reviewed hardening patch dated 25 October 2026 includes:

- explicit separation of live mode and fixture simulation;
- fail-closed behavior when live credentials are missing;
- removal of simulated Nemotron and Meterless claims;
- correction of post-filter spread calculation;
- accurate SHA-256 integrity terminology;
- expanded local regression coverage from 11 to 21 tests;
- corrected competition documentation.
- Meterless H-MEM core implementation with canonical provenance records, hierarchical layers, hybrid retrieval trace, local persistence, and a hash-chained trust ledger;
- five dedicated H-MEM contract tests and end-to-end H-MEM receipt assertions, bringing the suite to 21 passing tests.

If this patch is not adopted into the submission repository with reliable commit provenance, do not claim it as submitted work.

## Sponsor-work disclosure

- **Zetaris:** request adapter exists; live execution evidence is pending.
- **Meterless:** the new H-MEM integration profile is build-window work. The older `MeterlessGovernor` remains project-local cost arithmetic and is not presented as provider billing telemetry.
- **External model adapter:** a generic OpenAI-compatible adapter exists; no live provider output is claimed in this release.
- **Cursor:** do not claim use unless supported by development records.

This disclosure should be included in, or linked from, the final submission description and repository README.
