# 条件判断

## 学习目标

- 掌握 if 语句的语法
- 了解 if-else 和 if-elif-else 结构
- 掌握条件表达式（三元运算符）
- 理解布尔运算和比较运算

## 知识点

### 1. if 语句

```python
x = 10
if x > 0:
    print("x 是正数")
```

### 2. if-else 语句

```python
x = -5
if x > 0:
    print("x 是正数")
else:
    print("x 是负数或零")
```

### 3. if-elif-else 语句

```python
x = 0
if x > 0:
    print("x 是正数")
elif x < 0:
    print("x 是负数")
else:
    print("x 是零")
```

### 4. 条件表达式（三元运算符）

```python
x = 10
result = "正数" if x > 0 else "负数或零"
print(result)
```

### 5. 比较运算符

```python
==  # 等于
!=  # 不等于
>   # 大于
<   # 小于
>=  # 大于等于
<=  # 小于等于
```

### 6. 逻辑运算符

```python
and  # 与
or   # 或
not  # 非
```

### 7. 成员运算符

```python
in      # 在...中
not in  # 不在...中
```

### 8. 身份运算符

```python
is      # 是同一个对象
is not  # 不是同一个对象
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- if、if-else、if-elif-else 语句
- 条件表达式
- 比较运算符和逻辑运算符
- 成员运算符和身份运算符

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
