# -*- coding: utf-8 -*-
"""
课程：条件判断
作业要求：
1. 编写一个函数 grade(score)，根据分数返回等级（90-100: A, 80-89: B, 70-79: C, 60-69: D, 60以下: F）
2. 编写一个函数 is_even(num)，判断一个数是否是偶数
3. 编写一个函数 leap_year(year)，判断是否是闰年（能被4整除但不能被100整除，或者能被400整除）

完成后输入 `python，提交作业` 提交。
"""

# 作业1：成绩等级
# 请在此处填写代码
def grade(score):
    pass

# 作业2：判断偶数
# 请在此处填写代码
def is_even(num):
    pass

# 作业3：判断闰年
# 请在此处填写代码
def leap_year(year):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 成绩等级:")
    print(f"grade(95) = {grade(95)}")
    print(f"grade(85) = {grade(85)}")
    print(f"grade(75) = {grade(75)}")
    print(f"grade(65) = {grade(65)}")
    print(f"grade(55) = {grade(55)}")

    print("\n测试作业2 - 判断偶数:")
    print(f"is_even(4) = {is_even(4)}")
    print(f"is_even(7) = {is_even(7)}")

    print("\n测试作业3 - 判断闰年:")
    print(f"leap_year(2024) = {leap_year(2024)}")
    print(f"leap_year(2023) = {leap_year(2023)}")
    print(f"leap_year(2000) = {leap_year(2000)}")
    print(f"leap_year(1900) = {leap_year(1900)}")
