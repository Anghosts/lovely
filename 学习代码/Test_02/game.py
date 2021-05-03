import random
import sys
import csv
from time import sleep
from Test_03 import 名片管理系统

'''进行输出延时'''


def slow(msg, text):
    print(msg, end='')
    for i in text:
        print(i, end='')
        sys.stdout.flush()
        sleep(0.8)
    return '.'


# 设置姓名，年龄，身高

names = ''
ages = 0
heights = 0

studend = []


def identity(name, age, height):
    global names, ages, heights
    names = name
    ages = age
    heights = height
    # print('姓名:{0} 年龄:{1} 身高:{2}(cm)'.format(names, ages, heights))


def info():
    ID = input('请输入您的账号：')
    password = input('请输入您的密码：')
    for i in studend:
        for key, value in i.items():
            if ID == key and password == value:
                print('登录成功')
                名片管理系统.operation()
            else:
                print('账号或密码错误')


def info1():
    ID = input('请输入您的账号：')
    while True:
        password = input('请输入您的密码：')
        password2 = input('请再次输入您的密码：')
        if password2 != password:
            print('两次密码输入不一致，请再次输入')
        else:
            print('注册成功！')
            break
    studend.append({ID: password})
    for i in range(len(studend)):
        with open("test.csv", mode="w", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([studend[i]])


# 登录
def room():
    # slow('正在为你打开新世界的大门', '......')
    print('\n成功进入新世界，请先登录再操作：')
    quit_h = True
    while quit_h:
        pattern = input('==> 1.登录  2.注册  3.退出  4.调教 <==\n')
        if pattern == '1':  # 登录
            info()
        elif pattern == '2':  # 注册
            info1()
        elif pattern == '3':  # 退出
            quit_h = False
            print('已退出')
        elif pattern == '4':  # 调教
            print('想屁吃！！！')
        else:
            print('您输入的格式有误！')


def bed():
    print('已捕获一个生物')
    play = input('是否开始调教？y/* :')
    if play == 'y':
        for i in range(3):  # 让用户有两次输错密码的机会
            sequence = random.randint(0, 3)  # 创建输入密码的索引，每次输错密码，都重新设置密码索引
            try:
                password = int(input('请输入通行码({}):'.format(sequence)))
                if password == listpass[sequence]:  # 判断密码是否正确
                    room()
                    break
                else:  # 错误继续输入
                    print('错误！')
            except ValueError:
                print('请输入数字!不能包含其它字符')

    else:
        print('---------------')
        implement = input(' 返回/r  退出/* ：')
        if implement == 'r':
            bed()
        else:
            print('已退出')
            # return


listpass = [00, 11, 22, 33]  # 创建四个列表密码

identity('六花', 16, 159)
bed()
