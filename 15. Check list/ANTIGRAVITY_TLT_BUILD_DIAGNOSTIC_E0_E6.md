# ANTIGRAVITY — IEEE TLT BUILD DIAGNOSTIC E0 → E6
## Use because latest PDF `(4)` is byte-for-byte identical to `(3)`

Target manuscript:
**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Target journal:
**IEEE Transactions on Learning Technologies (IEEE TLT)**

## Problem statement

The newly exported PDF `(4)` is identical to PDF `(3)`. Therefore the latest Antigravity run did not change the compiled manuscript artifact.

Do **not** continue editing scientific content until the active build chain is diagnosed.

---

# E0 — FREEZE CONTENT EDITING

```text
TASK E0 — Freeze manuscript content edits.

Do not change:
- PRISMA numbers
- taxonomy
- QA scores
- figures
- references
- Abstract
- Conclusion

until the active source and build output are proven.

Create:
audit/E0_BUILD_FREEZE.md

Record:
BUILD_DIAGNOSTIC_MODE = ON

STOP.
```

---

# E1 — FIND THE EXACT ACTIVE MANUSCRIPT SOURCE

```text
TASK E1 — Identify which source file actually generates the PDF being exported.

1. Search the entire project for:
   - .tex
   - .docx
   - .md
   - .bib
   - Makefile
   - latexmkrc
   - build scripts
   - export scripts

2. Find every source containing the exact manuscript title:
   "Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings"

3. For each candidate source, record:
   path
   modified time
   file size
   title line
   output directory
   build command

4. Identify duplicate manuscript sources.

5. Identify which file actually produces the PDF copied/exported to the user.

6. Create:
   audit/E1_ACTIVE_SOURCE_INVENTORY.md

Required output table:
Source path | Type | Modified | Build command | Output PDF | Active? | Evidence

Do not edit content yet.

PASS only if exactly one active source is identified.

STOP.
```

---

# E2 — PROVE THE BUILD PATH WITH A TEMPORARY CANARY

```text
TASK E2 — Prove that the identified source controls the exported PDF.

1. In the suspected active source, insert a temporary visible canary:
   "BUILD-CANARY-E2"

Place it in a harmless draft-only location such as:
- immediately after the title in a red draft note, or
- footer/header draft marker.

2. Compile/export the manuscript.

3. Open/render the resulting PDF.

4. Verify the literal string:
   BUILD-CANARY-E2
appears in the PDF.

5. Record:
   source file changed
   build command
   generated PDF path
   PDF modified time
   file size
   checksum/hash

6. Remove the canary.
7. Rebuild again.
8. Confirm canary disappears.

Create:
audit/E2_BUILD_CANARY_PROOF.md

If canary does not appear:
ACTIVE_SOURCE_CONFIRMED = NO
STOP immediately.

If canary appears and disappears correctly:
ACTIVE_SOURCE_CONFIRMED = YES

STOP.
```

---

# E3 — PURGE STALE BUILD/CACHE ARTIFACTS

```text
TASK E3 — Remove stale generated artifacts that may be masking changes.

Only run if E2 PASS.

1. Identify temporary/cache artifacts:
   *.aux
   *.bbl
   *.blg
   *.fls
   *.fdb_latexmk
   *.log
   *.out
   *.toc
   *.synctex.gz
   cached generated PDFs
   old figure exports
   stale intermediate directories

2. Do NOT delete source data.

3. Clean build directory.

4. Rebuild from scratch.

5. Record:
   clean command
   build command
   output PDF
   checksum
   timestamp

6. Verify no old PDF is being copied after compilation by an export script.

Create:
audit/E3_CLEAN_BUILD_AUDIT.md

STOP.
```

---

# E4 — TRACE FIGURE SOURCES

```text
TASK E4 — Find why Figures 1, 2, 4, and 5 remain stale.

For each figure:
Figure 1 PRISMA
Figure 2 unified taxonomy
Figure 4 graph encoder distribution
Figure 5 SSL distribution

1. Find the exact file referenced by the active manuscript:
   e.g. \includegraphics{...}

2. Record:
   source image path
   source generation script
   source CSV/data
   modified time
   checksum

3. Verify whether a newly generated figure is written to the same path actually used by the manuscript.

4. Detect duplicate figure names in multiple directories.

5. For each figure create a temporary visual canary:
   add a small "E4 TEST" marker in the generated test copy,
   rebuild,
   verify the PDF changes,
   then remove marker.

6. Do not alter scientific values yet.

Create:
audit/E4_FIGURE_BUILD_TRACE.md

PASS only if every displayed figure has an identified active source path.

STOP.
```

---

# E5 — TRACE TABLE GENERATION

```text
TASK E5 — Determine whether Tables III–V are generated or manually hard-coded.

1. Locate active source for:
   Table III Graph-KT
   Table IV SSL-KT
   Table V sparse/cold-start

2. For each table determine:
   MANUAL_LATEX
   GENERATED_LATEX
   CSV_TO_LATEX
   DOCX_TABLE
   OTHER

3. If generated:
   locate generation script and input CSV.

4. If manual:
   record that the previous regenerate instructions could not affect the table automatically.

5. Insert one temporary table canary:
   change a non-scientific caption token to "E5-CANARY",
   rebuild,
   confirm it appears,
   revert.

Create:
audit/E5_TABLE_BUILD_TRACE.md

STOP.
```

---

# E6 — BUILD-CHAIN GATE BEFORE SCIENTIFIC PATCH

```text
TASK E6 — Decide whether scientific correction can resume.

Require all:

E1 active source identified = PASS
E2 canary proof = PASS
E3 clean build = PASS
E4 active figure paths = PASS
E5 active table paths = PASS

Then produce:

BUILD_CHAIN_STATUS:
- ACTIVE_SOURCE_CONFIRMED = YES/NO
- CLEAN_BUILD_CONFIRMED = YES/NO
- FIGURE_PATHS_CONFIRMED = YES/NO
- TABLE_PATHS_CONFIRMED = YES/NO
- EXPORTED_PDF_PATH_CONFIRMED = YES/NO

Also report:
active source path
active bibliography path
active figure directory
active table source locations
exact build command
exact final PDF path
final PDF checksum

If every field = YES:
READY_FOR_SCIENTIFIC_PATCH = YES

Otherwise:
READY_FOR_SCIENTIFIC_PATCH = NO

Create:
audit/E6_BUILD_CHAIN_GATE.md

STOP.

Do not resume D1–D7 until READY_FOR_SCIENTIFIC_PATCH = YES.
```

---

# AFTER E6 PASSES

Run the scientific correction set again against the verified active source:

D1 → D2 → D3 → D4 → D5 → D6 → D7

Then compile **from the verified build command only**.

At the end, create a new PDF and report its checksum. Compare it with the old PDF checksum. The new checksum must differ if any visible correction has been applied.
