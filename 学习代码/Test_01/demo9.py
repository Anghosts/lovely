import pygame
from math import pi

x = 0
y = 0
z = 1
i = 1

pygame.init()  # 初始化
screen = pygame.display.set_mode((1200, 800))  # 创建1200*800大小的窗口
screen.fill((230, 230, 230))  # 填充颜色
# 设置窗口的标题
pygame.display.set_caption('测试')
print(type(screen))

image = pygame.image.load('D://Temp//ship.png')  # 创建图片对象，括号内为图片地址
size = image.get_size()  # 获取图片大小
# screen.blit(image,(0,0))
# pygame.display.update()
# pygame.draw.rect(screen,(255,0,0),(10,10,10,15),0)
pygame.draw.lines(screen, (255, 0, 0), True, [(300, 50), (100, 150), (200, 120), (330, 200)], 3)  # 划线

pygame.draw.arc(screen, (255, 255, 0), (10, 200, 200, 200), pi / 2, z, 3)
pygame.display.flip()  # 将前面的内容渲染到屏幕

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 让窗口可以一直显示在屏幕上，直到点关闭按钮
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                pygame.draw.arc(screen, (255, 255, 0), (100, 400, z, i), pi / 2, pi, 3)  # 画圆
                z += 4
                i += 4
                pygame.display.flip()  # 将前面的内容渲染到屏幕
                print('鼠标按下')

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                print('鼠标按下弹起')

            if event.type == pygame.MOUSEMOTION:
                # print(event.pos)
                pass

            if event.type == pygame.KEYDOWN:
                print(chr(event.key))
                print('键盘按钮按下')
                if chr(event.key) == 'd':
                    print('右')
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, 10, 15), 0)
                    x += 10
                    pygame.display.flip()
                elif chr(event.key) == 'a':
                    print('左')
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, 10, 15), 0)
                    x -= 10
                    pygame.display.flip()
                elif chr(event.key) == 'w':
                    print('上')
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, 10, 15), 0)
                    y -= 10
                    pygame.display.flip()
                elif chr(event.key) == 's':
                    print('下')
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, 10, 15), 0)
                    y += 10
                    pygame.display.flip()
    except ValueError:
        print('错误！')
        exit()
