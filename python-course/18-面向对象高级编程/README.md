# 面向对象高级编程

## 学习目标

- 掌握 `__slots__` 的使用
- 了解 `@property` 装饰器
- 掌握多重继承
- 了解定制类和元类

## 知识点

### 1. `__slots__`

限制实例属性。

```python
class Student:
    __slots__ = ('name', 'age')

s = Student()
s.name = "Alice"
s.age = 25
# s.score = 100  # 错误：不允许添加新属性
```

### 2. `@property`

将方法转换为属性。

```python
class Student:
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须在 0-100 之间')
        self._score = value

s = Student(90)
print(s.score)  # 90
s.score = 85
```

### 3. 多重继承

```python
class A:
    def foo(self):
        print("A.foo")

class B(A):
    def foo(self):
        print("B.foo")

class C(A):
    def foo(self):
        print("C.foo")

class D(B, C):
    pass

d = D()
d.foo()  # B.foo (MRO)
```

### 4. 定制类

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Student: {self.name}'

    def __repr__(self):
        return f'Student({self.name!r})'

s = Student("Alice")
print(s)  # Student: Alice
```

### 5. 枚举类

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)      # Color.RED
print(Color.RED.name) # RED
print(Color.RED.value)# 1
```

### 6. 元类

```python
class HelloMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['hello'] = lambda self: f"Hello from {name}"
        return type.__new__(cls, name, bases, attrs)

class Hello(metaclass=HelloMeta):
    pass

h = Hello()
print(h.hello())  # Hello from Hello
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- `__slots__` 的使用
- `@property` 装饰器
- 多重继承
- 定制类和元类

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
