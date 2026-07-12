# 循环

## 学习目标

- 掌握 for 循环的语法和使用
- 掌握 while 循环的语法和使用
- 了解 break、continue 和 else 的用法
- 掌握循环嵌套

## 知识点

### 1. for 循环

```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "Hello":
    print(char)

# 使用 range()
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### 2. while 循环

```python
# 基本 while 循环
count = 0
while count < 5:
    print(count)
    count += 1

# 无限循环
while True:
    user_input = input("输入 'quit' 退出: ")
    if user_input == 'quit':
        break
```

### 3. break 语句

```python
# 跳出循环
for i in range(10):
    if i == 5:
        break
    print(i)
```

### 4. continue 语句

```python
# 跳过当前迭代
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### 5. else 子句

```python
# 循环正常结束时执行
for i in range(5):
    print(i)
else:
    print("循环结束")

# break 跳出时不执行
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("这行不会执行")
```

### 6. 循环嵌套

```python
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()
```

### 7. 列表推导式

```python
# 基本语法
squares = [x**2 for x in range(10)]

# 带条件
even = [x for x in range(10) if x % 2 == 0]

# 嵌套
matrix = [[i * j for j in range(5)] for i in range(5)]
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- for 循环和 while 循环
- break、continue 和 else 的用法
- 循环嵌套
- 列表推导式

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
