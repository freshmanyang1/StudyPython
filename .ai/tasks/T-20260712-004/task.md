# T-20260712-004 更新 pythonskill 添加上传更新功能

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
- 上下文摘要：用户希望在学习完成后，通过"上传更新"指令自动保存学习进度并推送到 GitHub

## 目标

更新 `pythonskill` 的 SKILL.md，添加"上传更新"功能：
1. 用户说"上传更新"时，自动保存学习进度
2. 自动生成 commit message（包含课程名和分数）
3. 自动 pull+push 到 GitHub

## 范围

### 允许范围

- 更新 `.agents/skills/python/SKILL.md` 添加上传更新功能
- 更新 `python-course/COURSE_INDEX.md` 的进度状态
- 执行 git add、commit、pull、push 操作

### 禁止范围

- 不修改业务代码
- 不修改其他 Skill
- 不修改 git 配置

## 验收标准

1. `.agents/skills/python/SKILL.md` 包含"上传更新"触发语
2. 用户说"上传更新"时，能够：
   - 读取当前学习进度
   - 添加进度文件和作业文件到 git
   - 自动生成 commit message
   - 执行 git pull --rebase
   - 执行 git push
3. commit message 格式为：`更新进度：XX-课程名 XX分` 或 `更新进度：XX-课程名 已完成`

## 交付内容

### 文件清单

1. `.agents/skills/python/SKILL.md` - 更新后的 Python 学习助手 Skill

### SKILL.md 新增内容

#### 触发语
- `上传更新` - 保存学习进度并推送到 GitHub

#### 执行流程
```
1. 读取 python-course/COURSE_INDEX.md 获取当前进度
2. 找到最近完成的课程（状态为"已完成"）
3. git add python-course/ 相关文件
4. git commit -m "更新进度：XX-课程名 XX分"
5. git pull --rebase origin master
6. git push origin master
7. 输出上传结果
```

#### 输出格式
```
## 上传更新

**课程**：XX-课程名
**分数**：XX分
**状态**：已推送到 GitHub

**提交信息**：更新进度：XX-课程名 XX分
**远程地址**：https://github.com/freshmanyang1/StudyPython
```

## 备注

- 这是协作资产任务，由 aiskill 直接完成，不进入测试或审查队列
- 完成自检后直接标记 DONE
