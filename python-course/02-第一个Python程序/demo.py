# -*- coding: utf-8 -*-
"""
课程：第一个Python程序
演示：print() 函数、注释、if __name__ == "__main__"
"""

# 1. print() 函数基本用法
print("Hello, World!")
print("你好，Python！")

# 2. 输出数字
print(42)
print(3.14)

# 3. 输出多个值
print("姓名:", "张三")
print("年龄:", 25)

# 4. 使用 sep 参数指定分隔符
print("2024", "01", "01", sep="-")
print("a", "b", "c", sep=", ")

# 5. 使用 end 参数指定结尾
print("Hello", end=" ")
print("World")

# 6. 输出空行
print()

# 7. 输出表达式结果
print(1 + 2)
print("Hello" + " " + "Python")

# 8. 单行注释
# 这是单行注释，用于解释代码
print("单行注释示例")  # 这也是单行注释

# 9. 多行注释
"""
这是多行注释
可以写多行
通常用于文档说明
"""

# 10. if __name__ == "__main__" 示例
### def greet():
    # """打招呼函数"""
    # print("Hello from greet()!")

### def add(a, b):
    #"""加法函数"""
    # return a + b

# 只有直接执行此文件时才会运行
###if __name__ == "__main__":
    #print("=== if __name__ == '__main__' 示例 ===")
    # greet(
    # result = add(3, 5)
    # print(f"3 + 5 = {result}")
    # print("这段代码只在直接执行此文件时运行")
