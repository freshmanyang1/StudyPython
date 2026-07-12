# AI 共享上下文入口

本目录承载 Codex、Claude Code、Cursor 共同读取的项目级 AI 协作上下文。规则正文按「主题 → 唯一事实来源」分布到本目录文件与各角色 `SKILL.md`；入口文件只保留指针，不复制长正文。

## 三方入口

| 工具 | 固定入口 | 说明 |
|---|---|---|
| Codex | `AGENTS.md` | 根目录 `AGENTS.md` 是 Codex 和通用 AI 的第一入口。 |
| Claude Code | `CLAUDE.md` | `CLAUDE.md` 使用 `@AGENTS.md` 导入共享规则。 |
| Cursor | `.cursor/rules/agents.mdc` | Cursor 项目规则指向 `AGENTS.md` 和本文件。 |

## 当前事实来源

| 主题 | 文件 |
|---|---|
| 项目入口、编码、工作区边界、硬规则指针 | `AGENTS.md` |
| 用户级 AI 协作母版 | `C:\Users\13730\project-agent-kit`；项目运行副本仍以当前项目文件为准 |
| 四步协作法、精准修改、自检验证 | `.agents/context/COLLABORATION_METHOD.md` |
| Runtime 防空转、THINK / ACT / VERIFY | `.agents/context/RUNTIME_RULES.md` |
| Codex 自然调用 Cursor / Claude Code | `.agents/context/AGENT_CALLS.md` |
| LLM Wiki 读取规则和 API 协议 | `.agents/context/LLM_WIKI.md` |
| 协作资产盘点和用户级母版提取边界 | `.agents/context/COLLABORATION_ASSET_INVENTORY.md` |
| 角色固定入口和常用触发语 | `.agents/ROLE_ENTRYPOINTS.md` |
| 角色职责边界正文 | `.agents/skills/**/SKILL.md` |
| 角色属性、路径映射和跨角色硬约束 | `ai/ROLE_REGISTRY.md` |
| 任务状态、归档、派生、flow 状态灯 | `ai/TASK_FLOW_RULES.md` |
| 任务占用和并发锁 | `ai/TASK_LOCKS.md` |
| 任务模块 | `ai/TASK_MODULES.md` |
| 交接格式 | `ai/HANDOFF_PROTOCOL.md` |
| Skill 注册和采用策略 | `.agents/skill-registry.md` |

## 启动顺序

1. 先读根目录 `AGENTS.md`。
2. 再读本文件确认共享上下文索引。
3. 按 `.agents/ROLE_ENTRYPOINTS.md` 定位角色 Skill。
4. 按 `.agents/context/RUNTIME_RULES.md` 控制 THINK / ACT / VERIFY。
5. 涉及任务时读取 `ai/TASK_BOARD.md`、任务说明和交接文件。
