# 集合set

## 学习目标

- 掌握集合的创建方法
- 了解集合的常用操作
- 掌握集合的运算
- 了解集合的常用方法

## 知识点

### 1. 集合的创建

集合是无序的不重复元素集合，用花括号 `{}` 或 `set()` 表示。

```python
# 创建集合
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4, 5])

# 空集合（不能用 {}，那是空字典）
empty = set()
```

### 2. 集合的常用操作

```python
fruits = {"apple", "banana", "cherry"}

# 添加元素
fruits.add("grape")

# 删除元素
fruits.remove("banana")     # 删除指定元素（不存在会报错）
fruits.discard("xxx")       # 删除指定元素（不存在不会报错）
fruits.pop()                # 删除任意元素
fruits.clear()                     # 清空所有元素
fruits.difference_update({...})    # 一次删除多个元素
del fruits                         # 删除整个集合变量
```

### 3. 集合的运算

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 并集
print(set1 | set2)  # {1, 2, 3, 4, 5}
print(set1.union(set2))

# 交集
print(set1 & set2)  # {3}
print(set1.intersection(set2))

# 差集
print(set1 - set2)  # {1, 2}
print(set1.difference(set2))

# 对称差集
print(set1 ^ set2)  # {1, 2, 4, 5}
print(set1.symmetric_difference(set2))
```

### 4. 集合的常用方法

```python
fruits = {"apple", "banana", "cherry"}

len(fruits)           # 3 - 长度
fruits.add("grape")   # 添加
fruits.remove("apple")# 删除
fruits.discard("xxx") # 删除（不报错）
```

### 5. 集合的特点

- 无序：元素没有顺序
- 不重复：自动去除重复元素
- 可哈希：元素必须是不可变类型

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 集合的创建和操作
- 集合的运算
- 集合的常用方法

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
