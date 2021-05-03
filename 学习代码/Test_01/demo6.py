class Student():
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):      #获取name的长度
        return len(self.name)

stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2         #两个对象相加
s1=stu1.__add__(stu2)   #两个对象相加
print(s)
print(s1)
lst=[11,22,33,44,55]
print(len(lst))     #获取列表的长度
print(len(stu1))