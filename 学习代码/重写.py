class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Student(Person):
    def __init__(self, name, age, school, ID, city):
        super(Student, self).__init__(name, age)
        self.school = school
        self.ID = ID
        self.city = city

    def sleep(self):
        super().sleep()
        print(self.name + '被叫醒了')
        print('他因上课睡觉，个人信息被人扒出来了')
        print('年龄：{}，在读学校：{}，身份证：{}，家庭地址：{}'.format(self.age, self.school, self.ID, self.city))
        print('全世界的人都在骂他，就因为他上课睡了觉')


s = Student('tom', 18, '潇湘职业学院', '4311*********81X', '湖南省永州市xx县xx镇xx村x组')
s.sleep()
