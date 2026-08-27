#!/usr/bin/env python3
"""
Deterministic Generator for SOURCES.md (ANANKE-001 & ANANKE-002)
Parses all sources/*.md metadata files and creates the consolidated register table.
"""

import os
import glob
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES_DIR = os.path.join(REPO_DIR, 'sources')
OUTPUT_FILE = os.path.join(SOURCES_DIR, 'SOURCES.md')

def parse_source_file(filepath):
    data = {}
    current_key = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line_str = line.rstrip('\n')
            # Check for top-level key: value
            m = re.match(r'^([a-zA-Z0-9_]+):\s*(.*)$', line_str)
            if m:
                current_key = m.group(1)
                data[current_key] = m.group(2).strip(' "')
            elif current_key and line_str.startswith('  '):
                data[current_key] += ' ' + line_str.strip(' "')
    return data

def main():
    source_files = sorted(glob.glob(os.path.join(SOURCES_DIR, '[LS]-*.md')))
    if not source_files:
        raise FileNotFoundError(f"No source files found in {SOURCES_DIR}")

    rows = [
        "# Primary Source & Licence Register (ANANKE-001 / ANANKE-002)",
        "",
        "| ID | Status | URL Resolved | Clause / Heading | Controlling Language | Provenance & Operational Notes |",
        "|:---|:---:|:---|:---|:---:|:---|"
    ]

    for fpath in source_files:
        fid = os.path.splitext(os.path.basename(fpath))[0]
        meta = parse_source_file(fpath)

        status = meta.get('status', 'NOT_OPENED')
        url = meta.get('url_resolved', meta.get('url_requested', ''))
        clause = meta.get('clause_id', 'NOT_OPENED')
        lang = meta.get('legally_controlling_language', 'en')
        notes = meta.get('notes', '')

        rows.append(f"| **{fid}** | `{status}` | {url} | {clause} | `{lang}` | {notes} |")

    rows.append("")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(rows))

    print(f"Successfully generated {OUTPUT_FILE} from {len(source_files)} source files.")

if __name__ == '__main__':
    main()
