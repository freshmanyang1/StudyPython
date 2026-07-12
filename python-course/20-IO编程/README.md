# IO编程

## 学习目标

- 掌握文件读写操作
- 了解文件路径处理
- 掌握目录操作
- 了解文件和目录的常用方法

## 知识点

### 1. 文件读写

```python
# 写入文件
with open('test.txt', 'w') as f:
    f.write('Hello, World!')

# 读取文件
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)
```

### 2. 文件模式

```python
'r'   # 读取（默认）
'w'   # 写入（覆盖）
'a'   # 追加
'r+'  # 读写
'rb'  # 二进制读取
'wb'  # 二进制写入
```

### 3. 逐行读取

```python
with open('test.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

### 4. 文件路径

```python
from pathlib import Path

# 创建路径
p = Path('test.txt')
print(p.exists())     # 检查是否存在
print(p.is_file())    # 是否是文件
print(p.is_dir())     # 是否是目录
print(p.name)         # 文件名
print(p.suffix)       # 扩展名
print(p.parent)       # 父目录
```

### 5. 目录操作

```python
import os

# 创建目录
os.makedirs('test/dir')

# 列出目录
files = os.listdir('.')

# 删除文件
os.remove('test.txt')

# 删除目录
os.rmdir('test/dir')
```

### 6. pathlib 模块

```python
from pathlib import Path

# 创建目录
Path('test/dir').mkdir(parents=True, exist_ok=True)

# 遍历目录
for p in Path('.').iterdir():
    print(p)

# 查找文件
for p in Path('.').glob('*.py'):
    print(p)
```

### 7. 文件信息

```python
import os

# 文件大小
size = os.path.getsize('test.txt')

# 修改时间
mtime = os.path.getmtime('test.txt')

# 绝对路径
abs_path = os.path.abspath('test.txt')
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 文件读写操作
- 文件路径处理
- 目录操作
- pathlib 模块的使用

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
