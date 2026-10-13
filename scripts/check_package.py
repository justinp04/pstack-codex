#!/usr/bin/env python3
"""Check the public skill package, local links, and attribution without dependencies."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/pstack'
EXPECTED_PLAYBOOKS = {
    'authoring-a-skill', 'autonomous-run', 'autopilot-full', 'autopilot-stack',
    'babysit', 'bug-fix', 'eval', 'feature', 'hillclimb', 'investigation',
    'multi-phase-plan', 'opening-a-pr', 'orchestrate', 'pause-safely',
    'perf-issue', 'prototype', 'refactoring', 'runtime-forensics',
    'session-pickup', 'shipping', 'trace-forensics', 'visual-parity',
    'worktree-cleanup',
}


def check(root=ROOT):
    skill = root / 'skills/pstack'
    assert (skill / 'SKILL.md').is_file(), 'Missing installable entry point'
    assert len(list(skill.rglob('SKILL.md'))) == 1, 'Support guides must not register as skills'
    entry = (skill / 'SKILL.md').read_text()
    assert entry.startswith('---\n') and '\nname: pstack\n' in entry
    assert re.search(r'^description: \S', entry, re.M), 'Missing discovery description'
    playbooks = skill / 'references/workflows/poteto-mode/playbooks'
    assert {p.stem for p in playbooks.glob('*.md')} == EXPECTED_PLAYBOOKS, 'Missing/extra playbook category'
    assert len(list((skill / 'references/workflows').glob('*/guide.md'))) == 52, 'Missing upstream guide'
    license_text = (root / 'LICENSE').read_text()
    assert 'Copyright (c) 2026 Lauren Tan' in license_text and 'MIT License' in license_text
    assert license_text == (skill / 'LICENSE').read_text(), 'Installed skill license differs'
    assert 'Lauren Tan' in (root / 'README.md').read_text()
    assert (root / 'ATTRIBUTION.md').is_file() and (root / 'UPSTREAM.json').is_file()
    for file in root.rglob('*.md'):
        if '.git' in file.parts or 'node_modules' in file.parts:
            continue
        content = file.read_text()
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
            if re.match(r'https?://|#|mailto:', target) or '<' in target or target == 'url':
                continue
            resolved = (file.parent / target.split('#')[0]).resolve()
            assert resolved.is_relative_to(root.resolve()), f'Link escapes package: {file}: {target}'
            assert resolved.exists(), f'Broken link: {file}: {target}'
    assert not any(p.is_symlink() for p in skill.rglob('*')), 'Unexpected skill symlink'
    print('PASS: one installable skill, 52 guides, 23 playbooks, local links and Lauren Tan/MIT attribution')


if __name__ == '__main__':
    check()
