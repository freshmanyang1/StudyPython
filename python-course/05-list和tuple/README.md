# list和tuple

## 学习目标

- 掌握列表（list）的创建和操作
- 了解元组（tuple）的特点和使用
- 掌握列表和元组的常用方法
- 理解可变和不可变数据类型的区别

## 知识点

### 1. 列表（list）

列表是有序的可变序列。

```python
# 创建列表
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

### 2. 列表操作

```python
# 访问元素
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # "apple"
print(fruits[-1])   # "cherry"

# 修改元素
fruits[0] = "orange"

# 添加元素
fruits.append("grape")      # 末尾添加
fruits.insert(1, "mango")   # 指定位置添加

# 删除元素
fruits.remove("banana")     # 删除指定元素
fruits.pop()                # 删除末尾元素
del fruits[0]               # 删除指定位置元素
```

### 3. 列表切片

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3]    # [2, 3]
numbers[:3]     # [1, 2, 3]
numbers[2:]     # [3, 4, 5]
numbers[::2]    # [1, 3, 5]
numbers[::-1]   # [5, 4, 3, 2, 1]
```

### 4. 列表方法

```python
fruits = ["apple", "banana", "cherry"]

len(fruits)           # 3
fruits.count("apple") # 1
fruits.index("banana")# 1
fruits.sort()         # 排序
fruits.reverse()      # 反转
fruits.copy()         # 复制
```

### 5. 列表推导式

```python
# 基本语法
squares = [x**2 for x in range(10)]

# 带条件
even = [x for x in range(10) if x % 2 == 0]
```

### 6. 元组（tuple）

元组是有序的不可变序列。

```python
# 创建元组
point = (1, 2)
colors = ("red", "green", "blue")
single = (1,)  # 单元素元组需要逗号
```

### 7. 元组操作

```python
point = (1, 2, 3)

# 访问元素
print(point[0])    # 1
print(point[-1])   # 3

# 切片
print(point[1:])   # (2, 3)

# 长度
print(len(point))  # 3

# 遍历
for x in point:
    print(x)
```

### 8. 列表和元组的区别

| 特性 | 列表 | 元组 |
|---|---|---|
| 可变性 | 可变 | 不变 |
| 语法 | [] | () |
| 性能 | 较慢 | 较快 |
| 用途 | 动态集合 | 固定数据 |

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 列表的创建、访问、修改和删除
- 列表的切片和常用方法
- 列表推导式
- 元组的创建和操作
- 列表和元组的区别

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
