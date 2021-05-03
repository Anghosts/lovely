class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle(object):
    def __init__(self, top_left: Point, bottom_right: Point):   # 左上角和右下角
        self.top_left = top_left
        self.bottom_right = bottom_right

    # 求矩形的面积
    def get_area(self):
        length = self.bottom_right.x - self.top_left.x
        width = self.top_left.y - self.bottom_right.y
        return length * width

    # 判断一个点是否在矩形内
    def is_inside(self, point):
        return self.bottom_right.x >= point.x >= self.top_left.x and self.top_left.y >= point.y >= self.bottom_right.y


p1 = Point(4, 20)
p2 = Point(30, 8)

r = Rectangle(p1, p2)
print(r.get_area())

p3 = Point(4, 20)
print(r.is_inside(p3))
