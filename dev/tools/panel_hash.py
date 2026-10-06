"""v5.2.2 (audit A8; REPRODUCE.md): a fingerprint of a run file's results that a fresh run can be compared with.

A run file (dev/runs/*.json) records its results and, under "_meta", how and when it was made (commit, date, seconds, Node version). A rerun of
the same command on the same engine gives the same results but a different "_meta", so the file's own hash cannot match. This prints the
SHA-256 of everything except "_meta", written canonically (keys sorted, no spaces, numbers as Python writes them: the shortest form that
reads back as the same double, which is also what JavaScript writes), and its first 16 hex digits, which REPRODUCE.md lists.

Usage: python3 dev/tools/panel_hash.py FILE [FILE ...]
"""
import hashlib, json, sys

def fingerprint(path):
    with open(path, encoding='utf-8') as f:
        d = json.load(f)
    if isinstance(d, dict):
        d = {k: v for k, v in d.items() if k != '_meta'}
    s = json.dumps(d, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        h = fingerprint(p)
        print(h[:16], h, p)
