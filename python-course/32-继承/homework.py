# -*- coding: utf-8 -*-
"""
课程：继承
作业要求：
1. 定义一个 Animal 基类，包含 name 属性和 speak 方法
2. 定义 Dog 和 Cat 子类，重写 speak 方法
3. 创建实例并调用 speak 方法

完成后输入 `python，提交作业` 提交。
"""

# 作业1：定义 Animal 基类
# 请在此处填写代码
class Animal:
    pass

# 作业2：定义 Dog 子类
# 请在此处填写代码
class Dog(Animal):
    pass

# 作业3：定义 Cat 子类
# 请在此处填写代码
class Cat(Animal):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - Animal 基类:")
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(f"dog.name = {dog.name}")
    print(f"cat.name = {cat.name}")
    print("\n测试作业2 - speak 方法:")
    print(f"dog.speak() = {dog.speak()}")
    print(f"cat.speak() = {cat.speak()}")
