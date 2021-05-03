class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Studend(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score
    def info(self):         #重写info方法
        super().info()
        print(self.score)
    def __str__(self):
        return '我叫{0}，今年{1}岁,学号为{2}'.format(self.name,self.age,self.score)

stu=Studend('王晶',18,202032020074)
print(stu)
print('-------------------------------')
print(stu.__dict__)     #实例对象的属性字典
print(Studend.__bases__)    #类的父类
print(Studend.__mro__)      #类的层次结构
print(Person.__subclasses__())  #类的列表

print('-----------------------------------')
class Dog():
    def info(self):
        print('狗吃屎！')
class Cat():
    def info(self):
        print('猫吃鱼！')
def fun(obj):
    obj.info()
fun(Dog())
fun(Cat())




