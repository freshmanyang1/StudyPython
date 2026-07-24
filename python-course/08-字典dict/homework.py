# -*- coding: utf-8 -*-
"""
课程：字典dict
作业要求：
1. 创建一个字典 person，包含姓名、年龄、城市三个键值对
2. 向字典中添加一个新的键值对（例如：职业）
3. 删除字典中的年龄键值对
4. 使用字典推导式生成一个字典，键为 1-5，值为键的平方

完成后输入 `python，提交作业` 提交。
"""

# 作业1：创建字典
# 请在此处填写代码
def homework1():
    student = {
        "name": "Ethan",
        "age": 30,
        "city": "Beijing"}   #字典里需要使用大括号{}
    print(f"student = {student}")
    pass

# 作业2：添加键值对
# 请在此处填写代码
def homework2():
    student = {
        "name": "Ethan",
        "age": 30,
        "city": "Beijing"
    }
    student["job"] = "Engineer"
    student["age"] = 28
    print(f"student = {student}")
    
    pass

# 作业3：删除键值对
# 请在此处填写代码
def homework3():
    student = {                     
        "name": "Ethan",
        "age": 30,
        "city": "Beijing",
        "job": "Engineer"
    }
    del student["job"]
    print(f"student = {student}")
    student.pop ("name")
    print(f"student = {student}")
    pass

# 作业4：字典推导式
# 请在此处填写代码
def homework4():
    squares = {}              
    for i in range(10):
        squares[i] = i ** 2
    print(f"squares = {squares}")

    squares = { i: i ** 2 for i in range(10)}
    print(f"squares = {squares}")

    even_squares = {                    #这种是拆开写法，函数定义
        x : x ** 2                          # x是键，x ** 2是值 x的平方
        for x in range(10)                  # for循环遍历0-9   10个数
        if x % 2 == 0                       # 只取偶数
    }
    print(f"even_squares = {even_squares}")
    
    even_squares = { x : x ** 2 for x in range(10) if x % 2 ==0}         #这种是合并写法，函数定义（x为键，for循环遍历，取模运算，取偶数）
    print(f"even_squares = {even_squares}")
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 创建字典:")
    homework1()
    print("\n测试作业2 - 添加键值对:")
    homework2()
    print("\n测试作业3 - 删除键值对:")
    homework3()
    print("\n测试作业4 - 字典推导式:")
    homework4()
