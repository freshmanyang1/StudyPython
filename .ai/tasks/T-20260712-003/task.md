# T-20260712-003 抓取网站课程整理大纲

## 基本信息

| 字段 | 值 |
|---|---|
| 状态 | PLANNED |
| Owner | 架构师 |
| 主执行 Agent | claude |
| 模块 | Python学习 |
| 类型 | 完整任务 |
| 优先级 | P1 |
| 依赖 | T-20260712-002 |
| 依赖门禁 | DONE |
| 目标 Git 根目录 | d:\Dev\StudyPython |
| 允许验证命令 | 静态验证 |

## 来源

- 来源任务：无（用户直接需求）
- 派生深度：0
- 来源类型：用户需求
- 承接/替代：无
- 上下文摘要：用户希望从廖雪峰和菜鸟教程两个网站抓取 Python 课程内容，整理成结构化大纲索引

## 目标

从以下两个网站抓取 Python 课程内容，整理成结构化大纲：
1. 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
2. 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html

生成以下内容：
1. `python-course/COURSE_INDEX.md` - 课程总索引
2. `python-course/XX-课程名/` - 每个课程的文件夹结构

## 范围

### 允许范围

- 创建 `python-course/` 目录结构
- 创建 `python-course/COURSE_INDEX.md` 课程索引
- 创建每个课程的文件夹和 README.md
- 创建每个课程的 demo.py 示例代码
- 创建每个课程的 homework.py 作业文件

### 禁止范围

- 不修改业务代码
- 不修改 `.agents/` 协作资产（由 T-20260712-002 负责）
- 不实现自动化打分逻辑

## 验收标准

1. `python-course/COURSE_INDEX.md` 存在且包含：
   - 课程列表（按章节排序）
   - 每个课程的路径
   - 分数字段（初始为空）
   - 学习状态（未开始/进行中/已完成）

2. 每个课程文件夹包含：
   - `README.md` - 课程内容（包含学习目标、知识点、示例说明）
   - `demo.py` - 示例代码（带详细注释）
   - `homework.py` - 作业文件（带注释说明要求，留空白让学生填写）

3. 课程大纲覆盖以下主题（至少）：
   - Python 基础：变量、数据类型、字符串、列表、元组、字典、集合
   - 流程控制：条件判断、循环
   - 函数：定义、参数、返回值、递归
   - 模块：导入、包、第三方库
   - 面向对象：类、继承、多态
   - 文件 I/O：读写文件、路径处理
   - 错误处理：异常、调试
   - 进阶：正则表达式、进程线程、网络编程

4. 以廖雪峰为主线，菜鸟教程作为补充参考

## 交付内容

### 文件清单

1. `python-course/COURSE_INDEX.md` - 课程总索引
2. `python-course/01-第一个Python程序/README.md` - 课程内容
3. `python-course/01-第一个Python程序/demo.py` - 示例代码
4. `python-course/01-第一个Python程序/homework.py` - 作业
5. `python-course/02-...` - 后续课程...

### COURSE_INDEX.md 格式

```markdown
# Python 学习课程索引

## 学习进度

| 序号 | 课程 | 路径 | 状态 | 分数 |
|---|---|---|---|---|
| 01 | 第一个Python程序 | `01-第一个Python程序/` | 未开始 | - |
| 02 | Python基础 | `02-Python基础/` | 未开始 | - |
| ... | ... | ... | ... | ... |

## 学习资源

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
```

### README.md 格式（每课）

```markdown
# [课程标题]

## 学习目标

- 目标1
- 目标2

## 知识点

### 知识点1
[详细说明]

### 知识点2
[详细说明]

## 示例说明

[demo.py 中的代码说明]

## 参考资料

- [链接1]
- [链接2]
```

### homework.py 格式（每课）

```python
"""
课程：[课程标题]
作业要求：
1. 要求1
2. 要求2
3. 要求3

完成后输入 `python，提交作业` 提交。
"""

# 作业1：[题目]
# 请在此处填写代码
def homework1():
    pass

# 作业2：[题目]
# 请在此处填写代码
def homework2():
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1:")
    homework1()
    print("\n测试作业2:")
    homework2()
```

## 备注

- 依赖 T-20260712-002 完成后才能开始
- 课程内容以廖雪峰为主线，菜鸟教程为补充
- 每个课程的 homework.py 需要设计合理的作业题目
