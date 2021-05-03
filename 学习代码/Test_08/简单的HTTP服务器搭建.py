import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 8090))
server_socket.listen(128)

client_socket, client_addr = server_socket.accept()

# 从客户端的 socket 获取数据
data = client_socket.recv(1024).decode('utf8')
print('接收到{}的访问:\n{}'.format(client_addr[0], data))

# 设置一个响应头就换一行
client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))

client_socket.send('\n'.encode('utf8'))
# 给客户端返回消息
client_socket.send(client_addr[0].encode('utf8'))

