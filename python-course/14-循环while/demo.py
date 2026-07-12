# -*- coding: utf-8 -*-
"""
课程：循环while
演示：while 循环、break、continue、while-else、无限循环
"""

# 1. while 循环
print("=== while 循环 ===")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# 2. break 语句
print("\n=== break 语句 ===")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# 3. continue 语句
print("\n=== continue 语句 ===")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 4. while-else 语句
print("\n=== while-else 语句 ===")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
else:
    print("\n循环结束")

# 5. 无限循环（示例，不会实际运行）
print("\n=== 无限循环示例 ===")
print("while True:")
print("    user_input = input('输入 quit 退出: ')")
print("    if user_input == 'quit':")
print("        break")
