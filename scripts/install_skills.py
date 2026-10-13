#!/usr/bin/env python3
"""Install the complete pstack skill bundle without replacing existing skills."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def manifest(path):
    if path.is_symlink() or any(p.is_symlink() for p in path.rglob('*')):
        raise ValueError(f'Refusing symlink skill: {path}')
    return {str(p.relative_to(path)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in path.rglob('*') if p.is_file()}


def install(destination):
    registry = json.loads((ROOT / 'entrypoints.json').read_text())
    names = [registry['core']] + [entry['skill'] for entry in registry['entries']]
    if len(names) != len(set(names)) or any(not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', name) for name in names):
        raise ValueError('Invalid duplicate/path skill name')
    pending = []
    for name in names:
        source = ROOT / 'skills' / name
        if not (source / 'SKILL.md').is_file():
            raise ValueError(f'Missing bundle skill: {name}')
        manifest(source)
        target = destination / name
        if target.exists() or target.is_symlink():
            if target.is_dir() and manifest(source) == manifest(target):
                continue
            raise FileExistsError(f'{target} differs. Back up and review the existing skill; nothing installed.')
        if destination.resolve() == (Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills').resolve():
            other = Path.home() / '.agents/skills' / name
            if other.exists() or other.is_symlink():
                raise FileExistsError(f'Existing cross-runtime skill {other}; refusing a competing {name} entry.')
        pending.append((source, target))
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    with tempfile.TemporaryDirectory(prefix='.pstack-stage-', dir=destination.parent) as temp:
        stage = Path(temp)
        for source, target in pending:
            candidate = stage / target.name
            shutil.copytree(source, candidate)
            if manifest(source) != manifest(candidate):
                raise ValueError(f'Staging mismatch: {target.name}')
        try:
            for source, target in pending:
                if target.exists() or target.is_symlink():
                    raise FileExistsError(f'Target appeared during staging: {target}')
                os.rename(stage / target.name, target)
                created.append(target)
        except BaseException:
            for target in reversed(created):
                # Only remove this transaction's newly created, unchanged tree.
                source = ROOT / 'skills' / target.name
                if manifest(target) == manifest(source):
                    shutil.rmtree(target)
            raise
    print(f'Installed {len(created)} skills; {len(names) - len(created)} identical copies preserved at {destination}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills')
    args = parser.parse_args()
    install(args.dest)
