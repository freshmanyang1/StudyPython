# 常用标准库

## 学习目标

- 掌握 os 模块的使用
- 了解 datetime 模块的使用
- 掌握 json 模块的使用
- 了解 random 模块的使用

## 知识点

### 1. os 模块

```python
import os

os.getcwd()          # 获取当前目录
os.listdir()         # 列出目录内容
os.makedirs('dir')   # 创建目录
os.path.exists()     # 检查路径是否存在
```

### 2. datetime 模块

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)

tomorrow = now + timedelta(days=1)
print(tomorrow)
```

### 3. json 模块

```python
import json

# 序列化
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)

# 反序列化
data = json.loads(json_str)
```

### 4. random 模块

```python
import random

random.randint(1, 100)    # 随机整数
random.random()           # 随机浮点数
random.choice(['a', 'b']) # 随机选择
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- os 模块
- datetime 模块
- json 模块
- random 模块

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
