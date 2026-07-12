# 变量作用域

## 学习目标

- 理解局部变量和全局变量
- 掌握 global 关键字的使用
- 了解 nonlocal 关键字的使用

## 知识点

### 1. 局部变量

在函数内部定义的变量，只在函数内部有效。

```python
def foo():
    x = 10  # 局部变量
    print(f"函数内: x = {x}")

foo()
# print(x)  # 错误：x 未定义
```

### 2. 全局变量

在函数外部定义的变量，在整个程序中有效。

```python
x = 10  # 全局变量

def foo():
    print(f"函数内: x = {x}")

foo()
print(f"函数外: x = {x}")
```

### 3. global 关键字

在函数内部修改全局变量。

```python
x = 10

def foo():
    global x
    x = 20

foo()
print(x)  # 20
```

### 4. nonlocal 关键字

在嵌套函数中修改外层函数的变量。

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # 20

outer()
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 局部变量和全局变量
- global 关键字
- nonlocal 关键字

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
