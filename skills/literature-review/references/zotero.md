# Zotero libraries (optional)

Use only when the user points to a Zotero library or collection and the host can reach it. The core workflow does not require Zotero; a supplied BibTeX file, PDFs, or reference list works the same way.

## Reaching the library

- Desktop local API: recent Zotero desktop versions expose the Web API under `http://localhost:23119/api/` when Settings → Advanced → "Allow other applications on this computer to communicate with Zotero" is enabled. Use user ID `0`, for example `/api/users/0/collections` and `/api/users/0/collections/{collectionKey}/items/top`. Local results are not paginated by default. Reads need no authentication.
- Treat the library as read-only. Newer versions accept write requests after the user grants a local key; do not request one or change the library unless the user asks.
- Zotero web API (`api.zotero.org`): private libraries require the user's API key. Use one only if the user has supplied or configured it.
- A host-provided Zotero tool or connector may be used if available; do not assume one exists.

If the library is unreachable because the desktop app is closed or the setting is off, ask the user to enable it or export the collection as BibTeX. Never substitute remembered papers for the user's library.

## Scope, keys, and full text

Work from the named collection and search outside it only to fill gaps you name. Zotero item keys (8-character identifiers) are not citation keys. Use the keys in the user's existing `.bib` or the library's citation-key field (native in recent Zotero versions; earlier setups often use Better BibTeX), and check that exported keys match those used in the manuscript. Preserve existing keys.

When the user asks for synthesis or evidence from their collection, reading attached full text is in scope; record the read depth for each item. Library metadata can be wrong, so run the reference verification in [Search and verification](search-and-verification.md) on the exported entries before delivery.

Documentation checked October 26, 2026: [Zotero local API](https://www.zotero.org/support/dev/web_api/v3/local_api), [Web API basics](https://www.zotero.org/support/dev/web_api/v3/basics), and [Better BibTeX](https://retorque.re/zotero-better-bibtex/).
