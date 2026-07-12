# 文件读写

## 学习目标

- 掌握 open() 函数的使用
- 了解 read()、write() 方法
- 掌握 with 语句的使用

## 知识点

### 1. open() 函数

```python
# 打开文件
f = open('test.txt', 'r')  # 读取模式
f = open('test.txt', 'w')  # 写入模式
f = open('test.txt', 'a')  # 追加模式
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

### 3. read() 方法

```python
with open('test.txt', 'r') as f:
    content = f.read()      # 读取全部内容
    lines = f.readlines()   # 读取所有行
    line = f.readline()     # 读取一行
```

### 4. write() 方法

```python
with open('test.txt', 'w') as f:
    f.write('Hello, World!')
```

### 5. with 语句

```python
# 使用 with 语句自动关闭文件
with open('test.txt', 'r') as f:
    content = f.read()
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- open() 函数
- read()、write() 方法
- with 语句

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
