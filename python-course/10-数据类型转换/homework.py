# -*- coding: utf-8 -*-
"""
课程：数据类型转换
作业要求：
1. 将字符串 "123" 转换为整数并打印
2. 将整数 456 转换为字符串并拼接 "元"
3. 将字符串 "3.14" 转换为浮点数并打印
4. 将列表 ["Hello", "World"] 转换为字符串（用空格连接）

完成后输入 `python，提交作业` 提交。
"""

# 作业1：字符串转整数
# 请在此处填写代码
def homework1():
    num = int("123")
    print(f"type(num) = {type(num)}")

    pass

# 作业2：整数转字符串并拼接
# 请在此处填写代码
def homework2():
    num1 = str(456)
    num2 = str("元")
    print(f"num1 + num2 = {num1 + num2}")

    pass

# 作业3：字符串转浮点数
# 请在此处填写代码
def homework3():
    num1 = float("3.14")
    print(f"num1 = {num1}")

    pass

# 作业4：列表转字符串
# 请在此处填写代码
def homework4():
    word = ["hello", "world"]       
    x = ",".join(word)              #这是字符串的 join() 方法，用来把多个字符串连接成一个字符串。
    print(f"x = {x}")

    a = "space university"
    y = a.split()                     #这是字符串的 split() 方法，用来把一个字符串分割成多个部分，并返回一个列表
    print(f"y = {y}")
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 字符串转整数:")
    homework1()
    print("\n测试作业2 - 整数转字符串并拼接:")
    homework2()
    print("\n测试作业3 - 字符串转浮点数:")
    homework3()
    print("\n测试作业4 - 列表转字符串:")
    homework4()
