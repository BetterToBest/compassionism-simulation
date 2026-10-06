#!/usr/bin/env node
/* Audit fix (Oct 2, 2026, finding V5-01): every STATIC version field must equal META.VERSION.
 * domtest.js already checks the labels the page fills in at run time (.meta-ver, .repl-ver, document.title). This checks what a crawler,
 * a citation tool or a reader with scripts off sees: the static <title>, the JSON-LD blocks, the script banner, the replication page's
 * meta / JSON-LD / seal tooltip, and the CONTRIBUTING.md signature line. Historical mentions ("the v4.22 engine", changelog entries) are
 * deliberately not matched: only the patterns below are. Appendix A's frozen v3.3 dataset (its own "version": "3.5.0") is excluded.
 * Usage: node dev/tools/check_versions.js   (exit 1 and a list if anything is stale). Also exported: findStale(root). */
const fs = require('fs'), path = require('path');
const read = (root, f) => fs.readFileSync(path.join(root, f), 'utf8');
function findStale(root) {
  const idx = read(root, 'index.html'), rep = read(root, 'replication.html'), con = read(root, 'CONTRIBUTING.md');
  const m = idx.match(/var META = \{\s*VERSION:'([^']+)'/); if (!m) throw new Error('META.VERSION not found in index.html');
  const V = m[1], out = [];
  const all = (file, src, field, re) => { let found = 0, x; const g = new RegExp(re.source, 'g');
    while ((x = g.exec(src))) { found++; if (x[1] !== V) out.push({file, field, found: x[1], want: V}); }
    if (!found) out.push({file, field, found: '(field missing)', want: V}); };
  all('index.html', idx, '<title>', /<title>[^<]*? v(\d+(?:\.\d+)+)[^<]*<\/title>/);
  all('index.html', idx, 'JSON-LD softwareVersion', /"softwareVersion":"([^"]+)"/);
  all('index.html', idx, 'static .meta-ver label', /class="meta-ver">v([^<]+)</);
  all('index.html', idx, 'script banner', /COMPASSIONISM FRAMEWORK SIMULATION\s+v(\d+(?:\.\d+)+)/);
  const eeF = path.join(root, 'earlier-engine.html'), ee = fs.existsSync(eeF) ? fs.readFileSync(eeF, 'utf8') : null;  /* v5.2 step 8 (decision D): the earlier engine's own page */
  if (ee){ all('earlier-engine.html', ee, '<title>', /<title>[^<]*? v(\d+(?:\.\d+)+)[^<]*<\/title>/); all('earlier-engine.html', ee, 'JSON-LD softwareVersion', /"softwareVersion":"([^"]+)"/);
    all('earlier-engine.html', ee, 'static .meta-ver label', /class="meta-ver">v([^<]+)</); all('earlier-engine.html', ee, 'script banner', /COMPASSIONISM FRAMEWORK SIMULATION\s+v(\d+(?:\.\d+)+)/); }
  const fdF = path.join(root, 'findings.html'), fd = fs.existsSync(fdF) ? fs.readFileSync(fdF, 'utf8') : null;  /* v5.2.1: the findings explorer */
  if (fd){ all('findings.html', fd, '<title>', /<title>[^<]*? v(\d+(?:\.\d+)+)[^<]*<\/title>/); all('findings.html', fd, 'meta sim-version', /<meta name="sim-version" content="([^"]+)"/); all('findings.html', fd, 'JSON-LD softwareVersion', /"softwareVersion":"([^"]+)"/);
    all('findings.html', fd, 'footer .meta-ver label', /class="meta-ver">v([^<]+)</); all('findings.html', fd, 'site/ cache keys', /(?:src|href)="site\/[a-z]+\.(?:js|css)\?v=([^"]+)"/); }
  all('index.html', idx, 'site/ cache keys', /(?:src|href)="site\/[a-z]+\.(?:js|css)\?v=([^"]+)"/);
  all('replication.html', rep, 'meta sim-version', /<meta name="sim-version" content="([^"]+)"/);
  all('replication.html', rep, 'JSON-LD name', /"name": "Compassionism Framework Simulation v(\d+(?:\.\d+)+)"/);
  const v1 = rep.match(/"version": "([^"]+)"/);
  if (!v1 || v1[1] !== V) out.push({file: 'replication.html', field: "JSON-LD version (the first, the page's own)", found: v1 ? v1[1] : '(missing)', want: V});
  all('replication.html', rep, '.repl-ver labels', /class="repl-ver">v([^<]+)</);
  all('replication.html', rep, 'seal tooltip', /describes engine version (\d+(?:\.\d+)+)/);
  const re2 = /(?:now at v|shipped v)(\d+(?:\.\d+)+)/g; let x; while ((x = re2.exec(rep))) if (x[1] !== V) out.push({file: 'replication.html', field: 'Python-snapshot caveat', found: x[1], want: V});
  all('CONTRIBUTING.md', con, 'signature line', /Compassionism Framework Simulation v(\d+(?:\.\d+)+)\*/);
  const cfF = path.join(root, 'CITATION.cff');  /* v5.2.2 (audit A9): the citation file */
  if (fs.existsSync(cfF)) all('CITATION.cff', fs.readFileSync(cfF, 'utf8'), 'version', /\nversion: (\S+)/);
  for (const [f, src] of [['index.html', idx], ['replication.html', rep]].concat(ee ? [['earlier-engine.html', ee]] : [], fd ? [['findings.html', fd]] : [])) for (const d of src.matchAll(/(?:name="description"|property="og:description") content="([^"]*)"/g))
    if (/\bv\d+\.\d+\b/.test(d[1])) out.push({file: f, field: 'meta description (must not carry a version)', found: (d[1].match(/\bv\d+\.\d+\b/) || [])[0], want: '(none)'});
  return out;
}
module.exports = { findStale };
if (require.main === module) {
  const stale = findStale(path.join(__dirname, '..', '..'));
  if (stale.length) { console.log('STALE version fields:'); stale.forEach(s => console.log('  ' + s.file + ' — ' + s.field + ': found ' + s.found + ', want ' + s.want)); process.exit(1); }
  console.log('every static version field equals META.VERSION');
}
