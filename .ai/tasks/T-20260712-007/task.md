# T-20260712-007 创建 README.md 并分离功能说明

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
- 上下文摘要：用户希望将功能使用说明从 COURSE_INDEX.md 分离到 README.md，使职责更清晰

## 目标

1. 创建 `python-course/README.md`，包含项目介绍和功能说明
2. 更新 `python-course/COURSE_INDEX.md`，只保留课程索引、大纲和学习资源

## 范围

### 允许范围

- 创建 `python-course/README.md`
- 更新 `python-course/COURSE_INDEX.md` 删除功能说明部分

### 禁止范围

- 不修改业务代码
- 不修改其他文件

## 验收标准

1. `python-course/README.md` 存在且包含：
   - 项目介绍
   - 功能说明（上传更新、重新学习）
   - 使用方法

2. `python-course/COURSE_INDEX.md` 只包含：
   - 学习进度表格
   - 学习资源
   - 课程大纲
   - 基本使用说明（简短版）

## 交付内容

### 文件清单

1. `python-course/README.md` - 新建的项目说明文件
2. `python-course/COURSE_INDEX.md` - 更新后的课程索引

### README.md 内容结构

```markdown
# Python 学习课程

## 项目介绍
[项目简介]

## 功能说明

### 上传更新
[功能描述、触发语、执行流程、commit message 格式]

### 重新学习
[功能描述、触发语、使用场景、执行流程、示例]

## 使用方法
[简短的使用步骤]
```

### COURSE_INDEX.md 更新

删除"功能说明"部分，只保留：
- 学习进度表格
- 学习资源
- 课程大纲
- 基本使用说明（简短版）

## 备注

- 这是协作资产任务，由 aiskill 直接完成，不进入测试或审查队列
- 完成自检后直接标记 DONE
