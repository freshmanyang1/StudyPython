# -*- coding: utf-8 -*-
"""
课程：类和对象
作业要求：
1. 定义一个 Student 类，包含姓名和年龄属性
2. 定义一个 introduce 方法，输出自我介绍
3. 创建两个 Student 实例并调用 introduce 方法

完成后输入 `python，提交作业` 提交。
"""

# 作业1：定义 Student 类
# 请在此处填写代码
class Student:
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - Student 类:")
    s1 = Student("Alice", 20)
    s2 = Student("Bob", 22)
    print(f"s1: {s1.name}, {s1.age}")
    print(f"s2: {s2.name}, {s2.age}")
    print("\n测试作业2 - introduce 方法:")
    s1.introduce()
    s2.introduce()
