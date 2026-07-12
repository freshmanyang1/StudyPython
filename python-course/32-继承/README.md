# 继承

## 学习目标

- 理解继承的概念
- 掌握继承的使用方法
- 了解 super() 函数的使用
- 掌握方法重写

## 知识点

### 1. 继承的概念

继承是指子类继承父类的属性和方法。

### 2. 基本继承

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### 3. super() 函数

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的 __init__
        self.breed = breed
```

### 4. 方法重写

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):  # 重写父类方法
        return "Woof!"
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 继承的概念
- 基本继承
- super() 函数
- 方法重写

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
