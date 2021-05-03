import multiprocessing, time


def produce(x):
    for i in range(20):
        time.sleep(1)
        print('生产了+++面包b{}'.format(i))
        x.put('b{}'.format(i))


def consumer(x):
    for i in range(20):
        time.sleep(0.5)
        print('买到了---面包{}'.format(x.get()))


if __name__ == '__main__':
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=produce, args=(q,))
    c1 = multiprocessing.Process(target=consumer, args=(q,))

    p1.start()
    c1.start()
