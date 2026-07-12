# 切片操作

## 学习目标

- 掌握列表切片的使用
- 了解字符串切片的使用
- 掌握元组切片的使用
- 了解切片赋值

## 知识点

### 1. 列表切片

```python
lst = [0, 1, 2, 3, 4, 5]
lst[1:4]    # [1, 2, 3]
lst[:3]     # [0, 1, 2]
lst[3:]     # [3, 4, 5]
lst[::2]    # [0, 2, 4]
lst[::-1]   # [5, 4, 3, 2, 1, 0]
```

### 2. 字符串切片

```python
s = "Hello World"
s[0:5]      # "Hello"
s[6:]       # "World"
s[::-1]     # "dlroW olleH"
```

### 3. 元组切片

```python
t = (1, 2, 3, 4, 5)
t[1:3]      # (2, 3)
```

### 4. 切片赋值

```python
lst = [1, 2, 3, 4, 5]
lst[1:3] = [20, 30]
print(lst)  # [1, 20, 30, 4, 5]
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 列表切片
- 字符串切片
- 元组切片
- 切片赋值

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
