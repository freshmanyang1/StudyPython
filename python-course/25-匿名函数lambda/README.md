# 匿名函数lambda

## 学习目标

- 掌握 lambda 函数的语法
- 了解 lambda 函数的使用场景
- 理解 lambda 函数与普通函数的区别

## 知识点

### 1. lambda 语法

```python
# 基本语法
square = lambda x: x ** 2
print(square(5))  # 25

# 多个参数
add = lambda x, y: x + y
print(add(3, 5))  # 8
```

### 2. 使用场景

```python
# 作为参数传递
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

# 排序
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
```

### 3. 与普通函数的区别

```python
# 普通函数
def square(x):
    return x ** 2

# lambda 函数
square = lambda x: x ** 2
```

**区别**：
- lambda 只能包含一个表达式
- lambda 没有函数名（匿名）
- lambda 适合简单的操作

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- lambda 函数的语法
- lambda 函数的使用场景
- lambda 函数与普通函数的区别

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
