# -*- coding: utf-8 -*-
"""
课程：生成器
演示：生成器概念、yield、生成器表达式
"""

# 1. 生成器函数
print("=== 生成器函数 ===")
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("countdown(5):")
for i in countdown(5):
    print(i, end=" ")
print()

# 2. 生成器表达式
print("\n=== 生成器表达式 ===")
squares_gen = (x**2 for x in range(10))
print(f"type(squares_gen) = {type(squares_gen)}")
print(f"list(squares_gen) = {list(squares_gen)}")

# 3. 斐波那契生成器
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

# 4. 生成器的优势
print("\n=== 生成器的优势 ===")
# 列表生成式（占用内存）
squares_list = [x**2 for x in range(1000000)]

# 生成器表达式（不占用内存）
squares_gen = (x**2 for x in range(1000000))

print(f"列表大小: {len(squares_list)}")
print(f"生成器大小: {sys.getsizeof(squares_gen)} 字节")
