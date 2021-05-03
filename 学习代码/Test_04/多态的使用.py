class Dog(object):
    def work(self):
        print('狗正在工作')


class PoliceDog(Dog):
    def work(self):
        print('警犬正在搜捕坏人')


class BlindDog(Dog):
    def work(self):
        print('导盲犬正在领路')


class DrugDog(Dog):
    def work(self):
        print('缉毒犬正在搜毒')


class Person(object):
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work_with_dog(self):
        if self.dog is not None and isinstance(self.dog, Dog):
            self.dog.work()


p = Person('警察')

pd = PoliceDog()
p.dog = pd
p.work_with_dog()

bd = BlindDog()
p.dog = bd
p.work_with_dog()
