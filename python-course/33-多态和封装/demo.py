# -*- coding: utf-8 -*-
"""
课程：多态和封装
演示：多态概念、多态使用、封装概念、访问控制
"""

# 1. 多态
print("=== 多态 ===")
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Kitty")
make_sound(dog)
make_sound(cat)

# 2. 封装
print("\n=== 封装 ===")
class Person:
    def __init__(self, name, age):
        self.name = name      # 公有属性
        self._age = age       # 受保护属性
        self.__secret = "xxx" # 私有属性

    def get_age(self):
        return self._age

p = Person("Alice", 25)
print(f"姓名: {p.name}")
print(f"年龄: {p.get_age()}")
# print(p.__secret)  # 错误：无法访问私有属性
