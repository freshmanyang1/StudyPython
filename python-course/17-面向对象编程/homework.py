# -*- coding: utf-8 -*-
"""
课程：面向对象编程
作业要求：
1. 定义一个 Rectangle 类，包含长和宽属性，以及计算面积和周长的方法
2. 定义一个 Circle 类，包含半径属性，以及计算面积和周长的方法
3. 定义一个 Animal 基类，以及 Dog 和 Cat 子类，实现多态
4. 定义一个 BankAccount 类，包含存款、取款和查询余额的方法

完成后输入 `python，提交作业` 提交。
"""

import math

# 作业1：Rectangle 类
# 请在此处填写代码
class Rectangle:
    pass

# 作业2：Circle 类
# 请在此处填写代码
class Circle:
    pass

# 作业3：Animal 类
# 请在此处填写代码
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 作业4：BankAccount 类
# 请在此处填写代码
class BankAccount:
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - Rectangle:")
    rect = Rectangle(5, 3)
    print(f"面积: {rect.area()}")
    print(f"周长: {rect.perimeter()}")

    print("\n测试作业2 - Circle:")
    circle = Circle(5)
    print(f"面积: {circle.area():.2f}")
    print(f"周长: {circle.perimeter():.2f}")

    print("\n测试作业3 - Animal:")
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(f"{dog.name}: {dog.speak()}")
    print(f"{cat.name}: {cat.speak()}")

    print("\n测试作业4 - BankAccount:")
    account = BankAccount("Alice", 1000)
    print(f"余额: {account.balance}")
    account.deposit(500)
    print(f"存款后: {account.balance}")
    account.withdraw(200)
    print(f"取款后: {account.balance}")
