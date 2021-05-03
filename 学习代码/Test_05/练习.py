class PetShop(object):
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.pet_list = []

    # 添加宠物
    def add_pet(self, pets):
        self.pet_list.append(pets)

    # 输出宠物店及宠物信息
    def info(self):
        if len(self.pet_list) == 0:
            print('本店暂时还没有宠物，欢迎下次再来！')
            return
        print('店名：{}，有{}个宠物'.format(self.shop_name, len(self.pet_list)))
        for pet in self.pet_list:
            print(pet)


class Pet(object):
    def __init__(self, name, gender, age, breed):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed

    def bark(self):
        print('正在叫')

    def eat(self):
        print('正在吃')

    def __repr__(self):
        return '名字：{}，性别：{}，年龄：{}，品种：{}'.format(self.name, self.gender, self.age, self.breed)


class PetDog(Pet):
    def bark(self):
        print(self.name + '正在汪汪汪')

    def build_home(self):
        print(self.name + '正在拆家')

    def eat(self):
        print(self.name + '正在啃骨头')

    def __repr__(self):
        return super().__repr__()


class PetCat(Pet):
    def __init__(self, name, gender, age, breed, eyes_color):
        super(PetCat, self).__init__(name, gender, age, breed)
        self.eyes_color = eyes_color

    def bark(self):
        print(self.name + '正在喵喵喵')

    def eat(self):
        print(self.name + '正在吃鱼')

    def __repr__(self):
        other = super(PetCat, self).__repr__()
        other += '，眼睛颜色：{}'.format(self.eyes_color)
        return other


shop = PetShop('萌宠宠物店')
dog = PetDog('大黄', '公', '1岁', '中华田园犬')
cat = PetCat('咪咪', '母', '2岁', '三花', '金色')

shop.add_pet(dog)
shop.add_pet(cat)

shop.info()
