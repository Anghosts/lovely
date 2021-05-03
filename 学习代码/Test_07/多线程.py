import threading
import time


def dance():
    for i in range(20):
        time.sleep(0.2)
        print('正在跳舞')


def sing():
    for i in range(20):
        time.sleep(0.2)
        print('正在唱歌')


t1 = threading.Thread(target=dance)
t2 = threading.Thread(target=sing)

t1.start()
t2.start()
