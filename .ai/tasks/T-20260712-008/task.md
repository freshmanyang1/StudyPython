# T-20260712-008 移动 README.md 到项目根目录

## 基本信息

| 字段 | 值 |
|---|---|
| 状态 | PLANNED |
| Owner | aiskill |
| 主执行 Agent | claude |
| 模块 | 协作资产 |
| 类型 | 协作资产任务 |
| 优先级 | P1 |
| 依赖 | 无 |
| 依赖门禁 | 无 |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |

## 来源

- 来源任务：无（用户直接需求）
- 派生深度：0
- 来源类型：用户需求
- 承接/替代：无
- 上下文摘要：用户希望将 README.md 从 python-course/ 目录移动到项目根目录

## 目标

将 `python-course/README.md` 移动到项目根目录 `d:\Dev\StudyPython\README.md`

## 范围

### 允许范围

- 移动 `python-course/README.md` 到 `README.md`
- 更新 `python-course/COURSE_INDEX.md` 中的链接

### 禁止范围

- 不修改业务代码
- 不修改其他文件

## 验收标准

1. `README.md` 存在于项目根目录
2. `python-course/README.md` 已删除
3. `python-course/COURSE_INDEX.md` 中的链接已更新

## 交付内容

### 文件清单

1. `README.md` - 移动后的项目说明文件
2. `python-course/COURSE_INDEX.md` - 更新链接

## 备注

- 这是协作资产任务，由 aiskill 直接完成，不进入测试或审查队列
- 完成自检后直接标记 DONE
