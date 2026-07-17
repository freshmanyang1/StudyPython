# -*- coding: utf-8 -*-
"""
课程：元组tuple
作业要求：
1. 创建一个元组 coordinates，包含经度和纬度（例如：(116.4, 39.9)）
2. 创建一个元组 colors，包含 5 种颜色
3. 访问 colors 元组的第三个元素
4. 使用切片获取 colors 元组的前三个元素
5. 遍历 colors 元组并打印每个元素

完成后输入 `python，提交作业` 提交。
"""

# 作业1：创建坐标元组
# 请在此处填写代码
def homework1():
    coordinates = (116.4, 393.9)
    print("坐标", coordinates)
    pass

# 作业2：创建颜色元组
# 请在此处填写代码
def homework2():
    colors = ("red", "green", "blue", "yellow","puple")
    print("颜色", colors)
    pass

# 作业3：访问第三个元素
# 请在此处填写代码
def homework3():
    colors = ("red", "green", "blue", "yellow", "purple")
    print("第三个元素", colors[3])  #这里是从0开始计数
    colors.index("purple")    #index里需要填元素，不能填数字索引
    print("第三个元素", colors.index("purple"))
    pass

# 作业4：使用切片获取前三个元素
# 请在此处填写代码
def homework4():
    colors = ("red", "green", "blue", "yellow", "purple")
    print("前两个元素", colors[:2])
    pass

# 作业5：遍历元组
# 请在此处填写代码
def homework5():
    colors = ("red", "green", "blue", "yellow", "purple")
    for color in colors:   # for 临时变量 in 可遍历对象:
        print(color)        #print(临时变量)
    for i, x in enumerate(colors):   #enumerate()索引遍历函数  i，x是两个索引值
        print(f"索引: {i}, 颜色: {x}")    # i是索引， X是索引对应的值
    pass                                   # i，x 这里第一个位置返回索引，第二个值是元素  索引只能是整数，元素没限制   

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 创建坐标元组:")
    homework1()
    print("\n测试作业2 - 创建颜色元组:")
    homework2()
    print("\n测试作业3 - 访问第三个元素:")
    homework3()
    print("\n测试作业4 - 使用切片获取前三个元素:")
    homework4()
    print("\n测试作业5 - 遍历元组:")
    homework5()
