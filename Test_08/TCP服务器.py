import socket

# SOCK_STREAM: 基于TCP的socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9000))

s.listen(128)  # 排队的最大长度

# 接收数据
# 第0个数据是客户端的socket连接，第1个数据是客户端的IP地址和端口号
client_socket, client_address = s.accept()
data = client_socket.recv(1024)

print('接收到了{}地址 {}端口的消息：{}'.format(client_address[0], client_address[1], data.decode('utf8')))

# 将接收到的数据写人到文件中
with open('首页(副本).txt', 'wb') as file:
    w = file.write(data)
