# -*- coding: utf-8 -*-
"""
课程：列表生成式和生成器
演示：列表生成式、生成器、yield
"""

# 1. 列表生成式
print("=== 列表生成式 ===")
squares = [x**2 for x in range(10)]
print(f"squares = {squares}")

# 2. 带条件的列表生成式
print("\n=== 带条件的列表生成式 ===")
even = [x for x in range(10) if x % 2 == 0]
print(f"even = {even}")

# 3. 嵌套列表生成式
print("\n=== 嵌套列表生成式 ===")
matrix = [[i * j for j in range(5)] for i in range(5)]
for row in matrix:
    print(row)

# 4. 字符串处理
print("\n=== 字符串处理 ===")
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"upper_words = {upper_words}")

# 5. 字典生成
print("\n=== 字典生成 ===")
squares_dict = {x: x**2 for x in range(10)}
print(f"squares_dict = {squares_dict}")

# 6. 集合生成
print("\n=== 集合生成 ===")
unique_lengths = {len(word) for word in words}
print(f"unique_lengths = {unique_lengths}")

# 7. 生成器
print("\n=== 生成器 ===")
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("countdown(5):")
for i in countdown(5):
    print(i, end=" ")
print()

# 8. 生成器表达式
print("\n=== 生成器表达式 ===")
squares_gen = (x**2 for x in range(10))
print(f"type(squares_gen) = {type(squares_gen)}")
print(f"list(squares_gen) = {list(squares_gen)}")

# 9. 斐波那契生成器
print("\n=== 斐波那契生成器 ===")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print("前10个斐波那契数:")
for _ in range(10):
    print(next(fib), end=" ")
print()

# 10. send 方法
print("\n=== send 方法 ===")
def counter():
    n = 0
    while True:
        n += 1
        received = yield n
        if received is not None:
            n = received

c = counter()
print(f"next(c) = {next(c)}")
print(f"next(c) = {next(c)}")
print(f"c.send(10) = {c.send(10)}")
print(f"next(c) = {next(c)}")

# 11. 生成器管道
print("\n=== 生成器管道 ===")
def numbers():
    for i in range(10):
        yield i

def square(nums):
    for n in nums:
        yield n ** 2

def even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

result = list(even(square(numbers())))
print(f"result = {result}")
