#!/usr/bin/env node
/* S84 (Nov 17, 2026; research-update PLAN S84): the documents, the manifest and the engine say the same thing about which release they describe.
 * Run in CI (.github/workflows/checks.yml); exit 1 and a list if anything disagrees. What it checks:
 *   - data/manifest.json: the newest release's version (major.minor) equals META.VERSION's; its tag is of that minor; its `docs.describes` equals it;
 *     `docs.engine` equals the round-2 engine commit; every file in `docs.files` exists.
 *   - each of those files names the release it describes; each (except the README, which names none) gives the engine commit; and the "which release"
 *     lines (title or first lines of ODD, MODEL_SPEC, TESTBED_SPEC, ECONOMIST-REVIEW, REPRODUCE, the model card) name the same release; no document
 *     calls an older release "the current release".
 *   - the manifest's stated main-row settings equal the engine's: `docs.mainRow` names a function the harness exports; `docs.backing` equals the
 *     programme arm's full-backing setting; `docs.spendingShare` equals the frozen spending share, and the specification and the review checklist print it.
 * A new release (version 5.10 or later) fails this check until the documents are rebuilt and the manifest's docs field is updated (S83's pattern).
 * Usage: node dev/tools/check_docs_agree.js */
'use strict';
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..'), read = f => fs.readFileSync(path.join(ROOT, f), 'utf8');
const bad = [], note = [];
const need = (ok, msg) => { if (!ok) bad.push(msg); };
const idx = read('index.html'), V = (/var META = \{\s*VERSION:'([^']+)'/.exec(idx) || [])[1];
need(!!V, 'META.VERSION not found in index.html');
const MM = (V || '').split('.').slice(0, 2).join('.');
const manifest = JSON.parse(read('data/manifest.json')), rel = manifest.releases[0], D = rel && rel.docs;
need(rel && rel.version === MM, 'manifest: the newest release is ' + (rel && rel.version) + ', but META.VERSION is ' + V + ' (release ' + MM + ')');
need(rel && rel.status === 'latest', 'manifest: the newest release is not marked "latest"');
need(rel && new RegExp('^v' + MM.replace('.', '\\.') + '\\.\\d+$').test(rel.tag || ''), 'manifest: tag ' + (rel && rel.tag) + ' is not of release ' + MM);
need(!!D, 'manifest: the newest release has no `docs` field');
if (D) {
  need(D.describes === MM, 'manifest docs.describes is ' + D.describes + ', the engine is release ' + MM);
  need(/^[0-9a-f]{7}$/.test(D.engine || ''), 'manifest docs.engine is not a 7-character commit');
  need(!rel.round2 || rel.round2.engine === D.engine, 'manifest: docs.engine ' + D.engine + ' differs from round2.engine ' + (rel.round2 && rel.round2.engine));
  (D.files || []).forEach(f => {
    if (!fs.existsSync(path.join(ROOT, f))) { bad.push('docs.files lists ' + f + ', which does not exist'); return; }
    const t = read(f);
    need(new RegExp('v?' + MM.replace('.', '\\.') + '(?![0-9])').test(t), f + ' does not name release ' + MM);
    if (f !== 'README.md') need(t.indexOf(D.engine) >= 0, f + ' does not give the engine commit ' + D.engine);
    for (const m of t.matchAll(/\b(v\d+\.\d+) is the current release/g)) need(m[1] === 'v' + MM, f + ' calls ' + m[1] + ' "the current release" (release ' + MM + ' is)');
  });
  const first = (f, n) => read(f).split('\n').slice(0, n).join('\n'), v = 'v' + MM, esc = v.replace('.', '\\.');
  need(new RegExp('^# ODD protocol[^\\n]*' + esc + '\\b').test(first('ODD.md', 1)), 'ODD.md: the title does not name ' + v);
  need(new RegExp('^# Model specification: ' + esc + '\\b').test(first('MODEL_SPEC.md', 1)), 'MODEL_SPEC.md: the title does not name ' + v);
  need(new RegExp('How to read this file for ' + esc + '\\b').test(first('TESTBED_SPEC.md', 5)), 'TESTBED_SPEC.md: the reading note does not name ' + v);
  need(new RegExp('^# Economist review checklist \\(' + esc + '\\)').test(first('ECONOMIST-REVIEW.md', 1)), 'ECONOMIST-REVIEW.md: the title does not name ' + v);
  need(new RegExp('^## ' + esc + '\\s*$', 'm').test(read('REPRODUCE.md')), 'REPRODUCE.md: no "## ' + v + '" section');
  need(new RegExp('Describes release ' + esc + '\\b').test(read('model-card.html')), 'model-card.html: does not say "Describes release ' + v + '"');
  /* the manifest's main-row settings against the engine */
  const H = require(path.join(ROOT, 'harness.js'));
  need(typeof H[(D.mainRow || '').split(' ').pop()] === 'function', 'docs.mainRow "' + D.mainRow + '" is not a function the harness exports');
  const S = H.startRelease(); try {
    const rows = H.r2FreezePair(Object.assign({}, H.FULL_INTEGRATION, {years: 20, nAgents: 500}), 'rel');
    const a = rows[1].o && rows[1].o.a;
    need(a === D.backing, 'docs.backing is ' + D.backing + ', the main row\'s programme arm has full backing (o.a) ' + a);
    need(H.SPEND_FROZEN === D.spendingShare, 'docs.spendingShare is ' + D.spendingShare + ', the engine\'s frozen share is ' + H.SPEND_FROZEN);
  } finally { S.restore(); }
  ['MODEL_SPEC.md', 'ECONOMIST-REVIEW.md'].forEach(f => need(read(f).indexOf(String(D.spendingShare)) >= 0, f + ' does not print the spending share ' + D.spendingShare));
  note.push('docs.ageing (' + D.ageing + ') is stated in the manifest and not checked against the engine');
}
if (bad.length) { console.log('DOCUMENTS, MANIFEST AND ENGINE DISAGREE (' + bad.length + '):\n  ' + bad.join('\n  ')); process.exit(1); }
console.log('the documents, the manifest and the engine agree: release ' + MM + ' (engine ' + D.engine + ', ' + (D.files || []).length + ' files, backing ' + D.backing + ', spending share ' + D.spendingShare + ')' + (note.length ? '\n  note: ' + note.join('; ') : ''));
