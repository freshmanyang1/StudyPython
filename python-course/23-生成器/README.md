# 生成器

## 学习目标

- 理解生成器的概念
- 掌握 yield 关键字的使用
- 了解生成器表达式

## 知识点

### 1. 生成器的概念

生成器是一种特殊的迭代器，使用 yield 关键字。

### 2. yield 关键字

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
```

### 3. 生成器表达式

```python
# 列表生成式
squares_list = [x**2 for x in range(10)]

# 生成器表达式
squares_gen = (x**2 for x in range(10))
```

### 4. 生成器的优势

- 节省内存：惰性计算，按需生成
- 无限序列：可以表示无限序列

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 生成器的概念
- yield 关键字
- 生成器表达式

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
