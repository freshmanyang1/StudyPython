# 任务面板

当前未归档开发任务的唯一入口。没有登记在这里的活跃任务，不允许修改代码；已 `DONE` 任务见 `ai/TASK_ARCHIVE.md`。

## 任务列表

### T-20260712-002 创建 pythonskill

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | aiskill |
| 主执行 Agent | claude |
| 模块 | 协作资产 |
| 类型 | 协作资产任务 |
| 优先级 | P1 |
| 依赖 | 无 |
| 依赖门禁 | 无 |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-002/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-002/handoff.md` |
| 有效代码行 | 0（协作资产） |

**目标摘要**：创建 pythonskill 的 SKILL.md，定义 Python 学习助手角色

**范围摘要**：创建 `.agents/skills/python/SKILL.md`，更新 skill-registry.md 和 ROLE_ENTRYPOINTS.md

**备注**：协作资产任务，已完成自检

### T-20260712-003 抓取网站课程整理大纲

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-002 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-003/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-003/handoff.md` |
| 有效代码行 | 60（课程文件） |

**目标摘要**：从廖雪峰和菜鸟教程抓取 Python 课程，整理成结构化大纲索引

**范围摘要**：创建 `python-course/` 目录结构、COURSE_INDEX.md、每个课程的 README.md、demo.py、homework.py

**备注**：已完成所有20个课程的文件创建

### T-20260712-004 更新 pythonskill 添加上传更新功能

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | aiskill |
| 主执行 Agent | claude |
| 模块 | 协作资产 |
| 类型 | 协作资产任务 |
| 优先级 | P1 |
| 依赖 | 无 |
| 依赖门禁 | 无 |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-004/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-004/handoff.md` |
| 有效代码行 | 0（协作资产） |

**目标摘要**：更新 pythonskill，添加"上传更新"功能，自动保存学习进度并推送到 GitHub

**范围摘要**：更新 `.agents/skills/python/SKILL.md`，添加触发语和执行流程

**备注**：协作资产任务，已完成自检

### T-20260712-005 更新 pythonskill 添加重新学习功能

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | aiskill |
| 主执行 Agent | claude |
| 模块 | 协作资产 |
| 类型 | 协作资产任务 |
| 优先级 | P1 |
| 依赖 | 无 |
| 依赖门禁 | 无 |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-005/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-005/handoff.md` |
| 有效代码行 | 0（协作资产） |

**目标摘要**：更新 pythonskill，添加"重新学习"功能，支持重新学习已完成的章节

**范围摘要**：更新 `.agents/skills/python/SKILL.md`，添加触发语、状态管理和打分逻辑

**备注**：协作资产任务，已完成自检

## 任务模板

```markdown
### T-YYYYMMDD-NNN 任务标题

| 字段 | 值 |
|---|---|
| 状态 | BACKLOG / PLANNED / ASSIGNED / IN_PROGRESS / CODE_READY / TESTING / TEST_FAILED / REVIEW_READY / REVIEWING / PM_REVIEW / FIX_REQUIRED / ACCEPTED / INTEGRATED / DONE / BLOCKED |
| Owner | 项目经理 / 后端工程师 / 前端工程师 / 测试 / 审查 / 架构师 / aiskill |
| 主执行 Agent | codex / cursor / claude / 其他：名称 |
| 模块 | 模块名 |
| 类型 | 完整任务 / 临时修复 / 协作资产任务 |
| 优先级 | P0 / P1 / P2 / P3 |
| 依赖 | 无 / T-YYYYMMDD-NNN |
| 依赖门禁 | CODE_READY / REVIEW_READY / DONE / 用户确认 |
| 目标 Git 根目录 | 仓库路径 / 无：原因 |
| 允许验证命令 | 命令 / 仅静态验证 |
| 任务说明 | `.ai/tasks/T-YYYYMMDD-NNN/task.md` |
| 交接文件 | `.ai/tasks/T-YYYYMMDD-NNN/handoff.md` |
| 有效代码行 | 待审查记录 |

**目标摘要**：

**范围摘要**：

**备注**：

暂无。
```
