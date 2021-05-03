import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.143.4.131', 8080))

while 1:
    # data: 接收到的消息
    # address: 是一个元组, 第0个是ip地址, 第1个是端口号
    data, address = s.recvfrom(1024)

    print('接收到了{}地址 {}端口的消息：{}'.format(address[0], address[1], data.decode('utf8')))

