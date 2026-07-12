# 第一个Python程序

## 学习目标

- 了解 Python 语言的特点和应用领域
- 掌握 Python 环境的安装和配置
- 编写并运行第一个 Python 程序
- 了解 Python 解释器的基本使用

## 知识点

### 1. Python 简介

Python 是一种高级、解释型、通用的编程语言，由 Guido van Rossum 于 1991 年创建。

**Python 的特点：**
- 语法简洁清晰，易于学习
- 跨平台，支持 Windows、Mac、Linux
- 丰富的标准库和第三方库
- 支持多种编程范式：面向对象、函数式、过程式

**Python 的应用领域：**
- Web 开发（Django、Flask）
- 数据科学和人工智能（NumPy、Pandas、TensorFlow）
- 自动化脚本
- 系统运维
- 游戏开发

### 2. 安装 Python

**Windows 安装：**
1. 访问 https://www.python.org/downloads/
2. 下载最新版本的 Python 安装包
3. 运行安装程序，勾选 "Add Python to PATH"
4. 点击 "Install Now" 完成安装

**验证安装：**
```bash
python --version
```

### 3. Python 解释器

Python 解释器是执行 Python 代码的程序。

**交互模式：**
```bash
python
>>> print("Hello, World!")
Hello, World!
>>> exit()
```

**脚本模式：**
创建文件 `hello.py`：
```python
print("Hello, World!")
```

运行脚本：
```bash
python hello.py
```

### 4. 第一个 Python 程序

```python
# 这是我的第一个 Python 程序
print("Hello, World!")
print("你好，Python！")
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 如何使用 print() 函数输出文本
- 如何使用注释
- Python 代码的基本格式

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
- Python 官方文档：https://docs.python.org/3/
