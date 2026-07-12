# 自定义异常

## 学习目标

- 掌握创建异常类的方法
- 了解 raise 语句的使用
- 掌握异常链

## 知识点

### 1. 创建异常类

```python
class MyError(Exception):
    pass

def foo():
    raise MyError("自定义错误")

try:
    foo()
except MyError as e:
    print(e)
```

### 2. raise 语句

```python
def validate_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能大于150")
    return age
```

### 3. 异常链

```python
try:
    # 代码
except ValueError as e:
    raise TypeError("类型错误") from e
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 创建异常类
- raise 语句
- 异常链

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
