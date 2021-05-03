import queue, multiprocessing

# q1 = multiprocessing.Queue()    # 进程间通信
# q2 = queue.Queue()  # 线程间通信

# 创建队列时，可以指定最大长度，默认为0
q = multiprocessing.Queue(5)

q.put('hello')
q.put('world')
q.put('good')
# q.put('hi')
# q.put('old')

print(q.full())   # 判断队列状态

# block = True: 表示是阻塞，如果队列已经满了，就等待
# timeout：超时，等待时间
q.put('how', block=True, timeout=1)

q.put_nowait('how')  # q.put('how', block=True)

print(q.get(block=True, timeout=1))
