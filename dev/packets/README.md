# Chat packets for the free plan (ledger step s135)

Each zip is one task for a plain chat (no repository access). Open the zip, read `00-START-HERE.md`, attach the files, paste the prompt.

| Zip | Task | Builder |
|---|---|---|
| `s118-second-implementation.zip` | A second, independent Python implementation of the core yearly loop, checked against the engine's results | `build_s118_packet.py` (reference outputs: `make_s118_reference.js`) |
| `s148-outside-audits.zip` | Four outside audits (arithmetic, assumptions, health claims, press-readiness) and the sorting chat | `build_chat_packets.py` |
| `s119-comses-and-fact-sheet.zip` | The CoMSES model-library text and the wide-audience fact sheet | `build_chat_packets.py` (figures: `make_release_summary.py`) |

`dev/background/ledger-open-items-oct15.md` is a copy of the ledger's open items (made by `ledger_open_items.py`). Rebuild the packets after any release: the reference outputs and the release summary are tied to the engine and the release file in the repository.
