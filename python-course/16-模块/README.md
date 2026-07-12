# 模块

## 学习目标

- 理解模块的概念
- 掌握模块的导入方式
- 了解包的概念和使用
- 掌握常用标准库模块

## 知识点

### 1. 模块的概念

模块是一个包含 Python 代码的文件。

```python
# math.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```

### 2. 导入模块

```python
# 导入整个模块
import math
print(math.sqrt(16))  # 4.0

# 导入特定函数
from math import sqrt
print(sqrt(16))  # 4.0

# 导入并重命名
import math as m
print(m.sqrt(16))  # 4.0

# 导入所有（不推荐）
from math import *
```

### 3. 模块搜索路径

```python
import sys
print(sys.path)
```

### 4. 包

包是包含 `__init__.py` 文件的目录。

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

```python
from mypackage import module1
from mypackage.module2 import func
```

### 5. 常用标准库

```python
import os
import sys
import math
import random
import datetime
import json
import re
```

### 6. os 模块

```python
import os

os.getcwd()          # 获取当前目录
os.listdir()         # 列出目录内容
os.makedirs('dir')   # 创建目录
os.path.exists()     # 检查路径是否存在
```

### 7. datetime 模块

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)

tomorrow = now + timedelta(days=1)
print(tomorrow)
```

### 8. json 模块

```python
import json

# 序列化
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)

# 反序列化
data = json.loads(json_str)
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 模块的导入方式
- 包的概念和使用
- 常用标准库模块

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
