"""Builds the chat packets for the free plan (ledger s135): s148 (four outside-audit prompts) and s119 (CoMSES text and fact sheet).
Usage: python3 -I dev/packets/build_chat_packets.py <release-summary.json> ; writes the zips beside this file. The s118 packet has its own builder."""
import sys, zipfile, os
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(os.path.dirname(P))
def z(name, files):
    with zipfile.ZipFile(os.path.join(P, name), 'w', zipfile.ZIP_DEFLATED) as zf:
        for arc, src in files: zf.write(src, arc)
    print(name, os.path.getsize(os.path.join(P, name)), 'bytes')
common = [('ODD.md', R + '/ODD.md'), ('MODEL_SPEC.md', R + '/MODEL_SPEC.md'), ('ECONOMIST-REVIEW.md', R + '/ECONOMIST-REVIEW.md'), ('ledger-open-items-oct15.md', R + '/dev/background/ledger-open-items-oct15.md')]
z('s148-outside-audits.zip', [('00-START-HERE.md', P + '/src/s148-brief.md'), ('next-study-audit-prompt.md', R + '/dev/plans/next-study-audit-prompt.md')] + [('prompt-%s.md' % k, P + '/src/prompt-%s.md' % k) for k in 'ABCD'] + common)
z('s119-comses-and-fact-sheet.zip', [('00-START-HERE.md', P + '/src/s119-brief.md'), ('release-summary.json', sys.argv[1]), ('ODD.md', R + '/ODD.md'), ('REPRODUCE.md', R + '/REPRODUCE.md'), ('README.md', R + '/README.md'), ('CITATION.cff', R + '/CITATION.cff'), ('ECONOMIST-REVIEW.md', R + '/ECONOMIST-REVIEW.md')])
