# 项目协作笔记

共享上下文索引见 `.agents/context/README.md`。Codex、Claude Code、Cursor 都应以本文件为项目总入口，再按共享上下文索引读取角色、Runtime 和任务流规则。

## 项目占位

- 项目名称：`StudyPython`
- 项目根目录：`D:\Dev\StudyPython`
- 主开发 Git 根目录：`D:\Dev\StudyPython`
- 项目类型：`unspecified`

## 中文与编码安全要求

- 中文统一使用简体中文，禁止新增繁体中文。
- 修改含中文文件时必须保持原编码，禁止因工具或终端编码导致乱码。
- 禁止从乱码终端输出中复制中文再写回文件。
- 含中文修改只做最小补丁；如发现乱码、繁体或编码异常，先停止并询问用户。

## 规则单一事实来源

- 本文件只保留项目入口、硬规则指针、工作区边界和事实来源指针。
- 用户级 AI 协作母版位于 `C:\Users\13730\project-agent-kit`；母版只提供通用角色模板和初始化模板，当前项目仍以本文件、`.agents/**`、`ai/**` 和 `.ai/tasks/**` 作为运行副本。
- Codex 自然调用 Cursor / Claude Code 的规则见 `.agents/context/AGENT_CALLS.md`；外部 Agent 是 Codex 调用的能力，不是项目事实源。
- 任务状态、依赖、归档、派生、测试、最终审查、PM 决策和 flow 状态灯的唯一正文是 `ai/TASK_FLOW_RULES.md`。
- 角色职责边界的唯一正文是各角色 `.agents/skills/**/SKILL.md`。
- 角色启动入口和常用触发语统一维护在 `.agents/ROLE_ENTRYPOINTS.md`。
- `ai/TASK_BOARD.md` 只保留当前任务索引、状态表和任务模板，不承载完整流程说明。

## 通用修改硬规则

- 没有任务 ID，不允许修改代码。所有任务必须登记在 `ai/TASK_BOARD.md`。
- 没有任务条目指定的 `task.md`，执行角色不允许修改代码。
- 默认不运行 build/test/lint/格式化命令，除非用户明确要求。
- 只做最小补丁，不修改无关文件，不回滚未确认来源的已有改动。
- 禁止全文件重写、自动格式化、批量替换导致无关 diff。
- 禁止批量删除文件或目录，不得使用递归删除命令。

## 工作区边界

项目事实由初始化时填写，不从母版继承其它项目路径。

| 路径 | 用途 | 默认权限 |
|---|---|---|
| `D:\Dev\StudyPython` | 主开发仓 | 按任务说明修改 |
| `none` | 参考仓或素材目录 | 默认只读 |

## AI 协作规则

- 所有 AI 对话和角色执行必须遵守 `.agents/context/RUNTIME_RULES.md`。
- 任务流转、归档、派生、测试与最终审查分流和 flow 状态灯规则见 `ai/TASK_FLOW_RULES.md`。
- 多个 flow 并行时，任务占用见 `ai/TASK_LOCKS.md`。
- `ai/TASK_BOARD.md` 只保留非 `DONE` 当前任务；`DONE` 任务归档到 `ai/TASK_ARCHIVE.md`。
- 任务模块定义见 `ai/TASK_MODULES.md`；当前任务必须填写 `模块` 字段。
- 角色固定入口见 `.agents/ROLE_ENTRYPOINTS.md`。
- 角色之间交接格式见 `ai/HANDOFF_PROTOCOL.md`。

## Skill 管理

- Skill 的添加、修改、删除、评估由 `aiskill` 负责。
- Skill 注册表见 `.agents/skill-registry.md`。
- 第三方 skill 默认先评估，不得直接安装或批量启用。
