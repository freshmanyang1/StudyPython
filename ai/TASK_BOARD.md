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

### T-20260712-006 更新 COURSE_INDEX.md 添加功能使用说明

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
| 任务说明 | `.ai/tasks/T-20260712-006/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-006/handoff.md` |
| 有效代码行 | 0（协作资产） |

**目标摘要**：更新 COURSE_INDEX.md，添加"上传更新"和"重新学习"功能的使用说明

**范围摘要**：更新 `python-course/COURSE_INDEX.md`，添加功能使用说明

**备注**：协作资产任务，已完成自检

### T-20260712-007 创建 README.md 并分离功能说明

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
| 任务说明 | `.ai/tasks/T-20260712-007/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-007/handoff.md` |
| 有效代码行 | 0（协作资产） |

**目标摘要**：创建 README.md，将功能使用说明从 COURSE_INDEX.md 分离出来

**范围摘要**：创建 `python-course/README.md`，更新 `python-course/COURSE_INDEX.md`

**备注**：协作资产任务，已完成自检

### T-20260712-008 移动 README.md 到项目根目录

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
| 任务说明 | `.ai/tasks/T-20260712-008/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-008/handoff.md` |
| 有效代码行 | 0（协作资产） |

**目标摘要**：将 README.md 从 python-course/ 目录移动到项目根目录

**范围摘要**：移动 `python-course/README.md` 到 `README.md`，更新链接

**备注**：协作资产任务，已完成自检

### T-20260712-009 完善上传更新功能触发语

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
| 任务说明 | `.ai/tasks/T-20260712-009/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-009/handoff.md` |
| 有效代码行 | 0（协作资产） |

**目标摘要**：完善上传更新功能，支持"上传"、"更新"、"提交"、"上传更新"触发语

**范围摘要**：更新 `.agents/skills/python/SKILL.md` 和 `README.md`

**备注**：协作资产任务，已完成自检

### T-20260712-010 创建新课程目录结构和索引

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | 无 |
| 依赖门禁 | 无 |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-010/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-010/handoff.md` |
| 有效代码行 | 0（目录和索引） |

**目标摘要**：创建新课程目录结构和索引，从 20 课扩展到 39 课

**范围摘要**：删除旧课程目录，创建 39 个新课程目录，更新 COURSE_INDEX.md

**备注**：架构师任务，已完成自检

### T-20260712-011 创建第一阶段课程（01-05）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-010 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-011/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-011/handoff.md` |
| 有效代码行 | 15（课程文件） |

**目标摘要**：创建第一阶段课程（01-05）内容，适合小白学习

**范围摘要**：创建 5 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-012 创建第二阶段课程（06-10）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-011 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-012/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-012/handoff.md` |
| 有效代码行 | 15（课程文件） |

**目标摘要**：创建第二阶段课程（06-10）内容，学习数据结构

**范围摘要**：创建 5 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-013 创建第三阶段课程（11-14）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-012 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-013/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-013/handoff.md` |
| 有效代码行 | 12（课程文件） |

**目标摘要**：创建第三阶段课程（11-14）内容，学习流程控制

**范围摘要**：创建 4 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-014 创建第四阶段课程（15-19）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-013 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-014/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-014/handoff.md` |
| 有效代码行 | 15（课程文件） |

**目标摘要**：创建第四阶段课程（15-19）内容，学习函数

**范围摘要**：创建 5 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-015 创建第五阶段课程（20-24）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-014 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-015/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-015/handoff.md` |
| 有效代码行 | 15（课程文件） |

**目标摘要**：创建第五阶段课程（20-24）内容，学习高级特性

**范围摘要**：创建 5 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-016 创建第六阶段课程（25-27）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-015 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-016/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-016/handoff.md` |
| 有效代码行 | 9（课程文件） |

**目标摘要**：创建第六阶段课程（25-27）内容，学习函数式编程

**范围摘要**：创建 3 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-017 创建第七阶段课程（28-29）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-016 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-017/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-017/handoff.md` |
| 有效代码行 | 6（课程文件） |

**目标摘要**：创建第七阶段课程（28-29）内容，学习模块和包

**范围摘要**：创建 2 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-018 创建第八阶段课程（30-33）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-017 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-018/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-018/handoff.md` |
| 有效代码行 | 12（课程文件） |

**目标摘要**：创建第八阶段课程（30-33）内容，学习面向对象编程

**范围摘要**：创建 4 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-019 创建第九阶段课程（34-36）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-018 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-019/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-019/handoff.md` |
| 有效代码行 | 9（课程文件） |

**目标摘要**：创建第九阶段课程（34-36）内容，学习错误处理

**范围摘要**：创建 3 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

### T-20260712-020 创建第十阶段课程（37-39）

| 字段 | 值 |
|---|---|
| 状态 | DONE |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-019 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |
| 任务说明 | `.ai/tasks/T-20260712-020/task.md` |
| 交接文件 | `.ai/tasks/T-20260712-020/handoff.md` |
| 有效代码行 | 9（课程文件） |

**目标摘要**：创建第十阶段课程（37-39）内容，学习文件操作

**范围摘要**：创建 3 个课程的 README.md、demo.py、homework.py

**备注**：架构师任务，已完成自检

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
