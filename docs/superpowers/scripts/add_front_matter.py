#!/usr/bin/env python3
"""Add Just The Docs front matter to all content .md files.

Usage:
    python add_front_matter.py --dry-run   # Preview changes
    python add_front_matter.py             # Apply changes
"""

import argparse
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(subprocess.check_output(
    ['git', 'rev-parse', '--show-toplevel'], text=True
).strip())

UNTOUCHED_FILES = {'CLAUDE.md'}
UNTOUCHED_DIRS = {'docs/superpowers'}

EXCLUDED_ROOT_FILES = {
    'README.md', 'CONTRIBUTING.md', 'CONTRIBUTORS.md',
    'STRUCTURE.md', 'CHANGELOG.md', 'bs-front-matter.md'
}

ROOT_NAV_ORDER = {
    '.NET': 1, 'Architecture': 2, 'Data': 3, 'Web Services': 4,
    'Azure': 5, 'Distributed Systems': 6, 'Testing': 7,
    'JavaScript': 8, 'DevOps': 9
}

DEFAULT_DATE = '2026-03-30 00:00:00 +00:00'

# JTD supports max 3 navigation levels. Directories at depth 3+
# have their files flattened as children of the depth-2 ancestor.
MAX_NAV_DEPTH = 3


def get_git_dates():
    """Run one bulk git log; return {relative_path: 'YYYY-MM-DD HH:MM:SS +00:00'}.

    Parses git log --format=COMMIT_DATE:<iso-date> --name-only output.
    Keeps only the first (most recent) date per file since git log is newest-first.
    """
    result = subprocess.run(
        ['git', 'log', '--format=COMMIT_DATE:%aI', '--name-only', '--diff-filter=ACDMRT'],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    dates = {}
    current_date = None
    for line in result.stdout.splitlines():
        if line.startswith('COMMIT_DATE:'):
            iso_str = line[len('COMMIT_DATE:'):]
            dt = datetime.fromisoformat(iso_str).astimezone(timezone.utc)
            current_date = dt.strftime('%Y-%m-%d %H:%M:%S') + ' +00:00'
        elif line.strip() and current_date:
            rel_path = line.strip().replace('\\', '/')
            if rel_path not in dates:
                dates[rel_path] = current_date
    return dates


def classify_file(rel_path):
    """Return 'untouched', 'excluded', or 'jtd'."""
    norm = rel_path.replace('\\', '/')
    parts = norm.split('/')
    filename = parts[-1]

    if len(parts) == 1 and filename in UNTOUCHED_FILES:
        return 'untouched'

    for d in UNTOUCHED_DIRS:
        if norm.startswith(d + '/'):
            return 'untouched'

    if len(parts) == 1 and filename in EXCLUDED_ROOT_FILES:
        return 'excluded'

    return 'jtd'


def extract_title(file_path):
    """Extract H1 heading from file content. Falls back to filename stem."""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^#\s+(.+)$', line.strip())
            if m:
                return m.group(1).strip()
    return file_path.stem.replace('-', ' ').title()


def build_hierarchy(md_files):
    """Build hierarchy info for each JTD file.

    Returns {rel_path: {parent, grand_parent, has_children, depth, nav_parent_dir}}.
    nav_parent_dir is the directory whose index.md serves as this file's JTD parent.
    """
    # Step 1: map directory -> index.md title
    dir_titles = {}
    for rel_path in md_files:
        p = Path(rel_path)
        if p.name == 'index.md' and classify_file(rel_path) == 'jtd':
            d = str(p.parent).replace('\\', '/')
            if d == '.':
                d = ''
            dir_titles[d] = extract_title(REPO_ROOT / rel_path)

    # Step 2: determine hierarchy for each file
    hierarchy = {}
    for rel_path in md_files:
        norm = rel_path.replace('\\', '/')
        if classify_file(norm) != 'jtd':
            continue

        p = Path(norm)
        file_dir = str(p.parent).replace('\\', '/')
        if file_dir == '.':
            file_dir = ''
        depth = len(Path(file_dir).parts) if file_dir else 0

        # Root index.md
        if norm == 'index.md':
            hierarchy[norm] = {
                'parent': None, 'grand_parent': None,
                'has_children': True, 'depth': 0, 'nav_parent_dir': None
            }
            continue

        is_index = p.name == 'index.md'

        if is_index:
            # Index files: JTD parent is the parent directory's index
            parent_dir = str(Path(file_dir).parent).replace('\\', '/')
            if parent_dir == '.':
                parent_dir = ''
            parent_title = dir_titles.get(parent_dir) if parent_dir else None

            # grand_parent: only if parent_dir itself has a parent with an index
            grand_parent_title = None
            if parent_dir:
                gp_dir = str(Path(parent_dir).parent).replace('\\', '/')
                if gp_dir == '.':
                    gp_dir = ''
                gp_title = dir_titles.get(gp_dir)
                # Only set grand_parent if the grandparent is NOT the root index
                # (root-level pages have no parent in JTD nav)
                if gp_title and gp_dir:
                    grand_parent_title = gp_title

            # Depth-3+ index files: flatten — no has_children
            if depth >= MAX_NAV_DEPTH:
                hierarchy[norm] = {
                    'parent': parent_title, 'grand_parent': grand_parent_title,
                    'has_children': False, 'depth': depth,
                    'nav_parent_dir': parent_dir
                }
                continue

            # Check if this index has children (other .md files in same dir or subdirs)
            has_kids = False
            for other in md_files:
                other_norm = other.replace('\\', '/')
                if other_norm == norm:
                    continue
                if classify_file(other_norm) != 'jtd':
                    continue
                other_dir = str(Path(other_norm).parent).replace('\\', '/')
                if other_dir == file_dir or other_dir.startswith(file_dir + '/'):
                    has_kids = True
                    break

            hierarchy[norm] = {
                'parent': parent_title, 'grand_parent': grand_parent_title,
                'has_children': has_kids, 'depth': depth,
                'nav_parent_dir': parent_dir
            }
        else:
            # Leaf files: parent is the index.md in their directory
            # or nearest ancestor directory with an index.md
            if file_dir in dir_titles:
                nav_parent_dir = file_dir
            else:
                # No index.md here — walk up to find nearest ancestor
                nav_parent_dir = str(Path(file_dir).parent).replace('\\', '/')
                if nav_parent_dir == '.':
                    nav_parent_dir = ''

            parent_title = dir_titles.get(nav_parent_dir)

            # grand_parent
            grand_parent_title = None
            if nav_parent_dir:
                gp_dir = str(Path(nav_parent_dir).parent).replace('\\', '/')
                if gp_dir == '.':
                    gp_dir = ''
                gp_title = dir_titles.get(gp_dir)
                if gp_title and gp_dir:
                    grand_parent_title = gp_title

            # Depth-3+ leaf files: flatten under depth-2 ancestor
            if depth >= MAX_NAV_DEPTH:
                # Walk up to find the depth-2 ancestor
                ancestor_dir = file_dir
                while len(Path(ancestor_dir).parts) >= MAX_NAV_DEPTH:
                    ancestor_dir = str(Path(ancestor_dir).parent).replace('\\', '/')
                    if ancestor_dir == '.':
                        ancestor_dir = ''
                parent_title = dir_titles.get(ancestor_dir)
                gp_dir = str(Path(ancestor_dir).parent).replace('\\', '/')
                if gp_dir == '.':
                    gp_dir = ''
                grand_parent_title = dir_titles.get(gp_dir) if gp_dir else None
                nav_parent_dir = ancestor_dir

            hierarchy[norm] = {
                'parent': parent_title, 'grand_parent': grand_parent_title,
                'has_children': False, 'depth': depth,
                'nav_parent_dir': nav_parent_dir
            }

    return hierarchy


def compute_nav_order(md_files, hierarchy):
    """Compute nav_order for each JTD file.

    Root index = 1. Category indices use ROOT_NAV_ORDER.
    All other files: grouped by nav_parent_dir, sorted alphabetically by title, numbered from 1.
    """
    nav_orders = {'index.md': 1}

    # Category index files (depth-1 index.md) use ROOT_NAV_ORDER
    for rel_path in md_files:
        norm = rel_path.replace('\\', '/')
        if norm not in hierarchy:
            continue
        info = hierarchy[norm]
        if info['depth'] == 1 and Path(norm).name == 'index.md':
            title = extract_title(REPO_ROOT / rel_path)
            nav_orders[norm] = ROOT_NAV_ORDER.get(title, 99)

    # All other files: group by nav_parent_dir, sort by title
    groups = {}
    for rel_path in md_files:
        norm = rel_path.replace('\\', '/')
        if norm in nav_orders or norm not in hierarchy:
            continue
        info = hierarchy[norm]
        key = info.get('nav_parent_dir', '')
        if key not in groups:
            groups[key] = []
        title = extract_title(REPO_ROOT / rel_path)
        groups[key].append((title.lower(), title, norm))

    for key, items in groups.items():
        items.sort()
        for i, (_, title, path) in enumerate(items, start=1):
            nav_orders[path] = i

    return nav_orders


def yaml_value(s):
    """Quote a YAML string value if it contains special characters."""
    if any(c in s for c in "':{}[]|>&*!?,#"):
        return f'"{s}"'
    return s


def generate_front_matter(rel_path, hierarchy, nav_orders, git_dates):
    """Generate YAML front matter string for a file."""
    norm = rel_path.replace('\\', '/')
    classification = classify_file(norm)

    if classification == 'excluded':
        return '---\nnav_exclude: true\nsearch_exclude: true\n---\n\n'

    if classification != 'jtd':
        return ''

    info = hierarchy.get(norm, {})
    title = extract_title(REPO_ROOT / rel_path)
    date = git_dates.get(norm, DEFAULT_DATE)
    nav_order = nav_orders.get(norm, 1)

    lines = ['---']
    lines.append(f'title: {yaml_value(title)}')

    if norm == 'index.md':
        lines.append('layout: home')
    elif Path(norm).name == 'index.md':
        lines.append('layout: minimal')
    else:
        lines.append('layout: default')

    lines.append(f'nav_order: {nav_order}')

    if norm == 'index.md':
        lines.append('description: "Dev documentation, tutorial, memory pointers, inverse oblivion"')
        lines.append('permalink: /')

    if info.get('has_children'):
        lines.append('has_children: true')
    if info.get('parent'):
        lines.append(f'parent: {yaml_value(info["parent"])}')
    if info.get('grand_parent'):
        lines.append(f'grand_parent: {yaml_value(info["grand_parent"])}')

    lines.append(f'last_modified_date: {date}')
    lines.append('---')
    lines.append('')

    return '\n'.join(lines) + '\n'


def fix_backlinks(content, rel_path):
    """Replace old backlink patterns with new standardized format.

    New format:
    - Leaf files: [<](./index.md) | [<<](/index.md)
    - Subcategory+ index files: [<](../index.md) | [<<](/index.md)
    - Category index files (depth 1): [<<](/index.md) only
    - Root index.md: no backlinks
    - Files in dirs without index.md: [<](../index.md) | [<<](/index.md)
    """
    norm = rel_path.replace('\\', '/')
    if classify_file(norm) != 'jtd' or norm == 'index.md':
        return content

    p = Path(norm)
    file_dir = str(p.parent).replace('\\', '/')
    if file_dir == '.':
        file_dir = ''
    is_index = p.name == 'index.md'
    depth = len(Path(file_dir).parts) if file_dir else 0

    if is_index and depth == 1:
        new_backlink = '[<<](/index.md)'
    elif is_index:
        new_backlink = '[<](../index.md) | [<<](/index.md)'
    else:
        has_local_index = (REPO_ROOT / file_dir / 'index.md').exists() if file_dir else False
        if has_local_index:
            new_backlink = '[<](./index.md) | [<<](/index.md)'
        else:
            new_backlink = '[<](../index.md) | [<<](/index.md)'

    # Match: [<<](path) | [home](path)  or  [<<](path) | [<<](path)
    pattern = r'\[<<?\]\([^)]+\)\s*\|\s*\[(?:home|<<?)\]\([^)]+\)'
    new_content = re.sub(pattern, new_backlink, content)

    return new_content


def main():
    parser = argparse.ArgumentParser(description='Add JTD front matter to .md files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without modifying files')
    args = parser.parse_args()

    print('Caching git dates...')
    git_dates = get_git_dates()
    print(f'  Cached dates for {len(git_dates)} files')

    # Collect all .md files
    md_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                full = Path(root) / f
                rel = str(full.relative_to(REPO_ROOT)).replace('\\', '/')
                md_files.append(rel)

    print(f'Found {len(md_files)} .md files')

    hierarchy = build_hierarchy(md_files)
    nav_orders = compute_nav_order(md_files, hierarchy)

    stats = {'untouched': 0, 'excluded': 0, 'jtd': 0, 'skipped_has_fm': 0}

    for rel_path in sorted(md_files):
        norm = rel_path.replace('\\', '/')
        classification = classify_file(norm)

        if classification == 'untouched':
            stats['untouched'] += 1
            continue

        file_path = REPO_ROOT / rel_path
        content = file_path.read_text(encoding='utf-8')

        # Skip files that already have front matter
        if content.startswith('---\n'):
            stats['skipped_has_fm'] += 1
            if args.dry_run:
                print(f'  SKIP (has FM): {norm}')
            continue

        fm = generate_front_matter(norm, hierarchy, nav_orders, git_dates)
        if not fm:
            continue

        new_content = fix_backlinks(content, norm)
        final = fm + new_content

        if args.dry_run:
            print(f'\n--- {norm} [{classification}] ---')
            print(fm.rstrip())
            if new_content != content:
                print('  [backlinks updated]')
        else:
            file_path.write_text(final, encoding='utf-8')
            print(f'  {classification}: {norm}')

        stats[classification] += 1

    print(f'\nSummary: untouched={stats["untouched"]}, excluded={stats["excluded"]}, '
          f'jtd={stats["jtd"]}, skipped(has FM)={stats["skipped_has_fm"]}')


if __name__ == '__main__':
    main()
