# -*- coding: utf-8 -*-
"""
课程：常用标准库
演示：os、datetime、json、random 模块
"""

# 1. os 模块
print("=== os 模块 ===")
import os
print(f"当前目录: {os.getcwd()}")
print(f"目录内容: {os.listdir('.')[:5]}...")

# 2. datetime 模块
print("\n=== datetime 模块 ===")
from datetime import datetime, timedelta
now = datetime.now()
print(f"当前时间: {now}")
tomorrow = now + timedelta(days=1)
print(f"明天: {tomorrow}")

# 3. json 模块
print("\n=== json 模块 ===")
import json

# 序列化
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data, ensure_ascii=False)
print(f"序列化: {json_str}")

# 反序列化
data = json.loads(json_str)
print(f"反序列化: {data}")

# 4. random 模块
print("\n=== random 模块 ===")
import random
print(f"随机整数: {random.randint(1, 100)}")
print(f"随机浮点数: {random.random()}")
print(f"随机选择: {random.choice(['apple', 'banana', 'cherry'])}")
