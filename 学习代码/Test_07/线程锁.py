import threading, time

ticket = 20
# 创建一把锁
lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:
        lock.acquire()  # 上锁
        if ticket > 0:
            time.sleep(0.5)
            ticket -= 1
            lock.release()  # 解锁
            print('{}卖出了一张票，还剩{}张'.format(threading.current_thread().name, ticket))
        else:
            lock.release()  # 解锁
            print('票卖完了')
            break


t1 = threading.Thread(target=sell_ticket, name='线程1')
t2 = threading.Thread(target=sell_ticket, name='线程2')

t1.start()
t2.start()
