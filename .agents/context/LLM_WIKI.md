# LLM Wiki 读取规则

本文件定义 Codex / Cursor / Claude 读取用户本机 LLM Wiki 知识库的通用协作规则。

## 定位

- LLM Wiki 是用户本地运行的知识库桌面应用，提供 HTTP API（默认 `127.0.0.1:19828`）。
- Wiki 是**长期知识层**，补充项目上下文、概念解释和历史决策依据。
- **不是任务事实源**：任务状态、锁、PM 决策、归档和任务板仍以 `ai/**` 和 `.ai/tasks/**` 为准。
- **不是运行副本**：Wiki 内容不复制到母版、项目运行副本或任务说明中。

## 触发条件

仅当用户明确指代 LLM Wiki 时触发：

- "wiki 里怎么说的" / "我的知识库怎么说" / "我的 wiki 里关于 X" / "LLM Wiki"
- "搜索我的 wiki" / "读 wiki 页面" / "查看 wiki 图谱" / "重新索引 wiki"
- 用户指定了 wiki 项目名称或路径

**不触发**：泛指"搜索笔记"、Obsidian、Notion、Logseq、Jupyter、OneNote 等其他工具。

## API 协议摘要

| 项目 | 值 |
|---|---|
| 基础地址 | `http://127.0.0.1:19828` |
| 路径前缀 | `/api/v1` |
| 认证方式 | `Authorization: Bearer <token>` 或 `X-LLM-Wiki-Token: <token>` 或 `?token=<token>` |
| Token 来源 | 环境变量 `LLM_WIKI_API_TOKEN`（优先）或桌面应用 Settings → API Server |
| 连通性探测 | `GET /api/v1/health`（无需认证） |

### 核心端点

| 方法 | 路径 | 用途 |
|---|---|---|
| GET | `/api/v1/health` | 探测应用状态和认证配置（无需 token） |
| GET | `/api/v1/projects` | 列出所有项目，返回 `{id, name, path, current}` |
| GET | `/api/v1/projects/{id}/files` | 文件树，支持 `?root=wiki\|sources\|all&recursive=true` |
| GET | `/api/v1/projects/{id}/files/content?path=...` | 读取单个文本文件（md/txt/json/yaml 等，2MB 上限） |
| POST | `/api/v1/projects/{id}/search` | 混合搜索（关键词+向量），body: `{query, topK, includeContent}` |
| GET | `/api/v1/projects/{id}/graph` | wikilinks 知识图谱，支持 `?q=&nodeType=&limit=` |
| POST | `/api/v1/projects/{id}/sources/rescan` | 触发源文件重新索引（唯一写操作） |
| POST | `/api/v1/projects/{id}/chat` | 501 未实现，不要调用 |

`{id}` 接受：UUID、绝对文件路径（URL 编码）、字面量 `current`。

## 标准调用流程

1. **探测**：`GET /api/v1/health`，检查 `enabled`、`authConfigured`、`tokenSource`。
   - 若 `authConfigured: false && allowUnauthenticated: false`，提示用户在 Settings → API Server → Generate new token。
   - 若连接失败（connection refused），提示用户启动 LLM Wiki 桌面应用。
2. **搜索**：`POST /api/v1/projects/{id}/search`，body 含 `query`、`topK: 5~10`。
3. **读取**：对搜索结果中相关条目，`GET .../files/content?path=...` 获取全文；或搜索时设 `includeContent: true` 避免额外请求。
4. **引用**：回答时引用 `path`（如 `wiki/concepts/rope.md`），供用户验证和跳转。

### 项目解析规则

- 用户说"我的 wiki" / "当前项目" → 使用 `current`
- 用户指定项目名称 → 先 `GET /projects` 列出，大小写不敏感子串匹配 `name`，0 匹配则告知用户并列出可用名称，2+ 匹配则要求用户消歧
- 用户指定文件路径 → URL 编码后直接用作 `{id}`
- 同一会话内缓存已解析的项目 ID，不重复列举

### 搜索评分解读

- `mode: "keyword"`：加法关键词评分，精确文件名命中约 200，标题短语命中约 50+
- `mode: "hybrid"` 或 `"vector"`：RRF 评分，典型范围 0.015~0.035
- 不同 mode 之间不要用固定阈值比较，按相对排序判断
- `vectorScore`（0~1 范围）可用于判断语义匹配强度

## Codex 调用前 Wiki 读取

Codex 生成任务包交给 Cursor / Claude 前，若任务涉及用户 Wiki 中记录的领域知识、历史决策或技术概念：

1. 按上述流程搜索相关 Wiki 页面。
2. 将搜索结果摘要（非全文）作为任务包的**上下文补充**写入 prompt。
3. 在任务包中注明来源：`（来自 LLM Wiki: wiki/xxx.md）`。
4. 不把 Wiki 内容当作任务事实源；任务定义、验收标准和状态仍由任务板决定。

## 限制与注意事项

- 端点限速：120 请求/秒（全局），并发上限 64
- 文件内容上限 2MB，请求体上限 1MB
- 仅支持文本文件（md/txt/json/yaml/csv/html 等），二进制文件返回 415
- Token 视为本地密钥，不在输出、日志或 URL 中明文暴露
- `sources/rescan` 是唯一的写操作，且只排队不等待完成
- 完整 API 细节见上游仓库：`https://github.com/nashsu/llm_wiki_skill`（`api-reference.md`、`examples.md`）

## 跨平台注意事项

- Windows 下使用 `curl.exe`（而非 PowerShell 别名 `curl`）
- 文件路径在 API 请求中使用正斜杠
- Windows 文件路径作为 `{id}` 时需 URL 编码（`[System.Uri]::EscapeDataString()`）
