# -*- coding: utf-8 -*-
"""Record the 2026-11-23 attempt on the four unfinished rerun rows.
Does not invent an export file or a rerun count.
"""
import csv

PATH = r"D:\TRINH\GraphSSL_KT_Survey\03_search\rerun_16_queries_TEMPLATE_2026-11-13.csv"
NOTES = {
    "SRCH_001": "2026-11-23 Basic Edition, signed out. All-field query plus E-Publication Date 2015-01-01 to 2026-07-31 showed 507 results. The search area was Anywhere, not Title/Abstract/Keywords. English and Journal/Conference filters were not applied. Download citation was disabled. No file saved. The 507 is a screen observation and is not the rerun count.",
    "SRCH_002": "2026-11-23 same Basic Edition session. All-field query plus E-Publication Date 2015-01-01 to 2026-07-31 showed 441 results. Download citation was disabled. No file saved. The 441 is a screen observation and is not the rerun count.",
    "SRCH_011": "2026-11-23 Web of Science advanced search redirected to the Clarivate sign-in page. No institutional session was available. No file saved and no result count was shown.",
    "SRCH_012": "2026-11-23 not run separately. The same Clarivate sign-in page blocks both Web of Science searches. No file saved and no result count was shown.",
}
with open(PATH, encoding="utf-8", newline="") as fh:
    rows = list(csv.reader(fh))
for row in rows[1:]:
    note = NOTES.get(row[0])
    if not note:
        continue
    row[12] = "2026-11-23"
    row[13] = "BLOCKED_NO_FILE"
    row[14] = "NONE"
    row[15] = note
with open(PATH, "w", encoding="utf-8", newline="") as fh:
    writer = csv.writer(fh)
    writer.writerows(rows)
print("updated", list(NOTES))
