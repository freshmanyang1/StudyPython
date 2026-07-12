# Agent 调用说明

本文件定义 Codex 自然调用外部 Agent 的通用语义。外部 Agent 是 Codex 可调用的能力，不是项目任务状态事实源。

## 总控原则

- Codex 是项目总控和任务事实源；项目事实仍以本地 `AGENTS.md`、`.agents/**`、`ai/**`、`.ai/tasks/**` 为准。
- Cursor 和 Claude Code 只能接收 Codex 给出的任务包、上下文和边界；它们的输出必须回到 Codex，由 Codex 决定是否采纳。
- 外部 Agent 不得绕过 Codex 自行改任务状态、锁、PM 决策、归档或任务事实源。
- 用户自然提到 `Cursor`、`Claude Code`、`调用 Cursor`、`让 Claude Code 追问` 时，Codex 应识别为外部 Agent 调用意图。
- 用户话里只要出现 `Cursor`，且上下文包含任务、问题、文件、报错、需求、方案、修复或“去做/处理/解决/执行/看看/分析”等语义，默认就是把该事项交给 Cursor 解决；除非用户明确说“不要调用 Cursor”“只生成 prompt”“只讨论规则”。
- 用户话里只要出现 `Claude Code`，或在外部 Agent 语境下出现 `Claude`，默认就是把该事项交给 Claude Code 解决；除非用户明确说“不要调用 Claude Code”“只生成 prompt”“只讨论规则”。用户误写 `cladue` 且语义明显时，按 `claude` 处理。

## Agent 定位

| Agent | 定位 | 适合做什么 |
|---|---|---|
| Cursor | 外部执行型 Agent | 小补丁、局部实现、快速分析、按任务包执行。 |
| Claude Code | 外部理解型 Agent | 需求追问、复杂上下文理解、任务拆解草案、方案澄清、副审建议。 |

## 自然触发

| 用户说法 | Codex 应理解为 |
|---|---|
| 调用 Cursor 做一下 / 执行这个任务 | 使用 Cursor 执行模式，允许在任务包范围内改代码。 |
| 交给 Cursor / 给 Cursor / Cursor 去做 / 让 Cursor 做 / Cursor 处理 / Cursor | 默认使用 Cursor 执行模式；Codex 必须生成 prompt 并实际调用 Cursor CLI。 |
| 调用 Cursor 看一下 / 分析一下 | 使用 Cursor 只读分析模式，优先不改文件。 |
| 让 Cursor 以 flow 身份跑 | 使用 Cursor flow 模式，必须按任务流继续测试、审查和归档，或说明阻塞原因。 |
| 调用 Claude Code 追问 / 拆一下 / 分析一下 / 副审 | 使用 Claude Code 做澄清、拆解、方案建议、复杂分析或副审输入；Codex 必须生成 prompt 并实际调用 Claude Code CLI。 |
| 交给 Claude Code / 给 Claude / Claude 去做 / 让 Claude 看看 / Claude | 默认使用 Claude Code 调用；具体权限按任务包和当前模式决定。 |
| Claude DeepSeek / Claude DeepSeek 模型 / Claude deepseek | 使用 Claude Code，并切到 cc-switch 中名称匹配 DeepSeek 的 provider；模型未细分时使用该 provider 的默认模型。 |
| Claude MiMo / Claude mimo / Claude 小米 | 使用 Claude Code，并切到 cc-switch 中名称匹配 MiMo / Xiaomi MiMo 的 provider；模型未细分时使用该 provider 的默认模型。 |
| Claude <模型名> | 先按当前 provider 和 `cc-switch provider fetch-models` 匹配模型；找不到时列出可用 provider / 模型并问用户是否改用列表中的某个模型。 |

## Cursor 默认调用

Codex 调用 Cursor 执行任务时，默认使用本机 Cursor Agent CLI：

```powershell
& "$env:LOCALAPPDATA\cursor-agent\agent.cmd" -p "<任务包>" --workspace "<项目路径>" --model composer-2.5-fast --output-format text --trust --force
```

约定：

- 默认模型：`composer-2.5-fast`。
- 默认执行权限：`--trust --force`。
- Agent 模式是 CLI 默认模式，不写 `--mode=agent`。
- 只读分析可使用 `--mode=ask` 或在任务包中明确禁止写文件。
- 详细 CLI 速查仍以用户级文件 `C:\Users\13730\cursor-agent-call-guide.md` 为参考；母版只保存通用调用语义。
- `cursor-flow-prompt.md`、`cursor-prompt.md` 或回复中的 prompt 只是调用包，不是调用完成；生成 prompt 后必须继续执行 Cursor CLI，或明确报告为什么无法调用。

## Claude Code 默认调用

Codex 调用 Claude Code 时，默认使用本机 Claude Code CLI。Claude Code 没有 `--workspace` 参数；需要先切到目标项目目录再调用。

连通性测试或一次性只读问答：

```powershell
claude -p "<任务包>" --permission-mode dontAsk --tools=""
```

让 Claude Code 作为编码 agent 执行任务：

```powershell
claude -p "<任务包>" --permission-mode acceptEdits
```

最高权限执行仅用于可信目录和用户明确授权：

```powershell
claude -p "<任务包>" --dangerously-skip-permissions
```

约定：

- 用户只说 `claude` 或 `Claude Code`，不指定 provider / 模型时，使用当前默认 provider 和默认模型。
- 用户说 `claude deepseek` 时，先用 `cc-switch provider list` 找名称匹配 `DeepSeek` 的 provider，再用 `cc-switch use <provider-id>` 切换；没有继续指定 `flash` / `pro` 等模型时，使用该 provider 默认模型。
- 用户说 `claude mimo`、`claude xiaomi` 或 `claude 小米` 时，先用 `cc-switch provider list` 找名称匹配 `MiMo` / `Xiaomi MiMo` 的 provider，再用 `cc-switch use <provider-id>` 切换；没有继续指定 `pro` / `ultraspeed` 等模型时，使用该 provider 默认模型。
- 用户指定具体模型词时，先用 `cc-switch provider current` 和 `cc-switch provider fetch-models <provider-id>` 读取当前 provider 可用模型；若用户同时指定 provider，则先切 provider 再取模型列表。
- 找不到用户说的 provider 或模型时，必须把 `provider list` / `fetch-models` 查到的候选项列给用户，询问是否使用列表中的某个 provider / 模型；不能擅自猜一个近似模型继续。
- 默认不在母版写死 provider ID 或模型；调用前按 cc-switch 当前库读取当前可用项。
- 不复制 `C:\Users\13730\.claude\settings.json`、token、provider key 或 cc-switch 数据库内容。
- 只读澄清、需求追问、方案拆解和副审优先用 `--permission-mode dontAsk --tools=""`。
- 需要 Claude Code 实际改文件时才使用 `--permission-mode acceptEdits`，并必须给出明确允许范围和禁止范围。
- `claude-prompt.md`、`claude-code-prompt.md` 或回复中的 prompt 只是调用包，不是调用完成；生成 prompt 后必须继续执行 Claude Code CLI，或明确报告为什么无法调用。

常用 cc-switch 查询命令：

```powershell
cc-switch provider list
cc-switch provider current
cc-switch provider fetch-models <provider-id>
cc-switch use <provider-id>
```

带模型的一次性调用示例：

```powershell
claude -p "<任务包>" --model <model> --permission-mode dontAsk --tools=""
```

## Codex 调用前任务包

Codex 交给外部 Agent 前，应自动补齐任务包，不要求用户每次手写完整说明：

- 项目路径和目标 Git 根目录。
- 任务 ID、任务目标和当前状态。
- 任务 `Owner` 和 `主执行 Agent`；调用 Cursor 前写 `cursor`，调用 Claude Code 前写 `claude`，Codex 自己执行时写 `codex`。
- 当前调用身份：执行模式、只读分析模式或 flow 模式。
- 允许修改范围和禁止范围。
- 是否允许改代码。
- 是否允许维护任务状态文件。
- 期望输出、验证要求和必须返回的证据。
- 若任务涉及用户 Wiki 中的领域知识或历史决策，按 `.agents/context/LLM_WIKI.md` 搜索并摘要写入 prompt 上下文；注明来源页路径。
- 明确声明：任务事实源和最终采纳权仍归 Codex。

任务包必须能直接复制给 Cursor 或 Claude Code 执行。若写入文件，推荐放在对应任务目录，例如 `.ai/tasks/<TaskId>/cursor-flow-prompt.md`、`.ai/tasks/<TaskId>/claude-code-prompt.md`；但写入文件后仍必须立即调用对应外部 Agent，不能把“已准备 prompt”当作完成。

## Codex 调用动作

用户触发 Cursor 或 Claude Code 调用后，Codex 必须按以下顺序执行：

1. 识别当前要交给外部 Agent 的任务或问题；没有任务 ID 时，按当前角色规则先建任务或说明无需任务的原因。
2. 在任务板和任务说明的基本信息中标记 `主执行 Agent`：Cursor 调用写 `cursor`，Claude Code 调用写 `claude`；仅 Codex 自己执行时写 `codex`。
3. 生成给外部 Agent 的 prompt，包含项目路径、任务目标、允许范围、禁止范围、验证要求和返回格式。
4. 使用默认 CLI 命令实际调用 Cursor 或 Claude Code。
5. 等待外部 Agent 返回结果。
6. 按“Codex 调用后收口”复查结果。

只有以下情况可以不实际调用外部 Agent：

- 用户明确要求只生成 prompt 或只讨论规则。
- Cursor / Claude Code CLI 不存在、未登录、权限被拦截或命令无法启动。
- 当前任务缺少必要边界，继续调用会造成越权修改。

无法调用时，Codex 必须把原因说清楚，并给出已经准备好的 prompt。

## Cursor flow 模式

当 Codex 明确让 Cursor 以 `flow` 身份执行时，Cursor 不应只把任务推进到 `CODE_READY` 就停止。

Cursor flow 模式必须完成以下动作之一：

1. 按项目任务流继续推进：`CODE_READY -> TESTING -> REVIEW_READY -> REVIEWING -> DONE`。
2. 因测试、审查、锁、依赖、权限或环境问题无法继续时，明确写出阻塞原因和下一步处理身份。

Cursor flow 模式可以在 Codex 授权范围内维护任务状态、锁、交接和归档；但不得越过任务包边界，不得修改无关项目状态。

## Codex 调用后收口

外部 Agent 返回后，Codex 必须复查，不直接把“已完成”当作最终事实：

- `ai/TASK_BOARD.md` 状态是否符合任务流。
- `TASK_BOARD.md`、`task.md` 和最近交接中的 `主执行 Agent` 是否与实际执行方一致。
- `ai/TASK_LOCKS.md` 是否释放或正确记录阻塞。
- `.ai/tasks/<TaskId>/handoff.md` 是否写清完成内容、验证证据和下一步。
- `ai/TASK_ARCHIVE.md` 是否只记录已归档任务。
- 是否跳过了必须的测试或最终审查。
- 是否越权修改了任务事实源或协作资产。
- 是否满足用户原始任务、bug、问题、需求或验收边界。
- 是否存在实现偏题、漏项、误改、未验证、状态流转不完整或“说完成但事实未完成”的情况。

发现收口缺口时，Codex 应按项目规则补齐协作状态或交给对应角色处理；外部 Agent 的输出只能作为输入材料。

## 复检与返工闭环
<!-- agent-call-recheck-loop -->

Cursor 或 Claude Code 完成后，Codex 必须复检。复检不是可选动作，不能因为外部 Agent 声称完成就结束。

复检范围包括：

1. 用户原始意图是否满足。
2. 任务说明、验收标准、允许范围和禁止范围是否满足。
3. `主执行 Agent` 是否记录为本轮实际执行方，后续返工是否能按该字段找回对应 Agent。
4. 修改是否越界，是否破坏任务状态、锁、归档或项目事实源。
5. bug、问题或需求是否真的解决，而不是只写了说明。
6. 必要验证、测试、审查或静态检查是否已经完成或明确说明不可执行原因。

如果复检发现不符合，Codex 必须直接打开对应任务继续处理：

1. 写清复检发现的问题。
2. 写清返工目标、允许范围、禁止范围、验收标准和必须返回的证据。
3. 优先按任务 `主执行 Agent` 交回对应 Agent 重做：`cursor` 返给 Cursor，`claude` 返给 Claude Code，`codex` 由 Codex 或项目角色继续处理；若需要改派，先写明原因并更新字段。
4. 外部 Agent 再次返回后，Codex 继续复检。

至少必须执行一轮返工；不得在第一次复检发现问题后只告诉用户“外部 Agent 没做好”就结束。

只有以下情况可以停止返工并回到用户：

- Codex 也无法判断正确做法或无法解释阻塞。
- 缺少用户必须拍板的信息，继续会猜测需求或越权修改。
- 外部依赖、权限、环境或工具不可用，且 Codex 无法绕过。
- 已经完成至少一轮返工后仍存在 P1/P2/P3 问题，需要用户取舍。

停止时必须按固定格式汇报：

```text
已完成：
1. ...
2. ...
3. ...

问题：
- P1/P2/P3：问题描述、影响范围、为什么现在不能继续。

建议：
1. 推荐做法。
2. 备选做法。
```

问题分级沿用项目 `AGENTS.md` 的 P1/P2/P3 口径；不得只写“有问题”。

## 禁止事项

- 不让 Cursor 或 Claude Code 成为任务状态事实源。
- 不让外部 Agent 自行决定需求、验收标准、最终审查结论或归档规则。
- 不把外部 Agent 的输出直接写入任务板，除非 Codex 已审定。
- 不把项目运行状态复制进用户级母版。
