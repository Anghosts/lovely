import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.143.4.131', 8080))


def send_msg():
    while True:
        msg = input('发送信息：')
        if msg == 'exit':
            break
        s.sendto(msg.encode('utf8'), ('10.143.4.131', 8080))


def recv_msg():
    while True:
        data, addr = s.recvfrom(1024)
        print('接收到了{}地址 {}端口的消息：{}'.format(addr[0], addr[1], data.decode('utf8')))


t1 = threading.Thread(target=send_msg())
t2 = threading.Thread(target=recv_msg())

t1.start()
t2.start()
