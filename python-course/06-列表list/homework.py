# -*- coding: utf-8 -*-
"""
课程：列表list
作业要求：
1. 创建一个包含 5 个你喜欢的城市的列表 cities
2. 向列表中添加一个新城市
3. 删除列表中的第二个城市
4. 对列表进行排序
5. 使用切片获取列表的前三个元素

完成后输入 `python，提交作业` 提交。
"""

# 作业1：创建城市列表
# 请在此处填写代码
def homework1():
    cities = ["Beijing", "Shanghai", "Suzhou", "Zhengzhou", "Guangzhou"]
    print(f"城市列表: {cities}")
    pass

# 作业2：添加新城市
# 请在此处填写代码
def homework2():
    cities = ["Beijing", "Shanghai", "Suzhou", "Zhengzhou", "Guangzhou"]
    cities.append("Shenzhen")
    cities.insert(1, "Shenzhen")
    print(f"添加后={cities}")
    print(f"插入后={cities}")
    pass

# 作业3：删除第二个城市
# 请在此处填写代码
def homework3():
    cities = ["Beijing", "Shanghai", "Suzhou", "Zhengzhou", "Guangzhou"]
    del cities[-2]
    print(f"删除后 = {cities}")
    cities.remove("Suzhou")
    print(f"删除后 = {cities}")
    cities.pop(0)
    print(f"删除后 = {cities}")
    pass

# 作业4：对列表排序
# 请在此处填写代码
def homework4():
    cities = ["Beijing", "Shanghai", "Suzhou", "Zhengzhou", "Guangzhou"]
    cities.sort()
    print(f"排序后 = {cities}")
    cities.reverse()
    print(f"反转后 = {cities}")
    pass

# 作业5：使用切片获取前三个元素
# 请在此处填写代码
def homework5():
    cities = ["Beijing", "Shanghai", "Suzhou", "Zhengzhou", "Guangzhou"]
    print(f"cities = {cities}")
    print(f"前四个元素 = {cities[ :4]}")
    print(f"第23元素 = {cities[1:3]}")  #前面的数字加上后面的数字之前的  例：1:3就是只有1和2
    print(f"后4个元素 = {cities[1:]}")   #这个是1 2 3 4
    print(f"第24元素 = {cities[::2]}")    #这个是步调为2的去掉保留其他， 1 3 5
    print(f"倒序 = {cities[::-1]}")    #这个是从后到前倒叙遍历
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 创建城市列表:")
    homework1()
    print("\n测试作业2 - 添加新城市:")
    homework2()
    print("\n测试作业3 - 删除第二个城市:")
    homework3()
    print("\n测试作业4 - 对列表排序:")
    homework4()
    print("\n测试作业5 - 使用切片获取前三个元素:")
    homework5()
