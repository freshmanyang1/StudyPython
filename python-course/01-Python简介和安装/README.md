# Python简介和安装

## 学习目标

- 了解什么是 Python
- 了解 Python 的应用领域
- 掌握 Python 的安装方法
- 了解 Python 执行文件的方式

## 知识点

### 1. 什么是 Python

Python 是一种高级、解释型、通用的编程语言，由 Guido van Rossum 于 1991 年创建。

**Python 的特点**：
- 语法简洁清晰，易于学习
- 跨平台，支持 Windows、Mac、Linux
- 丰富的标准库和第三方库
- 支持多种编程范式：面向对象、函数式、过程式

### 2. Python 的应用领域

- **Web 开发**：Django、Flask
- **数据科学和人工智能**：NumPy、Pandas、TensorFlow
- **自动化脚本**：系统运维、文件处理
- **游戏开发**：Pygame
- **网络爬虫**：Scrapy、BeautifulSoup

### 3. 安装 Python

**Windows 安装**：
1. 访问 https://www.python.org/downloads/
2. 下载最新版本的 Python 安装包
3. 运行安装程序，**勾选 "Add Python to PATH"**
4. 点击 "Install Now" 完成安装

**验证安装**：
```bash
python --version
```

如果显示 Python 版本号，说明安装成功。

### 4. Python 执行文件的方式

**方式一：交互模式**

直接在命令行输入 `python` 进入交互模式：
```bash
python
>>> print("Hello, World!")
Hello, World!
>>> exit()
```

**方式二：脚本模式**

创建一个 `.py` 文件，然后用 `python` 命令执行：
```bash
# 创建文件 hello.py
# 内容：print("Hello, World!")

python hello.py
```

**区别**：
- 交互模式：适合测试小段代码，退出后代码丢失
- 脚本模式：适合编写完整程序，代码保存在文件中

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- Python 的基本输出
- 如何执行 Python 文件

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
- Python 官方文档：https://docs.python.org/3/
