# 模块基础

## 学习目标

- 掌握 import 语句的使用
- 了解 from...import 语句的使用
- 理解模块搜索路径
- 了解包的概念

## 知识点

### 1. import 语句

```python
# 导入整个模块
import math
print(math.sqrt(16))  # 4.0

# 导入并重命名
import math as m
print(m.sqrt(16))  # 4.0
```

### 2. from...import 语句

```python
# 导入特定函数
from math import sqrt
print(sqrt(16))  # 4.0

# 导入多个函数
from math import sqrt, pi

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

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- import 语句
- from...import 语句
- 模块搜索路径
- 包的概念

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
