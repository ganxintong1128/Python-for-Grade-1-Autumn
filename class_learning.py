# 父类
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# 子类
class Dog(Animal):  # 继承Animal类
    def speak(self):  # 方法重写
        return "汪汪！"

class Cat(Animal):
    def speak(self):
        return "喵喵！"

dog = Dog("小白")
cat = Cat("小花")
print(dog.speak())  # 汪汪！
print(cat.speak())  # 喵喵！