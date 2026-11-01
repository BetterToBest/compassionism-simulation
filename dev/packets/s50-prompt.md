Paste this into a fresh session (Claude Code on the repository, or a plain chat with the files from the zip). The session must not have read the engine.

---

You are helping check a published agent-based model. The attached packet holds a written description of the model (`MODEL_SPEC.md`, `ODD.md`), every setting of the two runs as data (`release-config.json`), the real code that those runs execute (`code/`), the real code's results for 500 seeds (`reference/`), and a brief (`00-START-HERE.md`). Read the brief first and follow it exactly.

Rules:
- Write the Python program from the written description first. Open the code excerpt only when the description does not settle a question, and keep a numbered list of each such question and what the code said.
- Do not open any other part of the engine or the repository's results until your phase-1 program and results are committed.
- Do not tune any constant or rule to make a number agree. Report disagreements.
- Do the runs in the order the brief gives, and stop at the first one you cannot match, saying why.
- Work in small steps and show the comparison table after each run.
- Write the final report for a reader who is not a programmer or economist. Do not use bare labels such as step or decision numbers.
- If you run out of room, commit what you have, say which run and which key you reached, and write down exactly what the next session should do.
