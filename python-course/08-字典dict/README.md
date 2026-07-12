# 字典dict

## 学习目标

- 掌握字典的创建方法
- 了解字典的访问和修改
- 掌握字典的常用方法
- 了解字典推导式

## 知识点

### 1. 字典的创建

字典是无序的键值对集合，用花括号 `{}` 表示。

```python
# 创建字典
student = {
    "name": "Alice",
    "age": 25,
    "city": "Beijing"
}

# 空字典
empty = {}
```

### 2. 字典的访问

```python
student = {
    "name": "Alice",
    "age": 25,
    "city": "Beijing"
}

# 访问元素
print(student["name"])    # "Alice"
print(student.get("age")) # 25

# 访问不存在的键
print(student.get("email", "N/A"))  # "N/A"（默认值）
```

### 3. 字典的修改

```python
student = {
    "name": "Alice",
    "age": 25
}

# 添加/修改元素
student["email"] = "alice@example.com"
student["age"] = 26

# 删除元素
del student["email"]
student.pop("city")

# 检查键是否存在
print("name" in student)  # True
```

### 4. 字典的常用方法

```python
student = {
    "name": "Alice",
    "age": 25
}

student.keys()    # 获取所有键
student.values()  # 获取所有值
student.items()   # 获取所有键值对
student.update({"city": "Beijing"})  # 更新字典
```

### 5. 字典推导式

```python
# 基本语法
squares = {x: x**2 for x in range(10)}

# 带条件
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 字典的创建和访问
- 字典的修改和删除
- 字典的常用方法
- 字典推导式

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
