class Auto(object):
    def __init__(self, tyre_count, colour, weight, speed):
        self.tyre_count = tyre_count
        self.colour = colour
        self.weight = weight
        self.speed = speed

    def speed_up(self, x):
        self.speed += x
        print('汽车正在加速')

    def speed_down(self, x):
        self.speed += x
        if self.speed <= 0 and x < 0:
            self.speed = 0
        print('汽车正在减速')

    def parking(self, x):
        if x == 0:
            self.speed = 0
        print('汽车已停')


class CarAuto(Auto):
    def __init__(self, tyre_count, colour, weight, speed, ac, CD):
        super().__init__(tyre_count, colour, weight, speed)
        self.ac = ac
        self.CD = CD

    def speed_up(self, s):
        print('汽车正在超级加速')

    def speed_down(self, x):
        print('汽车正在往死里减速')

    def info(self):
        print('轮胎个数：{}，汽车颜色：{}，汽车重量：{}，速度：{}，有无空调：{}，有无CD功能：{}'.format(self.tyre_count, self.colour, self.weight, self.speed, self.ac, self.CD))


a = Auto(4, '白色', '1.2t', '100/h')

c = CarAuto(5, '白色', '1.5t', '100/h', '有空调', '有CD功能')

c.info()
