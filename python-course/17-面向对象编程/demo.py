# -*- coding: utf-8 -*-
"""
课程：面向对象编程
演示：类、继承、多态
"""

# 1. 类的定义
print("=== 类的定义 ===")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

p = Person("Alice", 25)
print(f"姓名: {p.name}")
print(f"年龄: {p.age}")
p.greet()

# 2. 类属性
print("\n=== 类属性 ===")
class Person2:
    count = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Person2.count += 1

p1 = Person2("Alice")
p2 = Person2("Bob")
print(f"Person2.count = {Person2.count}")

# 3. 方法
print("\n=== 方法 ===")
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

calc = Calculator()
print(f"add(3, 5) = {calc.add(3, 5)}")
print(f"subtract(10, 3) = {calc.subtract(10, 3)}")

# 4. 继承
print("\n=== 继承 ===")
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
cat = Cat("Kitty")
print(f"{dog.name}: {dog.speak()}")
print(f"{cat.name}: {cat.speak()}")

# 5. 多态
print("\n=== 多态 ===")
def make_sound(animal):
    print(f"{animal.name}: {animal.speak()}")

make_sound(dog)
make_sound(cat)

# 6. super() 函数
print("\n=== super() 函数 ===")
class Animal2:
    def __init__(self, name):
        self.name = name

class Dog2(Animal2):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog2 = Dog2("Buddy", "Golden Retriever")
print(f"姓名: {dog2.name}")
print(f"品种: {dog2.breed}")

# 7. isinstance 函数
print("\n=== isinstance 函数 ===")
print(f"isinstance(dog, Dog) = {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal) = {isinstance(dog, Animal)}")
print(f"isinstance(cat, Dog) = {isinstance(cat, Dog)}")

# 8. 特殊方法
print("\n=== 特殊方法 ===")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(f"p1 = {p1}")
print(f"p1 == p2 = {p1 == p2}")
