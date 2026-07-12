# 文件路径

## 学习目标

- 掌握 os.path 模块的使用
- 了解 pathlib 模块的使用
- 掌握路径操作

## 知识点

### 1. os.path 模块

```python
import os.path

os.path.exists()     # 检查路径是否存在
os.path.isfile()     # 是否是文件
os.path.isdir()      # 是否是目录
os.path.basename()   # 获取文件名
os.path.dirname()    # 获取目录名
os.path.join()       # 连接路径
```

### 2. pathlib 模块

```python
from pathlib import Path

p = Path('test.txt')
p.exists()      # 检查是否存在
p.is_file()     # 是否是文件
p.is_dir()      # 是否是目录
p.name          # 文件名
p.suffix        # 扩展名
p.parent        # 父目录
```

### 3. 路径操作

```python
from pathlib import Path

# 创建路径
p = Path('test/dir')

# 连接路径
p = Path('test') / 'dir' / 'file.txt'
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- os.path 模块
- pathlib 模块
- 路径操作

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
