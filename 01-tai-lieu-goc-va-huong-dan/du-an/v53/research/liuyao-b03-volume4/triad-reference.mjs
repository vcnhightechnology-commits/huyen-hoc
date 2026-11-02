// Private source-specific prerequisites. A candidate is not an effective formation or verdict.
import {readFileSync} from 'node:fs';
import {compile} from '../liuyao-foundations/liuyao-reference.mjs';
const tables = JSON.parse(readFileSync(new URL('TRIAD_TABLES.json', import.meta.url), 'utf8'));
export function triadCoordinates(values, ...extra) {
  if (extra.length) throw TypeError('Only six explicit values; calendar/strength/changed-line completion unsupported.');
  const chart = compile(values);
  const groups = tables.groups.map(group => {
    const positionsByMember = group.members.map(branch => ({branch,
      lines: chart.lines.filter(line => line.branch === branch).map(line => line.line)}));
    const missingMembers = positionsByMember.filter(x => !x.lines.length).map(x => x.branch);
    const witnesses = [];
    // One line per distinct branch prevents duplicate copies of a branch supplying a missing member.
    for (const a of positionsByMember[0].lines)
      for (const b of positionsByMember[1].lines)
        for (const c of positionsByMember[2].lines) {
          const lines = [a,b,c];
          const movingLines = lines.filter(n => chart.lines[n-1].moving);
          witnesses.push({lines, movingLines, movingCount: movingLines.length,
            structuralPrerequisitesPresent: movingLines.length >= 2});
        }
    const eligible = witnesses.filter(x => x.structuralPrerequisitesPresent);
    return {...structuredClone(group), positionsByMember, missingMembers, witnesses,
      completePrimaryMembership: missingMembers.length === 0,
      preliminaryGate: missingMembers.length ? 'incomplete-members'
        : eligible.length ? 'structural-prerequisites-present' : 'moving-premise-not-present',
      qualifyingWitnesses: eligible.length,
      effectiveFormation: null, transformedElement: null, auspicious: null};
  });
  return {schema: 'hhc.liuyao.B03.primary-triad-prerequisites.v1', sourceID: 'B03-book2',
    sourcePDFPage: 39, chart, groups, primaryOnly: true,
    changedOrCalendarBranchesUsedToCompleteGroups: false,
    fullStrengthModel: null, sourceQualifiedFormation: null, predictedEvent: null,
    twoMemberAndSelfPunishmentImplemented: false, consumerApplied: false};
}
