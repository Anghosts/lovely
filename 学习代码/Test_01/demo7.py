class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#类的赋值
cpu1=CPU()
cpu2=cpu1
print(id(cpu1))
print(id(cpu2))

print('-------------------------')
disk=Disk()     #创建一个Disk类的对象
computer=Computer(cpu1,disk)    #创建一个Computer类的对象


import copy
computer2=copy.copy(computer)   #浅拷贝
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

computer3=copy.deepcopy(computer)   #深拷贝