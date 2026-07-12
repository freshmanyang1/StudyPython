# 角色固定入口

本文件用于让 Claude Code、Codex 和其他 AI 不再通过 glob 或目录侦查猜测角色身份。收到角色调用时，先按本表读取固定入口，再读取任务文件。

## 固定入口表

| 用户称呼 | Skill 名称 | 固定入口 | 默认启动必读 |
|---|---|---|---|
| `项目经理` | `project-manager` | `.agents/skills/project-manager/SKILL.md` | `ai/TASK_BOARD.md`、`ai/TASK_LOCKS.md`、`ai/PM_DECISION_LIST.md` |
| `架构师` | `architect` | `.agents/skills/architect/SKILL.md` | `ai/TASK_BOARD.md`、`ai/TASK_LOCKS.md`、指定任务说明 |
| `后端` | `dev-backend` | `.agents/skills/dev-backend/SKILL.md` | `ai/TASK_BOARD.md`、`ai/TASK_LOCKS.md`、指定任务说明 |
| `前端` | `dev-frontend` | `.agents/skills/dev-frontend/SKILL.md` | `ai/TASK_BOARD.md`、`ai/TASK_LOCKS.md`、指定任务说明 |
| `测试` | `tester` | `.agents/skills/tester/SKILL.md` | `ai/TASK_BOARD.md`、待测任务说明、交接文件 |
| `审查` | `code-reviewer` | `.agents/skills/code-reviewer/SKILL.md` | `ai/TASK_BOARD.md`、待审任务说明、测试报告 / 交接文件 |
| `flow` | `flow` | `.agents/skills/flow/SKILL.md` | `ai/TASK_BOARD.md`、`ai/TASK_LOCKS.md`、`ai/PM_DECISION_LIST.md` |
| `aiskill` | `ai-collaboration-manager` | `.agents/skills/ai-collaboration-manager/SKILL.md` | `AGENTS.md`、相关协作资产、`.agents/skill-registry.md` |
| `prompt架构师` | `prompt-architect` | `.agents/skills/prompt-architect/SKILL.md` | `AGENTS.md`、`.agents/context/README.md`、相关现有实现或任务说明 |
| `python` | `python` | `.agents/skills/python/SKILL.md` | `python-course/COURSE_INDEX.md`、当前课程文件 |

## 使用规则

- 角色名加 `开始工作` 是自动化流程，不需要再询问是否开始。
- `切换 xxx 身份` 只切换身份、说明职责和边界，不自动领取任务；`xxx，开始工作` 才进入自动化流程。
- 角色 Skill 名称统一使用本表 `Skill 名称` 列；例如项目经理是 `project-manager`，禁止用 `project_manager` 或旧 PM 模式判断“没有项目经理 skill”。
- 启动任意角色后，必须遵守 `.agents/context/RUNTIME_RULES.md`。
- `审查` 可由 `flow` 在受控条件下推进；`aiskill` 默认不由 `flow` 推进，用户明确授权的协作机制顺序依赖链例外。`测试` 可由 `flow` 调度。
