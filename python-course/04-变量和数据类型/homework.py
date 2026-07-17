# -*- coding: utf-8 -*-
"""
课程：变量和数据类型
作业要求：
1. 定义一个整数变量 age，存储你的年龄
2. 定义一个浮点数变量 height，存储你的身高（米）
3. 定义一个字符串变量 name，存储你的名字
4. 定义一个布尔值变量 is_student，表示是否是学生
5. 将 age 转换为字符串并拼接 "岁" 输出

完成后输入 `python，提交作业` 提交。
"""

# 作业1：定义整数变量 age
# 请在此处填写代码
def homework1():
    age = 25
    print(f"age = {age}")
    pass

# 作业2：定义浮点数变量 height
# 请在此处填写代码
def homework2():
    height: float = 1.80
    print(f"height = {height}")
    pass

# 作业3：定义字符串变量 name
# 请在此处填写代码
def homework3():
    name = "Ethan"
    print(f"name = {name}")
    pass

# 作业4：定义布尔值变量 is_student
# 请在此处填写代码
def homework4():
    is_student = True
    print(f"is_student = {is_student}")
    pass

# 作业5：类型转换和拼接
# 请在此处填写代码
def homework5():
    age = 25
    age_str = str(age) + "岁"
    print(f"age_str = {age_str}")
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 整数变量:")
    homework1()
    print("\n测试作业2 - 浮点数变量:")
    homework2()
    print("\n测试作业3 - 字符串变量:")
    homework3()
    print("\n测试作业4 - 布尔值变量:")
    homework4()
    print("\n测试作业5 - 类型转换和拼接:")
    homework5()
