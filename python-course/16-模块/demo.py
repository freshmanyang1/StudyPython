# -*- coding: utf-8 -*-
"""
课程：模块
演示：模块导入、包、标准库
"""

# 1. 导入整个模块
print("=== 导入整个模块 ===")
import math
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.pi = {math.pi}")

# 2. 导入特定函数
print("\n=== 导入特定函数 ===")
from math import sqrt, pi
print(f"sqrt(16) = {sqrt(16)}")
print(f"pi = {pi}")

# 3. 导入并重命名
print("\n=== 导入并重命名 ===")
import math as m
print(f"m.sqrt(16) = {m.sqrt(16)}")

# 4. 模块搜索路径
print("\n=== 模块搜索路径 ===")
import sys
print(f"Python 路径: {sys.path[:3]}...")

# 5. os 模块
print("\n=== os 模块 ===")
import os
print(f"当前目录: {os.getcwd()}")
print(f"目录内容: {os.listdir('.')[:5]}...")

# 6. datetime 模块
print("\n=== datetime 模块 ===")
from datetime import datetime, timedelta
now = datetime.now()
print(f"当前时间: {now}")
tomorrow = now + timedelta(days=1)
print(f"明天: {tomorrow}")

# 7. json 模块
print("\n=== json 模块 ===")
import json

# 序列化
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data, ensure_ascii=False)
print(f"序列化: {json_str}")

# 反序列化
data = json.loads(json_str)
print(f"反序列化: {data}")

# 8. random 模块
print("\n=== random 模块 ===")
import random
print(f"随机整数: {random.randint(1, 100)}")
print(f"随机浮点数: {random.random()}")
print(f"随机选择: {random.choice(['apple', 'banana', 'cherry'])}")

# 9. collections 模块
print("\n=== collections 模块 ===")
from collections import Counter, defaultdict

# Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(f"Counter: {counter}")

# defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
print(f"defaultdict: {dict(dd)}")

# 10. itertools 模块
print("\n=== itertools 模块 ===")
import itertools

# 排列组合
print(f"排列: {list(itertools.permutations('ABC', 2))}")
print(f"组合: {list(itertools.combinations('ABC', 2))}")

# 链接
print(f"链: {list(itertools.chain([1, 2], [3, 4], [5, 6]))}")
