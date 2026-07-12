# -*- coding: utf-8 -*-
"""
课程：模块基础
演示：import 语句、from...import、模块搜索路径、包
"""

# 1. import 语句
print("=== import 语句 ===")
import math
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.pi = {math.pi}")

# 2. import 并重命名
print("\n=== import 并重命名 ===")
import math as m
print(f"m.sqrt(16) = {m.sqrt(16)}")

# 3. from...import 语句
print("\n=== from...import 语句 ===")
from math import sqrt, pi
print(f"sqrt(16) = {sqrt(16)}")
print(f"pi = {pi}")

# 4. 模块搜索路径
print("\n=== 模块搜索路径 ===")
import sys
print(f"Python 路径: {sys.path[:3]}...")

# 5. 常用模块
print("\n=== 常用模块 ===")
import os
print(f"当前目录: {os.getcwd()}")

from datetime import datetime
now = datetime.now()
print(f"当前时间: {now}")

import json
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data, ensure_ascii=False)
print(f"JSON: {json_str}")
