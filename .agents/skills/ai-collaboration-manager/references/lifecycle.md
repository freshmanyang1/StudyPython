# AI Collaboration Lifecycle

## Skill 添加要求

添加 Skill 前必须输出：

- Skill 名称
- 使用场景
- 适用对象：Codex / Claude / 两者都适用
- 项目级或个人级
- 是否依赖 `AGENTS.md`
- 是否有安全风险
- 安装或创建位置
- `SKILL.md` 草案
- 验收标准

## Skill 修改要求

修改 Skill 前必须输出：

- 修改原因
- 修改前问题
- 修改后行为
- 影响哪些 AI 角色
- 是否影响现有 Prompt
- 回滚方式

## Skill 删除要求

删除 Skill 前必须输出：

- 删除原因
- 是否有替代 Skill
- 是否仍被 Prompt 或 `AGENTS.md` 引用
- 删除风险
- 回滚方式

## 注册表维护

新增、修改、删除 Skill 后，必须同步检查 `.agents/skill-registry.md` 是否需要更新。

注册表至少记录：

- 正式名称
- 代称
- 来源
- 适用对象
- 当前状态
- 调用方式
- 冲突或重叠关系
- 风险说明

## 输出格式

维护完成后必须输出：

- 本次变更摘要
- 涉及文件
- 风险提示
- 后续建议

## 项目约束

遵守根目录 `AGENTS.md` 的通用修改硬规则，包括但不限于：默认不运行 build/test/lint、只做最小补丁、保留中文注释、第三方 Skill 默认先评估不直接安装。
