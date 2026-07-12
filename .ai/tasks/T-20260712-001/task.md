# T-20260712-001 Initialize project AI collaboration runtime

## Source

- Source task: none
- Derivation depth: 0
- Source type: bootstrap initialization
- Follow-up/replacement: none
- Context summary: create or repair this project's AI collaboration runtime copy from $kitRoot.

## Module

- Module: collaboration mechanism
- Cross-module impact: no business module impact.

## Basic Info

| Field | Value |
|---|---|
| Owner | aiskill |
| Module | collaboration mechanism |
| Type | collaboration asset task |
| Priority | P1 |
| Dependency | none |
| Dependency gate | none |
| Target Git root | none: collaboration assets are in the project root |
| Allowed verification command | powershell -ExecutionPolicy Bypass -File C:\Users\13730\project-agent-kit\scripts\check.ps1 -ProjectRoot D:\Dev\StudyPython |

## Goals

1. Complete the project-level AGENTS.md, .agents/, i/, and .ai/tasks/ runtime copy.
2. Preserve existing project facts and task state.
3. Make the project-agent-kit read-only check pass.

## Allowed Scope

- $Root\AGENTS.md
- $Root\.agents\**
- $Root\ai\**
- $Root\.ai\tasks\T-20260712-001\**

## Forbidden Scope

- Do not modify business code.
- Do not run build/test/lint/format commands.
- Do not overwrite existing tasks, task locks, PM decisions, or archive state.
- Do not write project runtime state back to $kitRoot.

## Acceptance Criteria

1. Every role skill referenced by .agents/ROLE_ENTRYPOINTS.md exists.
2. i/TASK_FLOW_RULES.md and i/HANDOFF_PROTOCOL.md exist.
3. The initialization task has 	ask.md, handoff.md, and an archive index entry.
4. check.ps1 -ProjectRoot returns PASS.