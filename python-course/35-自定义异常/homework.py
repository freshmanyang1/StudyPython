# -*- coding: utf-8 -*-
"""
课程：自定义异常
作业要求：
1. 定义一个 InvalidAgeError 异常类
2. 定义一个 validate_age 函数，使用自定义异常
3. 编写测试代码，验证异常处理

完成后输入 `python，提交作业` 提交。
"""

# 作业1：定义 InvalidAgeError 异常类
# 请在此处填写代码
class InvalidAgeError(Exception):
    pass

# 作业2：定义 validate_age 函数
# 请在此处填写代码
def validate_age(age):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - InvalidAgeError 异常类:")
    try:
        validate_age(-5)
    except InvalidAgeError as e:
        print(f"捕获到: {e}")

    print("\n测试作业2 - validate_age 函数:")
    try:
        validate_age(25)
        print("年龄有效")
    except InvalidAgeError as e:
        print(f"错误: {e}")

    try:
        validate_age(200)
    except InvalidAgeError as e:
        print(f"捕获到: {e}")
