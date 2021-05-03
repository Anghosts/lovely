import time, threading

x = 10


def test(a, b):
    time.sleep(1)
    global x
    x = a + b


t = threading.Thread(target=test, args=(1, 1))
t.start()

t.join()  # 让主线程等待子线程执行完

print(x)

