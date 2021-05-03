import threading, time
import queue


def produce():
    for i in range(20):
        time.sleep(1)
        print('生产了+++面包b{}'.format(i))
        q.put('b{}'.format(i))


def consumer():
    for i in range(20):
        time.sleep(0.5)
        print('买到了---面包{}'.format(q.get()))


q = queue.Queue()

p1 = threading.Thread(target=produce)
c1 = threading.Thread(target=consumer)

p1.start()
c1.start()
