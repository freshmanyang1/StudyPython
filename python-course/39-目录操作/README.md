# 目录操作

## 学习目标

- 掌握 os.makedirs() 的使用
- 了解 os.listdir() 的使用
- 掌握遍历目录的方法

## 知识点

### 1. 创建目录

```python
import os

# 创建目录
os.makedirs('test/dir')

# 创建目录（如果存在不报错）
os.makedirs('test/dir', exist_ok=True)
```

### 2. 列出目录

```python
import os

# 列出目录内容
files = os.listdir('.')
print(files)
```

### 3. 遍历目录

```python
from pathlib import Path

# 遍历目录
for p in Path('.').iterdir():
    print(p)
```

### 4. 查找文件

```python
from pathlib import Path

# 查找文件
for p in Path('.').glob('*.py'):
    print(p)
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 创建目录
- 列出目录
- 遍历目录
- 查找文件

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
