# -*- coding: utf-8 -*-
"""
课程：继承
演示：继承概念、基本继承、super()、方法重写
"""

# 1. 基本继承
print("=== 基本继承 ===")
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

# 2. super() 函数
print("\n=== super() 函数 ===")
class Animal2:
    def __init__(self, name):
        self.name = name

class Dog2(Animal2):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog2("Buddy", "Golden Retriever")
print(f"姓名: {dog.name}")
print(f"品种: {dog.breed}")

# 3. 方法重写
print("\n=== 方法重写 ===")
class Animal3:
    def speak(self):
        return "..."

class Dog3(Animal3):
    def speak(self):
        return "Woof!"

dog = Dog3()
print(f"dog.speak() = {dog.speak()}")

# 4. isinstance 函数
print("\n=== isinstance 函数 ===")
print(f"isinstance(dog, Dog3) = {isinstance(dog, Dog3)}")
print(f"isinstance(dog, Animal3) = {isinstance(dog, Animal3)}")
