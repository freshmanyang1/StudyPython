# dict和set

## 学习目标

- 掌握字典（dict）的创建和操作
- 了解集合（set）的特点和使用
- 掌握字典和集合的常用方法
- 理解哈希表的概念

## 知识点

### 1. 字典（dict）

字典是无序的键值对集合。

```python
# 创建字典
student = {
    "name": "Alice",
    "age": 25,
    "city": "Beijing"
}

# 访问元素
print(student["name"])    # "Alice"
print(student.get("age")) # 25
```

### 2. 字典操作

```python
# 添加/修改元素
student["email"] = "alice@example.com"
student["age"] = 26

# 删除元素
del student["email"]
student.pop("city")

# 检查键是否存在
print("name" in student)  # True
```

### 3. 字典方法

```python
student = {"name": "Alice", "age": 25}

student.keys()    # 获取所有键
student.values()  # 获取所有值
student.items()   # 获取所有键值对
student.update({"city": "Beijing"})  # 更新字典
```

### 4. 字典推导式

```python
squares = {x: x**2 for x in range(10)}
```

### 5. 集合（set）

集合是无序的不重复元素集合。

```python
# 创建集合
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4, 5])
```

### 6. 集合操作

```python
# 添加元素
fruits.add("grape")

# 删除元素
fruits.remove("banana")

# 集合运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1 | set2  # 并集 {1, 2, 3, 4, 5}
set1 & set2  # 交集 {3}
set1 - set2  # 差集 {1, 2}
```

### 7. 集合方法

```python
fruits = {"apple", "banana", "cherry"}

len(fruits)           # 3
fruits.add("grape")   # 添加
fruits.remove("apple")# 删除
fruits.discard("xxx") # 删除（不报错）
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 字典的创建、访问、修改和删除
- 字典的常用方法
- 字典推导式
- 集合的创建和操作
- 集合的运算

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
