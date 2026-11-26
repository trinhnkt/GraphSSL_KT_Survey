# VX PDF acquisition checklist (Step 1 — sequential)

**Date:** 2026-11-25  
**Drop folder:** `06_fulltext/papers/venue_probe_vx/`  
**Rule:** Without a real full PDF (or OA full-text extract), decision stays `UNCERTAIN` and corpus freeze stays blocked.

## Already deposited (do not re-download)

| ID | File | AI gateway |
|---|---|---|
| VX01 | `VX01_AGKT.pdf` | PRIMARY_CORE (G only) |
| VX03 | `VX03_GRKT.pdf` | PRIMARY_CORE (G only) |
| VX05 | `VX05_HCMKT.pdf` | PRIMARY_CORE (already KT086) |
| VX07 | `VX07_TransKT.pdf` | PRIMARY_CORE (G∩S) |
| VX10 | `VX10_KGSKT_OA_extract.txt` (OA HTML) | PRIMARY_CORE (G∩S) |

## Need author download (agent blocked: 403/420/paywall)

Place files with these exact names in the drop folder, then reply: `PDF ready`.

| ID | Save as | DOI / URL | OA? |
|---|---|---|---|
| VX02 | `VX02_ExpertGraphs_LAS2024.pdf` | https://doi.org/10.1145/3657604.3664683 | No (ACM) |
| VX04 | `VX04_BiCo.pdf` | https://doi.org/10.1145/3638055 | ACM OA PDF URL exists but Cloudflare-blocked here |
| VX06 | `VX06_GCLFKT.pdf` | https://doi.org/10.1109/iceit64364.2025.10976145 | No (IEEE) |
| VX08 | `VX08_SCDI.pdf` | https://doi.org/10.1109/access.2025.3542870 (IEEE doc **10891379**) | IEEE Access usually OA; stamp download blocked (420) from this host |
| VX09 | `VX09_MSCL.pdf` | https://doi.org/10.1016/j.neucom.2026.133837 | No (ScienceDirect) |

## After files land

Agent will, in order:
1. `pdftotext` + gateway re-code each row in `KNOWN_CANDIDATES_FULLTEXT_REVIEW_v1.csv`
2. Update `audit/KNOWN_CANDIDATES_GATEWAY_AUDIT.md`
3. Only if zero UNCERTAIN-for-missing-PDF → build `06_coding/PRIMARY_CORE_FINAL_v2.csv`
