# 面向对象编程

## 学习目标

- 理解面向对象编程的概念
- 掌握类的定义和使用
- 了解实例属性和类属性
- 掌握继承和多态

## 知识点

### 1. 类的定义

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

p = Person("Alice", 25)
p.greet()
```

### 2. 实例属性

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age

p = Person("Alice", 25)
print(p.name)  # Alice
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

### 4. 方法

```python
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

calc = Calculator()
print(calc.add(3, 5))  # 8
```

### 5. 继承

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

dog = Dog("Buddy")
print(dog.speak())  # Woof!
```

### 6. 多态

```python
def make_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Kitty")
make_sound(dog)  # Woof!
make_sound(cat)  # Meow!
```

### 7. super() 函数

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

### 8. isinstance 函数

```python
dog = Dog("Buddy", "Golden Retriever")
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 类的定义和使用
- 实例属性和类属性
- 继承和多态
- super() 函数和 isinstance 函数

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
