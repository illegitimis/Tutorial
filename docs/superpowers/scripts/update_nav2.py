import os
import re

BASE = "D:/GIT/Tutorial"


def get_correct_nav(rel_path):
    """Return the correct navigation string for a file based on its relative path."""
    parts = rel_path.split('/')
    depth = len(parts)

    # Skip index.md files
    if parts[-1] == 'index.md':
        return None

    # azure/lectures/ depth 3 - special nav
    if rel_path.startswith('azure/lectures/'):
        return '[<<](../index.md) | [home](../../README.md)'

    # devops/os/virtual-memory.md - no index in os/
    if rel_path == 'devops/os/virtual-memory.md':
        return '[<<](../index.md) | [home](../../README.md)'

    # Skip directories not in scope of the task
    if rel_path.startswith('azure/lctrs/'):
        return None
    if rel_path.startswith('azure/learn/'):
        return None
    if rel_path.startswith('azure/pages/'):
        return None

    # depth 4: e.g. data/nosql/mongo/articles.md
    if depth == 4:
        return '[<<](./index.md) | [home](../../../README.md)'

    # depth 3: e.g. dotnet/language/delegates.md, data/sql/acid.md
    if depth == 3:
        return '[<<](./index.md) | [home](../../README.md)'

    # depth 2: e.g. architecture/solid.md, testing/nunit.md
    if depth == 2:
        return '[<<](./index.md) | [home](../README.md)'

    return None


def is_nav_line(line):
    """Check if a line is a navigation line that should be removed/replaced."""
    stripped = line.strip()
    # Contains [<<] or [home] links (but not reference definitions like [1]: url)
    has_back = '[<<]' in stripped or '[<' in stripped
    has_home = '[home]' in stripped
    # Exclude pure reference link lines like [1]: http://...
    if re.match(r'^\[\d+\]:', stripped):
        return False
    # Only consider it a nav line if it has navigation-like content
    return has_back or has_home


def update_file(filepath, rel_path):
    correct_nav = get_correct_nav(rel_path)
    if correct_nav is None:
        return 'skip', None, None

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    original_lines = list(lines)

    # Find all nav lines in the file
    nav_line_indices = []
    for i, line in enumerate(lines):
        if is_nav_line(line):
            nav_line_indices.append(i)

    # Remove all nav lines (and adjacent empty lines that result from removal)
    # Build new lines without nav lines
    new_lines = []
    skip_next_empty = False
    for i, line in enumerate(lines):
        if i in nav_line_indices:
            # Skip this nav line; mark to potentially skip next empty line
            skip_next_empty = True
            continue
        if skip_next_empty and line.strip() == '':
            skip_next_empty = False
            # Skip one trailing empty line after nav removal
            continue
        skip_next_empty = False
        new_lines.append(line)

    # Now add the correct nav at the end
    # Strip trailing whitespace/newlines
    while new_lines and new_lines[-1].strip() == '':
        new_lines.pop()

    new_content = ''.join(new_lines) + '\n\n' + correct_nav + '\n'

    # Check if already correct (no change needed)
    if new_content == ''.join(original_lines):
        return 'already_correct', None, None

    # Check if just the nav was already correct (same as correct_nav at the end)
    # i.e., the only difference is nav lines replacement but result is same
    stripped_orig = ''.join(original_lines).rstrip('\n\r')
    stripped_new = new_content.rstrip('\n\r')

    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)

    was_added = len(nav_line_indices) == 0
    return 'added' if was_added else 'updated', nav_line_indices, correct_nav


# Process all relevant directories
DIRS = ['dotnet', 'javascript', 'architecture', 'distributed-systems', 'data',
        'web-services', 'azure', 'testing', 'devops']

stats = {'updated': 0, 'added': 0, 'already_correct': 0, 'skip': 0}
updated_files = []
added_files = []
correct_files = []
skipped_files = []

for d in DIRS:
    dir_path = os.path.join(BASE, d)
    for root, dirs, files in os.walk(dir_path):
        dirs.sort()
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            # Normalize path separators
            rel_path = os.path.relpath(filepath, BASE).replace('\\', '/')
            result, nav_indices, correct_nav = update_file(filepath, rel_path)
            stats[result] += 1
            if result == 'updated':
                updated_files.append(rel_path)
            elif result == 'added':
                added_files.append(rel_path)
            elif result == 'already_correct':
                correct_files.append(rel_path)
            elif result == 'skip':
                skipped_files.append(rel_path)

print("=== STATS ===")
print(f"Updated: {stats['updated']}")
print(f"Added:   {stats['added']}")
print(f"Already correct: {stats['already_correct']}")
print(f"Skipped: {stats['skip']}")
print()
print("=== UPDATED ===")
for f in updated_files:
    print(f)
print()
print("=== ADDED ===")
for f in added_files:
    print(f)
print()
print("=== ALREADY CORRECT ===")
for f in correct_files:
    print(f)
print()
print("=== SKIPPED (index.md and out-of-scope) ===")
for f in skipped_files:
    print(f)
