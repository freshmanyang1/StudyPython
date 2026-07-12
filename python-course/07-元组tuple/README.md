# 元组tuple

## 学习目标

- 掌握元组的创建方法
- 了解元组的访问方式
- 理解元组与列表的区别
- 掌握元组的常用方法

## 知识点

### 1. 元组的创建

元组是有序的不可变序列，用圆括号 `()` 表示。

```python
# 创建元组
point = (1, 2)
colors = ("red", "green", "blue")

# 单元素元组需要逗号
single = (1,)  # 正确
not_tuple = (1)  # 这是整数，不是元组

# 空元组
empty = ()
```

### 2. 元组的访问

```python
point = (1, 2, 3)

# 正向索引
print(point[0])    # 1
print(point[1])    # 2

# 反向索引
print(point[-1])   # 3
print(point[-2])   # 2

# 切片
print(point[1:])   # (2, 3)
print(point[:2])   # (1, 2)
```

### 3. 元组与列表的区别

| 特性 | 列表 | 元组 |
|---|---|---|
| 可变性 | 可变 | 不变 |
| 语法 | [] | () |
| 性能 | 较慢 | 较快 |
| 用途 | 动态集合 | 固定数据 |

```python
# 列表是可变的
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # [10, 2, 3]

# 元组是不可变的
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"元组修改失败: {e}")
```

### 4. 元组的常用方法

```python
point = (1, 2, 3)

len(point)           # 3 - 长度
point.count(1)       # 1 - 统计出现次数
point.index(2)       # 1 - 查找索引
```

### 5. 元组的遍历

```python
point = (1, 2, 3)

# for 循环遍历
for x in point:
    print(x)

# 带索引遍历
for i, x in enumerate(point):
    print(f"{i}: {x}")
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 元组的创建和访问
- 元组与列表的区别
- 元组的常用方法
- 元组的遍历

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
