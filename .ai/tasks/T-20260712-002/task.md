# T-20260712-002 创建 pythonskill

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
- 上下文摘要：用户希望创建一个 Python 学习管理 skill，用于管理课程、推送进度、生成作业和打分

## 目标

创建 `pythonskill` 的 SKILL.md，定义一个 Python 学习助手角色，具备以下能力：
1. 维护课程索引和学习进度
2. 推送下一节课程内容
3. 提前生成课程文件夹和文件
4. 接收作业提交并打分
5. 记录分数到课程索引

## 范围

### 允许范围

- 创建 `.agents/skills/python/SKILL.md`
- 更新 `.agents/skill-registry.md` 添加 python skill 条目
- 更新 `.agents/ROLE_ENTRYPOINTS.md` 添加 python 角色入口

### 禁止范围

- 不修改业务代码
- 不抓取网站内容（由 T-20260712-003 负责）
- 不实现自动化逻辑

## 验收标准

1. `.agents/skills/python/SKILL.md` 存在且格式正确
2. SKILL.md 包含以下章节：
   - 定位：Python 学习助手
   - 工作闸门：触发语、启动检查
   - 可以做：课程管理、进度推送、文件生成、作业打分
   - 不可以做：边界定义
   - 按需读取：课程索引、课程内容
   - 输出格式：课程推送格式、打分格式
3. `.agents/skill-registry.md` 包含 python skill 条目
4. `.agents/ROLE_ENTRYPOINTS.md` 包含 python 角色入口

## 交付内容

### 文件清单

1. `.agents/skills/python/SKILL.md` - Python 学习助手 Skill 定义
2. `.agents/skill-registry.md` - 更新后的 Skill 注册表
3. `.agents/ROLE_ENTRYPOINTS.md` - 更新后的角色入口表

### SKILL.md 必须包含的内容

#### 触发语
- `切换python` - 切换到 python 身份
- `python，开始工作` - 进入自动化流程
- `python，下一课` - 推送下一节课程
- `python，提交作业` - 提交作业并打分

#### 课程推送格式
```
## 课程：[课程标题]

### 学习目标
- 目标1
- 目标2

### 课程内容
[内容摘要]

### 本节文件
- `python-course/XX-课程名/README.md` - 课程内容
- `python-course/XX-课程名/demo.py` - 示例代码
- `python-course/XX-课程名/homework.py` - 作业

### 作业要求
[具体要求]

完成后输入 `python，提交作业` 提交。
```

#### 打分格式
```
## 作业评分

**课程**：[课程标题]
**得分**：XX/100

### 评分维度
- 运行结果：XX/40
- 代码规范：XX/30
- 完成度：XX/30

### 反馈
- 优点：...
- 改进建议：...

### 索引已更新
COURSE_INDEX.md 已更新分数。
```

## 备注

- 这是协作资产任务，由 aiskill 直接完成，不进入测试或审查队列
- 完成自检后直接标记 DONE
