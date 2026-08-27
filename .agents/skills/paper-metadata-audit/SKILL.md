---
name: paper-metadata-audit
description: Audits scientific-paper metadata and DOI/version conflicts for the KT survey using official publisher and proceedings sources.
---

# Paper metadata audit

Check:
- title;
- authors;
- year;
- venue;
- volume/issue/pages/article number;
- DOI;
- publication type;
- peer-reviewed status;
- preprint/publisher relationship;
- conference/journal extension relationship.

Never overwrite a conflicting value silently.
Write the conflict into the metadata audit log.
