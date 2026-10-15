Paste this into a new chat together with the files from the zip.

---

You are helping check a published agent-based model. The attached files are a written description of the model (`ODD.md`, `MODEL_SPEC.md`), the real code's core (`core-loop.js`), the real code's results (`reference-outputs.json`), and a brief (`00-START-HERE.md`). Read the brief first and follow it exactly.

Rules:
- Write the Python program from the written description first. Open `core-loop.js` only when the description does not settle a question, and keep a numbered list of each such question and what the code said.
- Do not tune any constant or rule to make a number agree. Report disagreements.
- Do the presets in the order the brief gives, and stop at the first one you cannot match, saying why.
- Work in small steps and show the comparison table after each preset.
- Write the final report for a reader who is not a programmer or economist. Do not use bare labels such as step or decision numbers.
- If you run out of room, say which preset and which key you reached, and write down exactly what the next chat should do.
