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
    x = score
    if x >= 90 and x <= 100:
        return "A"              #语法结束不需要以；结束    函数要通过return返回值，不能用print返回
    elif x >= 80 and x < 90:
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    elif x >= 60 and x < 70:
        return "D"
    else :                      # else后面不需要写条件
        return "F"
    pass

# 作业2：判断偶数
# 请在此处填写代码
def is_even(num):
    if num % 2 ==0:
        return True
    else:
        return False
    pass

# 作业3：判断闰年
# 请在此处填写代码
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
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
