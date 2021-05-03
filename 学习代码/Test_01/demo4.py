class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def print1():
        print('我是静态方法')

    @classmethod
    def print2(cls):
        print('我是类方法')

    def print(self):
        print('我叫'+self.name,'今年',self.age,'岁')

stu1=Student("张三",18)
print(id(stu1))
stu2=Student('李四',20)
print(id(stu2))
print('--------------------------------')
stu1.print()    #调用print方法,/Student.print(stu1)
stu2.print()    #调用print方法,/Student.print(stu2)
print('--------------------------------')
stu1.gender='动态绑定的属性'     #动态绑定的属性

print(stu1.gender)


def show():
    print('动态绑定的方法')
stu1.show=show
stu1.show()
print('--------------------------------')
stu1.print1()
stu2.print2()