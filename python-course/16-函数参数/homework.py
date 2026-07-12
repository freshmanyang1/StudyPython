# -*- coding: utf-8 -*-
"""
课程：函数参数
作业要求：
1. 定义一个函数 join_words(*words)，接受任意数量的字符串参数，用空格连接它们
2. 定义一个函数 create_profile(name, age, **kwargs)，创建用户资料字典
3. 定义一个函数 calculate(operation, *numbers)，根据操作符（+、-、*、/）计算结果

完成后输入 `python，提交作业` 提交。
"""

# 作业1：连接单词
# 请在此处填写代码
def join_words(*words):
    pass

# 作业2：创建用户资料
# 请在此处填写代码
def create_profile(name, age, **kwargs):
    pass

# 作业3：计算函数
# 请在此处填写代码
def calculate(operation, *numbers):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 连接单词:")
    print(f"join_words('Hello', 'World') = {join_words('Hello', 'World')}")
    print(f"join_words('I', 'love', 'Python') = {join_words('I', 'love', 'Python')}")

    print("\n测试作业2 - 创建用户资料:")
    print(f"create_profile('Alice', 25, city='Beijing') = {create_profile('Alice', 25, city='Beijing')}")

    print("\n测试作业3 - 计算函数:")
    print(f"calculate('+', 1, 2, 3) = {calculate('+', 1, 2, 3)}")
    print(f"calculate('*', 2, 3, 4) = {calculate('*', 2, 3, 4)}")
