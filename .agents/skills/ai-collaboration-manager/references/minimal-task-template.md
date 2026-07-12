# aiskill 最小任务样板

aiskill 修改协作资产前使用本样板创建最小任务。纯分析、评审或不出补丁时不需要创建任务。

## 建立步骤

1. 先检查 `ai/TASK_BOARD.md`、`ai/TASK_ARCHIVE.md` 和 `.ai/tasks/`，确认任务 ID 全局唯一。
2. 创建 `.ai/tasks/<TaskId>/` 专属目录。
3. 在专属目录写入 `task.md`，内容使用下方样板。
4. 在专属目录写入初始 `handoff.md`；协作资产任务完成时可直接更新为轻量交接并归档。
5. 活跃执行时登记 `ai/TASK_BOARD.md`；完成后从任务板移除并写入 `ai/TASK_ARCHIVE.md`。
6. 禁止只新增任务板索引而不创建任务目录、`task.md` 和 `handoff.md`。

```markdown
# T-YYYYMMDD-NNN 任务标题

## 来源

- 来源任务：无 / T-YYYYMMDD-NNN
- 派生深度：0
- 来源类型：用户直接要求 / 规则一致性修复
- 承接/替代：
- 上下文摘要：

## 模块

- 所属模块：协作机制
- 跨模块影响：无业务模块影响。

## 基本信息

| 字段 | 值 |
|---|---|
| Owner | aiskill |
| 主执行 Agent | codex |
| 模块 | 协作机制 |
| 类型 | 协作资产任务 |
| 优先级 | P0 / P1 / P2 / P3 |
| 依赖 | 无 / T-YYYYMMDD-NNN |
| 依赖门禁 | DONE / CODE_READY |
| 目标 Git 根目录 | 无：协作资产位于工作区根目录 |
| 允许验证命令 | 仅静态验证 |

## 目标

1. 

## 允许范围

- 

## 禁止范围

- 不修改业务代码。
- 不运行 build/test/lint/格式化命令。

## 验收标准

1. 
```
