# -*- coding: utf-8 -*-
"""
课程：比较和逻辑运算符
作业要求：
1. 编写一个函数 is_positive(num)，判断一个数是否是正数
2. 编写一个函数 is_in_range(num, low, high)，判断一个数是否在指定范围内
3. 编写一个函数 is_valid_age(age)，判断年龄是否有效（0-150）

完成后输入 `python，提交作业` 提交。
"""

# 作业1：判断正数
# 请在此处填写代码
def is_positive(num):
    pass

# 作业2：判断范围
# 请在此处填写代码
def is_in_range(num, low, high):
    pass

# 作业3：判断有效年龄
# 请在此处填写代码
def is_valid_age(age):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 判断正数:")
    print(f"is_positive(10) = {is_positive(10)}")
    print(f"is_positive(-5) = {is_positive(-5)}")
    print(f"is_positive(0) = {is_positive(0)}")

    print("\n测试作业2 - 判断范围:")
    print(f"is_in_range(5, 1, 10) = {is_in_range(5, 1, 10)}")
    print(f"is_in_range(15, 1, 10) = {is_in_range(15, 1, 10)}")

    print("\n测试作业3 - 判断有效年龄:")
    print(f"is_valid_age(25) = {is_valid_age(25)}")
    print(f"is_valid_age(-5) = {is_valid_age(-5)}")
    print(f"is_valid_age(200) = {is_valid_age(200)}")
