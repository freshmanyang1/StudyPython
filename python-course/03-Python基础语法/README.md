# Python基础语法

## 学习目标

- 掌握 Python 的缩进规则
- 了解标识符的命名规则
- 掌握 Python 的关键字
- 了解语句的写法

## 知识点

### 1. 缩进

Python 使用缩进来表示代码块，而不是使用大括号 `{}`。

```python
if True:
    print("缩进的代码块")
    print("属于同一个代码块")
print("不在 if 代码块中")
```

**缩进规则**：
- 使用 4 个空格作为一级缩进
- 可以使用 Tab 键，但要保持一致
- 同一代码块的缩进必须一致

### 2. 标识符

标识符是用来命名变量、函数、类等的名称。

**命名规则**：
- 由字母、数字、下划线组成
- 不能以数字开头
- 区分大小写
- 不能使用关键字

**命名规范**：
- 变量名：小写字母，单词间用下划线连接（`my_name`）
- 常量名：全大写字母（`MAX_SIZE`）
- 类名：大驼峰（`MyClass`）
- 函数名：小写字母，单词间用下划线连接（`get_name`）

### 3. 关键字

Python 有以下关键字，不能用作标识符：

```python
import keyword
print(keyword.kwlist)
```

常用关键字：
- `if`, `elif`, `else`：条件判断
- `for`, `while`：循环
- `def`：定义函数
- `class`：定义类
- `import`, `from`：导入模块
- `return`：返回值
- `True`, `False`, `None`：布尔值和空值

### 4. 语句

**单行语句**：
```python
x = 10
print(x)
```

**多行语句**：
```python
# 使用反斜杠换行
total = 1 + 2 + 3 + \
        4 + 5 + 6

# 在括号内可以自动换行
total = (1 + 2 + 3 +
         4 + 5 + 6)
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 缩进的使用
- 标识符的命名
- 关键字的查看
- 语句的写法

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
