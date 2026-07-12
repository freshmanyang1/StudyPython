# 角色注册表

本文件只维护角色属性、入口映射、路径映射和跨角色硬约束。详细职责边界以各角色 `.agents/skills/**/SKILL.md` 为唯一正文。

## 角色属性表

| 用户称呼 | Skill 名称 | 类型 | 入口文件 |
|---|---|---|---|
| 项目经理 | project-manager | 计划者 | `.agents/skills/project-manager/SKILL.md` |
| 架构师 | architect | 全能技术角色 | `.agents/skills/architect/SKILL.md` |
| 后端 | dev-backend | 受控执行者 | `.agents/skills/dev-backend/SKILL.md` |
| 前端 | dev-frontend | 受控执行者 | `.agents/skills/dev-frontend/SKILL.md` |
| 测试 | tester | 交付验证 | `.agents/skills/tester/SKILL.md` |
| 审查 | code-reviewer | 最终批改 | `.agents/skills/code-reviewer/SKILL.md` |
| flow | flow | 任务流大管家 | `.agents/skills/flow/SKILL.md` |
| aiskill | ai-collaboration-manager | 协作资产维护者 | `.agents/skills/ai-collaboration-manager/SKILL.md` |

## 文件路径与角色映射

| 文件路径模式 | 默认 Owner |
|---|---|
| `{{MAIN_SOURCE_PATH}}/**` | 后端工程师 / 前端工程师 / 架构师 |
| `.agents/**` | aiskill |
| `ai/**` | 项目经理；其中角色规则、交接协议和协作规则段由 aiskill 维护 |
| `AGENTS.md` | aiskill |
