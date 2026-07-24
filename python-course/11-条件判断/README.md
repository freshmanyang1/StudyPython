# 条件判断

## 学习目标

- 掌握 if 语句的语法
- 了解 if-else 和 if-elif-else 结构
- 掌握条件表达式（三元运算符）
- 理解条件判断的嵌套

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
if x > 0:                                       # 如果
    print("x 是正数")               
elif x < 0:                                    #否则如果  语法可以出现多个elif
    print("x 是负数")
else:                                           #否则
    print("x 是零")
```

### 4. 条件表达式（三元运算符）

```python
x = 10
result = "正数" if x > 0 else "负数或零"
print(result)
```

### 5. 嵌套条件

```python
x = 15
if x > 0:
    if x > 10:
        print("x 是大于10的正数")
    else:
        print("x 是小于等于10的正数")
else:
    print("x 是负数或零")
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- if 语句
- if-else 语句
- if-elif-else 语句
- 条件表达式
- 嵌套条件

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
