# 类和对象

## 学习目标

- 理解类和对象的概念
- 掌握类的定义方法
- 了解实例化的过程
- 掌握 __init__ 方法的使用

## 知识点

### 1. 类的概念

类是对象的模板，定义了对象的属性和方法。

### 2. 定义类

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}")
```

### 3. 实例化

```python
p = Person("Alice", 25)
print(p.name)    # "Alice"
print(p.age)     # 25
p.greet()        # "Hello, my name is Alice"
```

### 4. __init__ 方法

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 类的定义
- 实例化
- __init__ 方法
- 实例属性和方法

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
