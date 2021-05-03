class House(object):
    def __init__(self, house_type, total_area, frn_list=None):  # 户型，总面积，家具名称列表
        if frn_list is None:
            frn_list = []
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.7  # 剩余面积
        self.frn_list = frn_list

    def add_frn(self, x):
        if self.free_area < x.area:
            print('剩余空间不足')
        else:
            self.frn_list.append(x.name)
            self.free_area -= x.area

    def __str__(self):
        return "户型：{}，总面积：{}，剩余面积：{}，家具名称：{}".format(self.house_type, self.total_area, self.free_area, self.frn_list)


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


house = House('两室一厅', 70)

sofa = Furniture('沙发', 12)
bed = Furniture('席梦思', 20)
chest = Furniture('衣柜', 5)
table = Furniture('餐桌', 8)
shoe_rack = Furniture('鞋架', 4)

house.add_frn(sofa)
house.add_frn(bed)
house.add_frn(chest)
house.add_frn(table)
house.add_frn(shoe_rack)

print(house)
