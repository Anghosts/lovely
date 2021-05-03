import file_p


def info():
    print('--' * 10)
    print('--名片管理系统-- V1.0')
    print('1:添加名片')
    print('2:删除名片')
    print('3:修改名片')
    print('4:查询名片')
    print('5:显示所有名片')
    print('6:退出系统')
    print('--' * 10)


card = [
    {'姓名': '张三', '手机号': 0, 'QQ': 0}
]
goto = True
flag = True  # 程序的主循环


# 此函数的功能是，用户每完成一个操作以后，询问用户是否再次操作，如果选择返回，则结束本次操作，继续下一次操作
def go(fn):
    global goto, flag
    while True:
        x = input('是否继续操作？1：继续  2：返回 :')
        if x == '2':
            break
        elif x == '1':
            goto = False
            fn()
            goto = True
        else:
            print('格式错误！')


# 添加名片
def add():
    name = input('请输入您要添加的姓名：')
    tel = input('请输入您的手机号：')
    qq = input('请输入您的QQ号：')

    if file_p.red(name):
        print('您输入的姓名已存在')
    else:
        card.append({'姓名': name, '手机号': tel, 'QQ': qq})
        print('添加成功！')
        file_p.wri(name, tel, qq)

    print()
    if goto:
        go(add)


# 删除名片
def delete():
    names = input('请输入您要删除名片的姓名：')
    for i in card:
        if i['姓名'] == names:
            card.remove(i)
            print('已删除')
            break
    else:
        print('姓名不存在')
    if goto:
        go(delete)


# 修改名片
def amend():
    names = input('请输入您要修改名片的姓名：')
    for i in card:
        if i['姓名'] == names:
            print('( 输入你要修改的信息 )')
            name = input('请输入您的姓名：')
            tel = input('请输入您的手机号：')
            qq = input('请输入您的QQ号：')
            i['姓名'] = name
            i['手机号'] = tel
            i['QQ'] = qq
            print('修改成功')
            break
    else:
        print('姓名不存在')
    if goto:
        go(amend)


# 查询名片
def find():
    global goto
    names = input('请输入您要查询名片的姓名：')
    for i in card:
        if i['姓名'] == names:
            print(i)
            break
    else:
        print('姓名不存在')
    if goto:
        go(find)


# 显示所有名片
def entire():
    for cards in card:
        print(cards)
    print()


def operation():
    global flag
    while flag:
        info()
        try:
            state = int(input('请继续您的下一步操作(1~6)：'))
            if state == 1:  # 添加名片
                add()
            elif state == 2:  # 删除名片
                delete()
            elif state == 3:  # 修改名片
                amend()
            elif state == 4:  # 查询名片
                find()
            elif state == 5:  # 显示所有名片
                entire()
            elif state == 6:
                flag = False
                print('已退出，感谢您的使用！')
            else:
                print('您输入你格式错误！请输入1~6的数字')
        except ValueError:
            print('您输入的格式错误！请输入1~6的数字')


if __name__ == '__main__':
    operation()