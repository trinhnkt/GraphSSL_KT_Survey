# AI assist for Coder B (not a substitute coder)

Official κ in §II requires a **human** Coder B who did not see Coder A, the manuscript tables, or any AI-filled code sheet.

AI may **speed retrieval**. AI may **not** be reported as independent human B.

## Allowed

- Open the PDF in `14_references/` and quote 4–8 passages (SSL / graph / cold-start / ECE) with page or section.
- Point to the codebook token list (no recommended token).
- After B has locked a row, check that the written locator exists on that page (existence check only).

## Not allowed

- Fill `Y`/`N`/`YES`/`NO` or an encoder/family token **for B**.
- Show `inter_rater_coderA_locked_v1.0.csv`, manuscript Table III/V, or `HUMAN_ADOPTED_AI_DRAFT`.
- Compute or write Cohen’s κ into the manuscript from an AI-filled sheet.
- Use `inter_rater_coding_sample_BLIND_v1.0.csv` or `inter_rater_coding_sample_BLIND_EMPTY_v1.2.csv` (AI-filled, not human B).

## What B fills

`08_quality_reliability/inter_rater_coding_sample_BLIND_EMPTY_v1.3.csv`

`coderB_id` = human name or initials, same on every row.

Locator pack (quotes only): `CODER_B_LOCATOR_PACK_v1.1.md`.

## How to use the assistant in this repo

One paper at a time. Human says e.g. `locator KT044`. Assistant returns quotes only. Human assigns the eight fields from the PDF + codebook.

Do not ask the assistant “S = Y hay N?” until the row is already locked by the human.
