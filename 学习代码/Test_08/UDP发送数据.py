import socket

# AF_INET: 表示这个socket用来网络连接
# SOCK_DGRAM : 表示是一个udp连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 8080))

while 1:
    # data: 发送的数据
    # address: 发送给谁(ip, port)
    # 端口号: (0)1024~65536
    msg = input('发送信息：')
    if msg == 'exit':
        break
    s.sendto(msg.encode('utf8'), ('10.143.4.131', 8080))
s.close()
