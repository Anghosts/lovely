import socket, os


# 向服务器发送一个文件
def read_file():
    with open('首页.html', 'rb') as file:
        x = file.read(1024)
        return x


# SOCK_STREAM: 基于TCP的socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TCP在发送数据前必须要与服务器进行连接
s.connect(('10.143.4.131', 9000))  # 调用 connect 方法，与服务器建立连接

# 发送数据
s.send(read_file())
