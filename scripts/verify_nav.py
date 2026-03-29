import os
import re
import pathlib

BASE = "D:/GIT/Tutorial"
DIRS = ['dotnet', 'javascript', 'architecture', 'distributed-systems', 'data',
        'web-services', 'azure', 'testing', 'devops']


def to_posix(rel):
    return str(pathlib.PurePosixPath(pathlib.PureWindowsPath(rel)))


def get_expected_nav(rel_path):
    parts = rel_path.split('/')
    depth = len(parts)
    if parts[-1] == 'index.md':
        return None
    if rel_path.startswith('azure/lectures/'):
        return '[<<](../index.md) | [home](../../README.md)'
    if rel_path == 'devops/os/virtual-memory.md':
        return '[<<](../index.md) | [home](../../README.md)'
    if rel_path.startswith('azure/lctrs/') or rel_path.startswith('azure/learn/') or rel_path.startswith('azure/pages/'):
        return None
    if depth == 4:
        return '[<<](./index.md) | [home](../../../README.md)'
    if depth == 3:
        return '[<<](./index.md) | [home](../../README.md)'
    if depth == 2:
        return '[<<](./index.md) | [home](../README.md)'
    return None


no_nav = []
multiple_nav = []
wrong_nav = []
ok_files = []

for d in DIRS:
    dir_path = os.path.join(BASE, d)
    for root, dirs, files in os.walk(dir_path):
        dirs.sort()
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            rel_path = to_posix(os.path.relpath(filepath, BASE))

            expected = get_expected_nav(rel_path)
            if expected is None:
                continue

            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()

            nav_lines = [l.strip() for l in lines if '[<<]' in l or '[home]' in l]
            nav_lines = [l for l in nav_lines if not re.match(r'^\[\d+\]:', l)]

            if len(nav_lines) == 0:
                no_nav.append(rel_path)
            elif len(nav_lines) > 1:
                multiple_nav.append((rel_path, nav_lines))
            elif nav_lines[0] != expected:
                wrong_nav.append((rel_path, nav_lines[0], expected))
            else:
                ok_files.append(rel_path)

print(f"OK: {len(ok_files)}")
print(f"No nav: {len(no_nav)}")
print(f"Multiple nav: {len(multiple_nav)}")
print(f"Wrong nav: {len(wrong_nav)}")
print()
if no_nav:
    print("NO NAV FILES:")
    for f in no_nav:
        print(f"  {f}")
if multiple_nav:
    print("MULTIPLE NAV FILES:")
    for f, navs in multiple_nav:
        print(f"  {f}")
        for n in navs:
            print(f"    {n}")
if wrong_nav:
    print("WRONG NAV FILES:")
    for f, got, exp in wrong_nav:
        print(f"  {f}")
        print(f"    got: {got}")
        print(f"    exp: {exp}")
