# 列表list

## 学习目标

- 掌握列表的创建方法
- 了解列表的访问和修改
- 掌握列表的常用方法
- 了解列表的切片操作

## 知识点

### 1. 列表的创建

列表是有序的可变序列，用方括号 `[]` 表示。

```python
# 创建列表
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# 空列表
empty = []
```

### 2. 列表的访问

```python
fruits = ["apple", "banana", "cherry"]

# 正向索引（从 0 开始）
print(fruits[0])    # "apple"
print(fruits[1])    # "banana"

# 反向索引（从 -1 开始）
print(fruits[-1])   # "cherry"
print(fruits[-2])   # "banana"
```

### 3. 列表的修改

```python
fruits = ["apple", "banana", "cherry"]

# 修改元素
fruits[0] = "orange"
print(fruits)  # ["orange", "banana", "cherry"]

# 添加元素
fruits.append("grape")      # 末尾添加
fruits.insert(1, "mango")   # 指定位置添加

# 删除元素
fruits.remove("banana")     # 删除指定元素
fruits.pop()                # 删除末尾元素
del fruits[0]               # 删除指定位置元素
```

### 4. 列表的常用方法

```python
fruits = ["apple", "banana", "cherry"]

len(fruits)           # 3 - 长度
fruits.count("apple") # 1 - 统计出现次数
fruits.index("banana")# 1 - 查找索引
fruits.sort()         # 排序
fruits.reverse()      # 反转
fruits.copy()         # 复制
```

### 5. 列表的切片

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3]    # [2, 3]
numbers[:3]     # [1, 2, 3]
numbers[2:]     # [3, 4, 5]
numbers[::2]    # [1, 3, 5]
numbers[::-1]   # [5, 4, 3, 2, 1]
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 列表的创建和访问
- 列表的修改和删除
- 列表的常用方法
- 列表的切片操作

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
