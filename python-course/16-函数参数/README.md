# 函数参数

## 学习目标

- 掌握位置参数的使用
- 了解默认参数的使用
- 掌握关键字参数的使用
- 了解可变参数 *args 和 **kwargs

## 知识点

### 1. 位置参数

```python
def greet(name, age):
    print(f"姓名: {name}, 年龄: {age}")

greet("Alice", 25)  # 位置参数
```

### 2. 默认参数

```python
def greet(name, age=18):
    print(f"姓名: {name}, 年龄: {age}")

greet("Alice")        # 使用默认值
greet("Bob", 25)      # 覆盖默认值
```

### 3. 关键字参数

```python
def greet(name, age):
    print(f"姓名: {name}, 年龄: {age}")

greet(age=25, name="Alice")  # 关键字参数
```

### 4. 可变参数 *args

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))      # 6
print(sum_numbers(1, 2, 3, 4, 5)) # 15
```

### 5. 关键字可变参数 **kwargs

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Beijing")
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 位置参数
- 默认参数
- 关键字参数
- 可变参数 *args 和 **kwargs

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
