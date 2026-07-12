# 第一个Python程序

## 学习目标

- 掌握 print() 函数的使用
- 了解注释的写法
- 理解 `if __name__ == "__main__":` 的含义
- 掌握执行 Python 文件的方法

## 知识点

### 1. print() 函数

`print()` 是 Python 最基本的输出函数，用于在屏幕上显示内容。

```python
# 输出字符串
print("Hello, World!")

# 输出数字
print(42)

# 输出多个值
print("姓名:", "张三")

# 使用分隔符
print("2024", "01", "01", sep="-")

# 使用结尾符
print("Hello", end=" ")
print("World")
```

### 2. 注释

注释是代码中不会被执行的文字，用于解释代码的作用。

**单行注释**：
```python
# 这是单行注释
print("Hello")  # 这也是单行注释
```

**多行注释**：
```python
"""
这是多行注释
可以写多行
通常用于文档说明
"""

'''
这也是多行注释
'''
```

### 3. 执行 Python 文件

**步骤**：
1. 创建一个 `.py` 文件，例如 `hello.py`
2. 在文件中写入代码
3. 在命令行执行：`python hello.py`

**示例**：
```python
# hello.py
print("Hello, World!")
```

```bash
python hello.py
# 输出：Hello, World!
```

### 4. `if __name__ == "__main__":` 详解

这是一个 Python 的特殊用法，用于判断当前文件是否被直接执行。

**含义**：
- `__name__` 是 Python 的内置变量
- 当文件被直接执行时，`__name__` 的值是 `"__main__"`
- 当文件被导入时，`__name__` 的值是模块名

**示例**：
```python
# hello.py
def greet():
    print("Hello!")

if __name__ == "__main__":
    # 只有直接执行此文件时才会运行
    greet()
```

**为什么使用它**：
- 当文件被导入时，不会自动执行测试代码
- 当文件被直接执行时，可以运行测试代码

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- print() 函数的各种用法
- 注释的写法
- `if __name__ == "__main__":` 的使用

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
