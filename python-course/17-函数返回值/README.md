# 函数返回值

## 学习目标

- 掌握 return 语句的使用
- 了解返回多个值的方法
- 理解返回 None 的情况

## 知识点

### 1. return 语句

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

### 2. 返回多个值

```python
def get_info():
    return "Alice", 25

name, age = get_info()
print(f"姓名: {name}, 年龄: {age}")
```

### 3. 返回 None

```python
def greet(name):
    print(f"Hello, {name}!")
    # 没有 return 语句，返回 None

result = greet("Alice")
print(result)  # None
```

### 4. 提前返回

```python
def check_age(age):
    if age < 0:
        return "年龄无效"
    if age < 18:
        return "未成年"
    return "成年"
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- return 语句
- 返回多个值
- 返回 None
- 提前返回

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
