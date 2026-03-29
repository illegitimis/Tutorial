import os
import re

BASE = "D:/GIT/Tutorial"


def get_correct_nav(rel_path):
    """Return the correct navigation string for a file based on its relative path."""
    parts = rel_path.split('/')
    depth = len(parts)  # 2 = top-level file, 3 = one subdir, 4 = two subdirs

    # Skip index.md files
    if parts[-1] == 'index.md':
        return None

    # azure/lectures/ depth 3 - already has correct nav
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
    """Check if a line is a navigation line that should be replaced."""
    line = line.strip()
    has_back = '[<<]' in line
    has_home = '[home]' in line
    return has_back or has_home


def update_file(filepath, rel_path):
    correct_nav = get_correct_nav(rel_path)
    if correct_nav is None:
        return 'skip'

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        lines = content.splitlines(keepends=True)

    # Check if already correct - look in last few lines
    last_lines = [l.strip() for l in lines[-5:] if l.strip()]
    for ll in last_lines:
        if ll == correct_nav:
            return 'already_correct'

    new_lines = list(lines)

    # Find nav lines at the end to replace
    nav_indices = []
    for i in range(len(new_lines) - 1, max(len(new_lines) - 15, -1), -1):
        line = new_lines[i].strip()
        if line == '':
            continue
        if is_nav_line(line):
            nav_indices.append(i)
        else:
            break

    if nav_indices:
        nav_indices.sort()
        first_nav = nav_indices[0]

        before = new_lines[:first_nav]
        # Remove trailing empty lines before nav
        while before and before[-1].strip() == '':
            before.pop()

        new_content = ''.join(before) + '\n\n' + correct_nav + '\n'
    else:
        # No nav found, add at end
        new_content = content.rstrip('\n\r') + '\n\n' + correct_nav + '\n'

    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)

    if nav_indices:
        return 'updated'
    else:
        return 'added'


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
            rel_path = os.path.relpath(filepath, BASE).replace('\\', '/')
            result = update_file(filepath, rel_path)
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
print("=== SKIPPED ===")
for f in skipped_files:
    print(f)
