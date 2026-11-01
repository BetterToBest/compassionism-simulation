/* s50 packet (research-update step S50): the release row and its no-programme pair, as the published panel runs them
 * (`node harness.js testbed 500 release ref,adv,st --v54 --snab --slope`), for a second, independent implementation to match.
 * It loads the engine exactly as harness.js does (builtSource) and adds this file's code in the same scope, so it can read the switches.
 *
 *   node dev/packets/make_s50_reference.js run ENV LO HI > part.json   per-seed outputs of both rows, seeds LO..HI (ENV ref | adv | st)
 *   node dev/packets/make_s50_reference.js config > config.json        every switch and constant in effect while each row runs (seed 1)
 *   node dev/packets/make_s50_reference.js coverage N OUTDIR           runs seeds 1..N of all six rows under V8 block coverage and writes the code
 *                                                                      that ran (release-row-code.js: blocks that never ran folded; -full.js: whole)
 * Nothing here changes the engine; the rows are built the way the testbed's release section builds them (checked against it in run.txt). */
'use strict';
const path = require('path'), fs = require('fs'), vm = require('vm');
const ROOT = path.join(__dirname, '..', '..');
const H = require(path.join(ROOT, 'harness.js'));
const SRC = H.builtSource();
const URL = 's50-built.js';
/* Every top-level name the built script declares (function NAME, var NAME = ..., var A = 1, B = 2 on the first line). */
const NAMES = (function(){ const out = new Set(); SRC.split('\n').forEach(function(ln){ let m = /^function\s+([A-Za-z_$][\w$]*)/.exec(ln); if (m) out.add(m[1]);
  if (/^var /.test(ln)){ const r = /(?:^var |, *)([A-Za-z_$][\w$]*) *=/g; let x; while ((x = r.exec(ln))) out.add(x[1]); } }); return Array.from(out); })();
const MY = `
var __snapNames = ${JSON.stringify(NAMES)};
function __snap(){ var o = {}; __snapNames.forEach(function(n){ try { var v = eval(n); if (typeof v !== 'function') o[n] = v; } catch (e){} }); return o; }
var __cap = null, __tbRun0 = tbRun;
tbRun = function(p, seed, o, S){ if (__cap && seed === 1) __cap.push({p:JSON.parse(JSON.stringify(p)), o:tbOpts(o), g:__ser(__snap())}); return __tbRun0.apply(this, arguments); };
function __ser(x, up){ up = up || [];  /* plain data: functions left out, typed arrays as arrays (first 2,000), a true cycle marked; shared references are copied */
  if (typeof x === 'number') return isFinite(x) ? x : String(x);
  if (x === null || typeof x !== 'object') return typeof x === 'function' ? undefined : x;
  if (up.indexOf(x) >= 0) return '[cycle]';
  if (ArrayBuffer.isView(x)) return Array.prototype.slice.call(x, 0, 2000).map(function(v){ return isFinite(v) ? v : String(v); });
  var u = up.concat([x]);
  if (Array.isArray(x)) return x.map(function(v){ var s = __ser(v, u); return s === undefined ? null : s; });
  var o = {}; Object.keys(x).forEach(function(k){ var s = __ser(x[k], u); if (s !== undefined) o[k] = s; }); return o; }
/* The release section's pair, as stepSection builds it with --v54 --snab --slope: row 0 the no-programme run, row 1 the release row (j 'release'). */
function __pair(e){
  var ENV = {ref:FULL_INTEGRATION, adv:ADVERSE_REFERENCE, st:STRESS_TEST};
  var P = Object.assign({}, ENV[e]), PR = tbPresets(P), SC = SPEND_SOURCED, SNALL = {abawd:true, slope:true};
  var base = Object.assign({sc:SC, so:REL_V52_STUDY}, {hh:HH_V53, sg:true, g:ACCT_V53, em:true, fb:true}, {v54:V54_MAIN}, {snAll:SNALL});
  var rel = releaseRowsV54(SC).filter(function(r){ return r.k !== 'a' && r.j === 'release'; })[0];
  var c0 = Object.assign({p:PR.baseline()}, base); delete c0.snAll;
  var c1 = n1Row(PR, 'framework', rel.v); if (rel.v.o) Object.assign(c1.o || (c1.o = {}), rel.v.o);
  [c0, c1].forEach(function(c){ c.sn = Object.assign({}, SNALL); });
  var o = Object.assign({}, {fin:'tax', aT:0, a:0, X:0}, REL_V52_STUDY, {sc:SC});
  return {P:P, cfg:[c0, c1], o:o, label:['No programme', rel.l]};
}
/* The testbed mode's profile: the debt floor at -$10,000, the NR6 accounting profile, N7_BLEI (TB_PROFILE_G). */
function __profile(fn){ var wf = CFG.WEALTH_FLOOR, svN = applyNR6(), svG = tbSetG(TB_PROFILE_G); CFG.WEALTH_FLOOR = -10000;
  try { return fn(); } finally { CFG.WEALTH_FLOOR = wf; resetNR6(svN); tbSetG(svG); } }
module.exports.run = function(e, lo, hi){ return __profile(function(){ var X = __pair(e), R = tbStudy(X.cfg, hi, X.P, X.o, lo);
  return R.map(function(r, i){ var s = {}; Object.keys(r._s).sort().forEach(function(k){ s[k] = Array.prototype.slice.call(r._s[k]); }); return {row:i ? 'release' : 'base', label:X.label[i], seeds:s}; }); }); };
module.exports.config = function(e){ var g0 = __ser(__snap()); return __profile(function(){ var X = __pair(e); __cap = [];
  try { tbStudy(X.cfg, 1, X.P, X.o, 1); } finally { var C = __cap; __cap = null; }
  return {rows:C.map(function(c, i){ var d = {}; Object.keys(c.g).forEach(function(k){ if (JSON.stringify(c.g[k]) !== JSON.stringify(g0[k])) d[k] = c.g[k]; });
    return {row:i ? 'release' : 'base', label:X.label[i], rowConfig:__ser(X.cfg[i]), preset:c.p, options:c.o, switchesDifferentFromLoad:d}; }), studyOptions:X.o, env:__ser(X.P), atLoad:g0}; }); };
module.exports.manifest = function(){ return runManifest(__dirname); };
`;
function load(){ const mod = {exports:{}};
  vm.runInThisContext('(function (require, module, exports, __dirname, __filename, builtSource, csEngineSource) {' + SRC + '\n' + MY + '\n})', {filename:URL})(require, mod, mod.exports, ROOT, path.join(ROOT, 'harness.js'), H.builtSource, H.csEngineSource);
  return mod.exports; }
const mode = process.argv[2];
if (mode === 'run'){ const e = process.argv[3], lo = +process.argv[4], hi = +process.argv[5], X = load(), t = Date.now();
  const rows = X.run(e, lo, hi);
  process.stdout.write(JSON.stringify({about:'s50 reference: release row and its no-programme pair, per-seed outputs (tbStudy _s arrays), env ' + e + ', seeds ' + lo + '-' + hi, env:e, lo:lo, hi:hi, seconds:(Date.now() - t)/1000, manifest:X.manifest(), rows:rows}));
} else if (mode === 'config'){ const X = load(), out = {about:'s50: switches and constants in effect while each row runs (captured at the tbRun call for seed 1). switchesDifferentFromLoad: top-level values that differ from the engine at load. atLoad: every top-level value at load (functions left out).', manifest:X.manifest(), envs:{}};
  ['ref', 'adv', 'st'].forEach(function(e){ const c = X.config(e); out.envs[e] = {env:c.env, studyOptions:c.studyOptions, rows:c.rows}; out.atLoad = c.atLoad; });
  process.stdout.write(JSON.stringify(out, null, 1));
} else if (mode === 'coverage'){ const N = +process.argv[3], OUT = process.argv[4], inspector = require('inspector'), S = new inspector.Session(); S.connect();
  S.post('Profiler.enable', function(){ S.post('Profiler.startPreciseCoverage', {callCount:true, detailed:true}, function(){
    const X = load(); ['ref', 'adv', 'st'].forEach(function(e){ X.run(e, 1, N); });
    S.post('Profiler.takePreciseCoverage', function(err, res){ if (err) throw err;
      const sc = res.result.filter(function(s){ return s.url === URL; })[0]; writeCode(sc.functions, N, OUT); }); }); });
} else { console.error('usage: run ENV LO HI | config | coverage N OUTDIR'); process.exit(1); }

/* The code that ran, by top-level statement of the built script, in source order. A statement is included when any function in it ran, or when it
 * declares a value (var) that code which ran names. Each carries the file and line it comes from (index.html or harness.js). */
function writeCode(fns, N, OUT){
  const W = '(function (require, module, exports, __dirname, __filename, builtSource, csEngineSource) {', base = W.length;  /* offsets are into the compiled text */
  const starts = new RegExp("^(function |var |CFG\\.[A-Z_]+ *=|Object\\.assign\\(module\\.exports|/\\*|if *\\(|window\\.|document\\.|REL_HUB\\.|[A-Za-z_$][\\w$]*\\.[\\w$.]+ *=[^=]|[A-Za-z_$][\\w$]*\\()");
  const lines = SRC.split('\n'), chunks = []; let off = 0, cur = null;
  lines.forEach(function(ln){ if (starts.test(ln) || !cur){ if (cur) chunks.push(cur); cur = {a:off, text:[]}; } cur.text.push(ln); off += ln.length + 1; });
  chunks.push(cur); chunks.forEach(function(c){ c.text = c.text.join('\n'); c.b = c.a + c.text.length; });
  /* attach column-0 comment chunks to the declaration that follows them */
  const units = []; let pend = [];
  chunks.forEach(function(c){ if (/^\/\*[\s\S]*\*\/\s*$/.test(c.text) && !/\*\/\s*\S/.test(c.text)){ pend.push(c); return; } units.push({parts:pend.concat([c]), main:c}); pend = []; });
  const mark = '/* ==== HARNESS' + '-ONLY CODE ==== */', hk = SRC.indexOf(mark);
  const I = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8'), Hs = fs.readFileSync(path.join(ROOT, 'harness.js'), 'utf8');
  function origin(c){ const inH = c.a >= hk, F = inH ? Hs : I, k = F.indexOf(c.text); return k < 0 ? (inH ? 'harness.js' : 'index.html') + ' (line not found)' : (inH ? 'harness.js' : 'index.html') + ' line ' + (F.slice(0, k).split('\n').length); }
  function declared(t){ let m = /^function ([A-Za-z_$][\w$]*)/.exec(t); if (m) return [m[1]];
    if (t.indexOf('var ') === 0){ const r = /(?:^var |, *)([A-Za-z_$][\w$]*) *=/g, first = t.split('\n')[0]; let x, names = []; while ((x = r.exec(first))) names.push(x[1]); return names; }
    m = /^(CFG\.[A-Z_]+) *=/.exec(t); return m ? [m[1]] : []; }
  /* ranges: [a, b, count] in SRC offsets */
  const ran = [], zero = [];
  fns.forEach(function(f){ f.ranges.forEach(function(r, i){ const a = r.startOffset - base, b = r.endOffset - base; if (a < 0 || b > SRC.length) return; (r.count > 0 ? ran : zero).push([a, b, r.count, i === 0]); }); });
  units.forEach(function(u){ const c = u.main; u.names = declared(c.text); u.ran = ran.some(function(r){ return r[3] && r[0] >= c.a && r[1] <= c.b && r[2] > 0; }); u.engine = c.a < hk; });
  /* include: ran, or a value named by included code (closure over names) */
  const byName = {}; units.forEach(function(u){ u.names.forEach(function(n){ (byName[n] = byName[n] || []).push(u); }); });
  const inc = new Set(units.filter(function(u){ return u.ran && u.names.length; }));
  let grew = true; while (grew){ grew = false; Array.from(inc).forEach(function(u){ const toks = u.main.text.match(/[A-Za-z_$][\w$]*/g) || [];
    toks.forEach(function(t){ (byName[t] || []).forEach(function(v){ if (!inc.has(v) && !/^function /.test(v.main.text)){ inc.add(v); grew = true; } });
      if (t === 'CFG') units.forEach(function(v){ if (/^CFG\./.test(v.main.text) && !inc.has(v)){ inc.add(v); grew = true; } }); }); }); }
  /* functions named by code that ran but never called in these rows: listed, not included */
  const ranNames = new Set(); inc.forEach(function(u){ u.names.forEach(function(n){ ranNames.add(n); }); });
  const notRun = new Set(); inc.forEach(function(u){ (u.main.text.match(/[A-Za-z_$][\w$]*/g) || []).forEach(function(t){ (byName[t] || []).forEach(function(v){ if (!inc.has(v) && /^function /.test(v.main.text)) notRun.add(v); }); }); });
  function fold(u){ /* the unit's text with the outermost never-run ranges inside it replaced by a marker */
    const a0 = u.parts[0].a, b0 = u.main.b, Z = zero.filter(function(z){ return z[0] >= a0 && z[1] <= b0; }).sort(function(x, y){ return x[0] - y[0] || y[1] - x[1]; }), top = [];
    Z.forEach(function(z){ if (!top.length || z[0] >= top[top.length - 1][1]) top.push(z); });
    let t = SRC.slice(a0, b0); top.slice().reverse().forEach(function(z){ const s = SRC.slice(z[0], z[1]), nl = (s.match(/\n/g) || []).length;
      t = t.slice(0, z[0] - a0) + '⟦not run' + (nl ? ', ' + (nl + 1) + ' lines' : '') + '⟧' + t.slice(z[1] - a0); }); return t; }
  const list = units.filter(function(u){ return inc.has(u); });
  const hdr = '// The Compassionism Simulation engine: the code that the release row and its no-programme pair run (Reference, Adverse and Stress), in source order.\n' +
    '// Cut by dev/packets/make_s50_reference.js from the script harness.js builds (index.html\'s engine first, then harness.js\'s own code), under V8 block coverage over seeds 1-' + N + ' of all six rows.\n' +
    '// Included: every top-level function that ran, and every top-level value such code names. Each piece is headed by the file and line it comes from.\n';
  const fold1 = hdr + '// In this file, code inside an included function that never ran in those runs is folded to ⟦not run⟧ (the whole text is in release-row-code-full.js).\n' +
    '// "Never ran" is measured, not proved: a branch that runs only on a rare seed would be folded too, so check release-row-code-full.js before relying on a fold.\n\n';
  const full1 = hdr + '// The whole text of each included piece (release-row-code.js has the same pieces with the parts that never ran folded).\n\n';
  fs.mkdirSync(OUT, {recursive:true});
  fs.writeFileSync(path.join(OUT, 'release-row-code.js'), fold1 + list.map(function(u){ return '// ' + origin(u.main) + '\n' + fold(u); }).join('\n\n') + '\n');
  fs.writeFileSync(path.join(OUT, 'release-row-code-full.js'), full1 + list.map(function(u){ return '// ' + origin(u.main) + '\n' + SRC.slice(u.parts[0].a, u.main.b); }).join('\n\n') + '\n');
  const nr = Array.from(notRun).sort(function(x, y){ return x.main.a - y.main.a; });
  fs.writeFileSync(path.join(OUT, 'not-run.md'), '# Functions named in the release row\'s code that never ran in these rows\n\nUnder V8 block coverage over seeds 1-' + N + ' of the six rows (release row and no-programme run; Reference, Adverse, Stress), these top-level functions are named by code that ran but were never called: they belong to switches that are off, or to other study modes. They are not in the packet.\n\n' +
    nr.map(function(u){ return '- `' + u.names.join(', ') + '` (' + origin(u.main) + ', ' + u.main.text.split('\n').length + ' lines)'; }).join('\n') + '\n');
  console.log(JSON.stringify({included:list.length, functionsRan:list.filter(function(u){ return /^function /.test(u.main.text); }).length, values:list.filter(function(u){ return !/^function /.test(u.main.text); }).length, notRun:nr.length,
    linesFull:list.reduce(function(m, u){ return m + SRC.slice(u.parts[0].a, u.main.b).split('\n').length; }, 0)}));
}
