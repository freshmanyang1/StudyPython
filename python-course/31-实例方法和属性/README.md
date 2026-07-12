# 实例方法和属性

## 学习目标

- 理解 self 参数的含义
- 掌握实例属性的使用
- 了解类属性的使用
- 掌握实例方法的定义

## 知识点

### 1. self 参数

```python
class Person:
    def __init__(self, name):
        self.name = name  # self 指向实例本身
    
    def greet(self):
        print(f"Hello, {self.name}")
```

### 2. 实例属性

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

p = Person("Alice", 25)
print(p.name)  # "Alice"
print(p.age)   # 25
```

### 3. 类属性

```python
class Person:
    count = 0  # 类属性
    
    def __init__(self, name):
        self.name = name
        Person.count += 1

p1 = Person("Alice")
p2 = Person("Bob")
print(Person.count)  # 2
```

### 4. 实例方法

```python
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

calc = Calculator()
print(calc.add(3, 5))  # 8
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- self 参数
- 实例属性
- 类属性
- 实例方法

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
