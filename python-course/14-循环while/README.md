# 循环while

## 学习目标

- 掌握 while 循环的语法
- 了解 break 和 continue 语句
- 掌握 while-else 语句
- 了解无限循环和退出

## 知识点

### 1. while 循环

```python
# 基本 while 循环
count = 0
while count < 5:
    print(count)
    count += 1
```

### 2. break 语句

```python
# 跳出循环
for i in range(10):
    if i == 5:
        break
    print(i)
```

### 3. continue 语句

```python
# 跳过当前迭代
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### 4. while-else 语句

```python
# 循环正常结束时执行
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("循环结束")
```

### 5. 无限循环

```python
# 无限循环（需要 break 退出）
while True:
    user_input = input("输入 'quit' 退出: ")
    if user_input == 'quit':
        break
    print(f"你输入了: {user_input}")
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- while 循环
- break 和 continue 语句
- while-else 语句
- 无限循环

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
