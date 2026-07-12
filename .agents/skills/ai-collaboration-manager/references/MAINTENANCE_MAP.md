# aiskill 协作资产维护路标

aiskill 维护协作资产时按本表定位「主题 → 唯一正文」，不再 glob 猜文件。本文件只放对照表和路径指针，不复制任何已有规则正文；正文以表中所指文件为准。

## 启动链

| 顺序 | 文件 | 用途 |
|---|---|---|
| 1 | `.agents/ROLE_ENTRYPOINTS.md` | 身份入口、aiskill 必读列表 |
| 2 | `.agents/skills/ai-collaboration-manager/SKILL.md` | 闸门、可做/不可做、输出模板 |
| 3 | `AGENTS.md` | 入口硬规则 + 单一事实来源指针表 |
| 4 | `.agents/context/README.md` | 全库「主题 → 唯一正文」索引 |

改协作资产前：用户要求出补丁 → 先建 Owner=`aiskill` 最小任务（用 `references/minimal-task-template.md`）→ 改文件 → 自检 → 直接 `DONE` 归档；纯分析或评审不出补丁不建任务。

## 主题 → 维护文件

| 要维护的内容 | 唯一/主维护位置 | 不要重复写到 |
|---|---|---|
| 项目入口、三仓+PAR、无任务 ID 不改代码 | `AGENTS.md` | `.agents/skill-usage.md`、各 SKILL 长段流程 |
| 四步协作法、精准修改、机械/结构性分级 | `.agents/context/COLLABORATION_METHOD.md` | `AGENTS.md` 正文 |
| Tunnel 命名与敏感边界 | 启用 Tunnel profile 时为 `.agents/context/TUNNEL_RULES.md` | `AGENTS.md` 长段 |
| Runtime 防空转、UTF-8 读中文 | `.agents/context/RUNTIME_RULES.md` | 各角色 SKILL |
| 协作资产盘点和用户级母版提取边界 | `.agents/context/COLLABORATION_ASSET_INVENTORY.md` | `AGENTS.md`、任务板、各角色 Skill |
| 任务状态、flow、测试/审查分流、PM 决策、依赖门禁 | `ai/TASK_FLOW_RULES.md` | `ai/TASK_BOARD.md` 长流程、`.agents/skill-usage.md` |
| AI 协作交付流水线 v1 试运行路径 | `ai/AI_DELIVERY_PIPELINE_V1_TRIAL.md` | 各角色 Skill 长段复制；未验证前不要写入正式状态机 |
| AI 任务系统 v2 草案 | `ai/AI_TASK_SYSTEM_V2_DRAFT.md` | `TASK_BOARD.md` 结构、各角色 Skill、flow 规则；草案验证前不要拆散 |
| 任务索引、状态表、任务模板字段 | `ai/TASK_BOARD.md` | 不要复制完整流转说明 |
| 交接模板（完整/轻量/测试/审查/BLOCKED） | `ai/HANDOFF_PROTOCOL.md` | 各 SKILL 里另写一套模板 |
| 角色触发语、启动必读 | `.agents/ROLE_ENTRYPOINTS.md` | `.agents/skill-usage.md`（仅兼容跳转） |
| 角色「可以做/不可以做」正文 | `.agents/skills/<角色>/SKILL.md` | `ai/ROLE_REGISTRY.md` |
| 角色属性表、路径 Owner 映射、跨角色硬约束 | `ai/ROLE_REGISTRY.md` | 不要恢复各角色长段职责 |
| 模块定义、PAR 模块说明、建议优先级 | `ai/TASK_MODULES.md` | — |
| Skill 注册、14 天评估 | `.agents/skill-registry.md` | — |
| Skill 增删改生命周期 | `.agents/skills/ai-collaboration-manager/references/lifecycle.md` | — |
| aiskill 最小任务样板 | `.agents/skills/ai-collaboration-manager/references/minimal-task-template.md` | — |
| 维护路标（本文件） | `.agents/skills/ai-collaboration-manager/references/MAINTENANCE_MAP.md` | 不要写进 `AGENTS.md`、`ROLE_REGISTRY.md`、`skill-usage.md` |
| Cursor 入口指针 | `.cursor/rules/agents.mdc` | 不复制长规则 |
| PAR 工作区边界 | `AGENTS.md`、`ai/TASK_MODULES.md` | — |

## 已知仍剩问题 → 维护点

复检剩余项的修改去处。改动前必须先建 Owner=`aiskill` 最小任务，再补丁。

| 剩余项 | 应维护的文件 |
|---|---|
| 临时修复合并测试+审查（如未来要松绑） | `ai/TASK_FLOW_RULES.md`、`ai/TASK_BOARD.md` 临时修复段、`ai/HANDOFF_PROTOCOL.md` |
| 任务锁心跳工具化 | `ai/TASK_LOCKS.md`（规则段）；工具化属环境侧，需用户拍板 |
| 架构师边界继续收紧 | `.agents/skills/architect/SKILL.md` |
| 历史 handoff 缺 `下一步处理身份` | 各 `.ai/tasks/<旧任务>/handoff.md`；建议按任务级最小补丁，不批量改写 |
| 模块建议优先级更新 | `ai/TASK_MODULES.md` 「当前模块优先级」段 |
| `.agents/context/README.md` L3 表述过时 | `.agents/context/README.md` |

## 自检三步

1. **改前**：在 `AGENTS.md` 「规则单一事实来源」段和 `.agents/context/README.md` 「当前事实来源」表里确认主题归属。
2. **改时**：同一规则只改一处正文；其它文件只加一行指针，不复制段落。
3. **改后**：用 `rg` 搜关键词（例如 `阻断承接`、`依赖门禁`、`PM_REVIEW` 子类型），看是否出现两处以上相同长段落；有则合并到唯一正文，其余改为指针。

## 维护本文件本身

本表内容变化时（新增主题、文件迁移、归属调整），按 aiskill 流程建任务后直接更新本文件；不在其它文件复制本表。
