# 比较和逻辑运算符

## 学习目标

- 掌握比较运算符的使用
- 了解逻辑运算符的使用
- 掌握成员运算符的使用
- 了解身份运算符的使用

## 知识点

### 1. 比较运算符

```python
a, b = 10, 20

a == b  # 等于：False
a != b  # 不等于：True
a > b   # 大于：False
a < b   # 小于：True
a >= b  # 大于等于：False
a <= b  # 小于等于：True
```

### 2. 逻辑运算符

```python
x, y = True, False

x and y  # 与：False
x or y   # 或：True
not x    # 非：False
```

### 3. 成员运算符

```python
fruits = ["apple", "banana", "cherry"]

"apple" in fruits      # True
"grape" in fruits      # False
"grape" not in fruits  # True
```

### 4. 身份运算符

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a is b      # False（不同对象）
a is c      # True（同一对象）
a == b      # True（值相同）
```

### 5. 运算符优先级

从高到低：
1. `**`（幂）
2. `~`, `+`, `-`（一元运算符）
3. `*`, `/`, `//`, `%`（乘除）
4. `+`, `-`（加减）
5. `>>`, `<<`（位移）
6. `&`（位与）
7. `^`（位异或）
8. `|`（位或）
9. `==`, `!=`, `>`, `<`, `>=`, `<=`（比较）
10. `not`（逻辑非）
11. `and`（逻辑与）
12. `or`（逻辑或）

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 比较运算符
- 逻辑运算符
- 成员运算符
- 身份运算符

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
