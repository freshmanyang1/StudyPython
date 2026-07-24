# -*- coding: utf-8 -*-
"""
课程：集合set
作业要求：
1. 创建两个集合 set1 和 set2，分别包含一些数字
2. 求两个集合的并集
3. 求两个集合的交集
4. 求两个集合的差集

完成后输入 `python，提交作业` 提交。
"""

# 作业1：创建两个集合
# 请在此处填写代码
def homework1():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, "sun", 7}
    print(f"set1 = {set1}")
    print(f"set2 = {set2}")
    pass

# 作业2：求并集
# 请在此处填写代码
def homework2():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, "sun", 7}
    print(f"ser1 = {set1}")
    print(F"set2 = {set2}")
    print(f"set1 | set2 = {set1 | set2}")       #并集 将两者结合
    print(f"set1.union(set2) = {set1.union(set2)}")
    print(f"set1 & set2 = {set1 & set2}")       #交集 取两者都有的
    print(f"set1.intersection(set2) = {set1.intersection(set2)}")
    print(f"set1 - set2 = {set1 - set2}")       #差集  取set1中有但set2中没有的元素
    print(f"set1.difference(set2) = {set1.difference(set2)}")
    print(f"set1 ^ set2 = {set1 ^ set2}")    #对称差集  取两者中不重复的元素
    print(f"set1.symmetric_difference = {set1.symmetric_difference(set2)}")
    pass

# 作业3：求交集
# 请在此处填写代码
def homework3():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, "sun", 7}
    print(f"set1 & set2 = {set1 & set2}")       #交集 取两者都有的
    print(f"set1.intersection(set2) = {set1.intersection(set2)}")
    pass

# 作业4：求差集
# 请在此处填写代码
def homework4():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, "sun", 7}
    print(f"set1.difference(set2) = {set1.difference(set2)}")
    print(f"set1 ^ set2 = {set1 ^ set2}")    #对称差集  取两者中不重复的元素
    print(f"set1.symmetric_difference = {set1.symmetric_difference(set2)}")


# 元素常用方式
    set1.add("moon")                                    #元素添加
    set1.update({"star", "university", "space"})        #一次性添加多个元素{}   
    print(f"set1 = {set1}")  

    set1.remove(2)                                          #删除， 没有元素会报错  
    print(f"set1 = {set1}")                                 
    set1.discard(3)                                         #删除，没有元素不会报错
    print(f"set1 = {set1} ")
    set1.pop()                                              #随即删除一个
    print(f"set1 = {set1}")
    set1.difference_update({"space", "university"})         #删除多个
    print(f"set1 = {set1}")
    set1.clear()                                            #删除集合内所有元素
    print(f"set1 = {set1}")
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 创建两个集合:")
    homework1()
    print("\n测试作业2 - 求并集:")
    homework2()
    print("\n测试作业3 - 求交集:")
    homework3()
    print("\n测试作业4 - 求差集:")
    homework4()
