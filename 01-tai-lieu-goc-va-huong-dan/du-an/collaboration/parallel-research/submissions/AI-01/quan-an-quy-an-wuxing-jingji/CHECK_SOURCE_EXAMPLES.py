#!/usr/bin/env python3
"""AI-01 local sanity checks of historical text case examples.

This intentionally tests a few *textual readings* and the traditional
month/hour gan sequence. It does NOT authenticate a facsimile, make predictions,
run Huyen Hoc Cac engines, or infer universal 官印/鬼印 rules.
"""
from collections import Counter
import json

STEMS = "甲乙丙丁戊己庚辛壬癸"
MONTH_BRANCHES = "寅卯辰巳午未申酉戌亥子丑"
HOUR_BRANCHES = "子丑寅卯辰巳午未申酉戌亥"
MONTH_START = {"甲": "丙", "己": "丙", "乙": "戊", "庚": "戊", "丙": "庚", "辛": "庚", "丁": "壬", "壬": "壬", "戊": "甲", "癸": "甲"}
HOUR_START = {"甲": "甲", "己": "甲", "乙": "丙", "庚": "丙", "丙": "戊", "辛": "戊", "丁": "庚", "壬": "庚", "戊": "壬", "癸": "壬"}
NAYIN_SELECTED = {
    "癸巳": ("水", "長流水"),
    "乙卯": ("水", "大溪水"),
    "己卯": ("土", "城頭土"),
    "丙辰": ("土", "沙中土"),
    "壬辰": ("水", "長流水"),
    "戊戌": ("木", "平地木"),
    "甲戌": ("火", "山頭火"),
    "乙酉": ("水", "泉中水"),
    "癸酉": ("金", "劍鋒金"),
}

def month_pillar(year_stem, month_branch):
    i = MONTH_BRANCHES.index(month_branch)
    start = STEMS.index(MONTH_START[year_stem])
    return STEMS[(start + i) % 10] + month_branch

def hour_pillar(day_stem, hour_branch):
    i = HOUR_BRANCHES.index(hour_branch)
    start = STEMS.index(HOUR_START[day_stem])
    return STEMS[(start + i) % 10] + hour_branch

def nayin_counts(pillars):
    assert all(s in NAYIN_SELECTED for s in pillars)
    return dict(sorted(Counter(NAYIN_SELECTED[s][0] for s in pillars).items()))

# A facsimile has been inspected; the first example's month-stem glyph is still unresolved.
case_a = ["癸巳", "乙卯", "丙辰", "壬辰"]
case_a_ocr_alternative = ["癸巳", "己卯", "丙辰", "壬辰"]
case_b = ["癸巳", "丙辰", "戊戌", "丙辰"]
assert month_pillar("癸", "卯") == "乙卯"
assert month_pillar("癸", "辰") == "丙辰"
assert hour_pillar("丙", "辰") == "壬辰"
assert hour_pillar("戊", "辰") == "丙辰"
assert hour_pillar("甲", "酉") == "癸酉"
assert hour_pillar("甲", "酉") != "乙酉"
assert case_a[1] == month_pillar(case_a[0][0], case_a[1][1])
assert case_a_ocr_alternative[1] != month_pillar(case_a_ocr_alternative[0][0], case_a_ocr_alternative[1][1])
assert case_a[3] == hour_pillar(case_a[2][0], case_a[3][1])
assert case_b[1] == month_pillar(case_b[0][0], case_b[1][1])
assert case_b[3] == hour_pillar(case_b[2][0], case_b[3][1])
assert nayin_counts(case_a) == {"土": 1, "水": 3}
assert nayin_counts(case_a_ocr_alternative) == {"土": 2, "水": 2}
assert nayin_counts(case_b) == {"土": 2, "木": 1, "水": 1}
assert all(s in NAYIN_SELECTED for s in [*case_a, *case_b, "甲戌", "乙酉", "癸酉"])

print(json.dumps({
    "validation": "LOCAL_TEXTUAL_SANITY_ONLY",
    "passed": True,
    "caseA": {"pillars": case_a, "nayinCounts": nayin_counts(case_a), "monthMatchesYearMethod": True, "hourMatchesDayMethod": True},
    "caseA_OCR_alternative": {"pillars": case_a_ocr_alternative, "nayinCounts": nayin_counts(case_a_ocr_alternative), "monthMatchesYearMethod": False},
    "caseB": {"pillars": case_b, "nayinCounts": nayin_counts(case_b), "monthMatchesYearMethod": True, "hourMatchesDayMethod": True},
    "otherReading": {"day": "甲戌", "timeWXJJtext": "乙酉", "timeTMTHtext": "癸酉", "expectedByDefaultDayHourRule": "癸酉"},
    "facsimileInspected": True, "firstExampleMonthStemResolvedFromImage": False,
    "GitHubRepoChanged": False,
    "engineOrNatalPredictions": 0,
    "universalGuanOrGuiSealRulesEstablished": 0,
}, ensure_ascii=False, indent=2))
