# -*- coding: utf-8 -*-
"""
课程：多态和封装
作业要求：
1. 定义一个 Shape 基类，包含 area 方法
2. 定义 Circle 和 Rectangle 子类，重写 area 方法
3. 定义一个函数 print_area，接受 Shape 对象并打印面积

完成后输入 `python，提交作业` 提交。
"""

import math

# 作业1：定义 Shape 基类
# 请在此处填写代码
class Shape:
    pass

# 作业2：定义 Circle 子类
# 请在此处填写代码
class Circle(Shape):
    pass

# 作业3：定义 Rectangle 子类
# 请在此处填写代码
class Rectangle(Shape):
    pass

# 作业4：定义 print_area 函数
# 请在此处填写代码
def print_area(shape):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - Shape 基类:")
    circle = Circle(5)
    rect = Rectangle(4, 6)
    print(f"circle.radius = {circle.radius}")
    print(f"rect.width = {rect.width}")
    print("\n测试作业2 - area 方法:")
    print(f"circle.area() = {circle.area():.2f}")
    print(f"rect.area() = {rect.area()}")
    print("\n测试作业3 - print_area 函数:")
    print_area(circle)
    print_area(rect)
