import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import vm from 'node:vm';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../../../../../');
const enginePath = resolve(root, 'v53/engine.js');
const reportPath = resolve(here, 'AI01_ENGINE_EXAMPLE_AUDIT_2026-11-01.json');
const engineBytes = await readFile(enginePath);
const context = { window: {} };
vm.createContext(context);
vm.runInContext(engineBytes.toString('utf8'), context, { filename: enginePath });

const engine = context.window.HHC_ENGINE;
assert.equal(typeof engine?.bazi, 'function', 'The current project engine must expose HHC_ENGINE.bazi.');

const examples = [
  {
    id: 'WXJJ-TMTH-GUAN-SEAL-EXAMPLE',
    sourceReading: ['癸巳', '乙卯', '丙辰', '壬辰'],
    input: { y: 1953, m: 3, d: 6, hour: 7, minute: 0, tz: 7 },
  },
  {
    id: 'WXJJ-GUI-SEAL-EXAMPLE',
    sourceReading: ['癸巳', '丙辰', '戊戌', '丙辰'],
    input: { y: 1953, m: 4, d: 17, hour: 7, minute: 0, tz: 7 },
  },
];

const results = examples.map(({ id, sourceReading, input }) => {
  const result = engine.bazi(input);
  const enginePillars = Array.from(result.pillars, pillar => pillar.han);
  assert.deepEqual(enginePillars, sourceReading, `${id}: actual engine pillars must match the source example.`);
  return {
    id,
    input,
    sourceReading,
    enginePillars,
    dayMaster: result.dayMaster.han,
    nearBoundary: result.nearBoundary,
    engineMatched: true,
  };
});

const alternativeInput = examples[0].input;
const alternativeResult = Array.from(engine.bazi(alternativeInput).pillars, pillar => pillar.han);
const ocrAlternative = ['癸巳', '己卯', '丙辰', '壬辰'];
const report = {
  schema: 'hhc.ai01.real-engine-example-audit.v1',
  date: '2026-11-01',
  engine: {
    file: 'v53/engine.js',
    bytes: engineBytes.length,
    sha256: createHash('sha256').update(engineBytes).digest('hex'),
    function: 'HHC_ENGINE.bazi',
    execution: 'Loaded the current project engine.js in a Node VM; no mock engine or reimplementation.',
  },
  timezoneConvention: '+07:00 (explicit test input; not asserted as the historical source location/timezone)',
  examples: results,
  ocrAlternativeCheck: {
    id: 'WXJJ-TMTH-GUAN-SEAL-EXAMPLE-month-stem-variant',
    input: alternativeInput,
    proposedReading: ocrAlternative,
    enginePillarsAtSameInput: alternativeResult,
    rejectedByCurrentEngineAtSameInput: alternativeResult.join('') !== ocrAlternative.join(''),
    scope: 'The engine returns 乙卯 for this generated date. This checks the project calendar convention only; it does not by itself read the manuscript glyph.',
  },
  interpretationLimits: [
    'These are constructed civil-date realizations of the quoted four-pillar strings under the current engine; they are not claimed as historical birth records.',
    'A pillar match verifies internal calendar consistency only, not the traditional 官印/鬼印 classification or its predictive efficacy.',
    'The unknown/ambiguous manuscript glyph remains a source-collation question and must not be silently replaced by engine output.',
  ],
  consumerEngineChanged: false,
  consumerSiteChanged: false,
};

await writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, 'utf8');
console.log(JSON.stringify(report, null, 2));
