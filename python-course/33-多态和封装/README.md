# 多态和封装

## 学习目标

- 理解多态的概念
- 掌握多态的使用
- 了解封装的概念
- 掌握访问控制

## 知识点

### 1. 多态的概念

多态是指不同的类对同一方法有不同的实现。

### 2. 多态的使用

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Kitty")
make_sound(dog)  # "Woof!"
make_sound(cat)  # "Meow!"
```

### 3. 封装的概念

封装是指将数据和方法封装在类中，限制外部访问。

### 4. 访问控制

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # 公有属性
        self._age = age       # 受保护属性
        self.__secret = "xxx" # 私有属性
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 多态的概念
- 多态的使用
- 封装的概念
- 访问控制

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
