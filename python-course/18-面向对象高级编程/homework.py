# -*- coding: utf-8 -*-
"""
课程：面向对象高级编程
作业要求：
1. 定义一个 Student 类，使用 __slots__ 限制属性
2. 定义一个 Temperature 类，使用 @property 实现温度转换
3. 定义一个 Shape 基类，以及 Circle 和 Rectangle 子类，实现多态
4. 定义一个 Color 枚举类，包含红、绿、蓝三种颜色

完成后输入 `python，提交作业` 提交。
"""

from enum import Enum

# 作业1：Student 类
# 请在此处填写代码
class Student:
    pass

# 作业2：Temperature 类
# 请在此处填写代码
class Temperature:
    pass

# 作业3：Shape 类
# 请在此处填写代码
class Shape:
    pass

class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

# 作业4：Color 枚举类
# 请在此处填写代码
class Color(Enum):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - Student:")
    s = Student("Alice", 25)
    print(f"姓名: {s.name}")
    print(f"年龄: {s.age}")

    print("\n测试作业2 - Temperature:")
    t = Temperature(100)
    print(f"摄氏度: {t.celsius}")
    print(f"华氏度: {t.fahrenheit}")

    print("\n测试作业3 - Shape:")
    circle = Circle(5)
    rect = Rectangle(4, 6)
    print(f"圆面积: {circle.area():.2f}")
    print(f"矩形面积: {rect.area()}")

    print("\n测试作业4 - Color:")
    print(f"Color.RED = {Color.RED}")
    print(f"Color.GREEN = {Color.GREEN}")
    print(f"Color.BLUE = {Color.BLUE}")
