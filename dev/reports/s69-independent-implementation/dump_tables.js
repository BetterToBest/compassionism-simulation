// Reads the packet's code excerpt as text, evaluates its top-level declarations in a sandbox, and writes the
// non-function top-level values (data tables and constants) as JSON. No engine function is called.
const fs = require('fs'), vm = require('vm');
const src = fs.readFileSync(process.argv[2], 'utf8');
const ctx = {console, Math, JSON, Object, Array, Float64Array, Number, String, Error, isNaN, isFinite, Infinity, NaN};
vm.createContext(ctx);
// strip "const/let" to var so declarations land on the context
vm.runInContext(src, ctx, {filename: 'main-row-code-full.js'});
const out = {};
for (const k of Object.keys(ctx)) { const v = ctx[k]; if (typeof v === 'function') continue; try { out[k] = JSON.parse(JSON.stringify(v)); } catch (e) {} }
fs.writeFileSync(process.argv[3], JSON.stringify(out));
console.log(Object.keys(out).length + ' values');
