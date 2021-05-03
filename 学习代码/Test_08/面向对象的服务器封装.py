import socket


class MySever(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.socket.listen(128)

    def run_forever(self):
        while True:
            client_socket, client_addr = self.socket.accept()

            # 从客户端的 socket 获取数据
            data = client_socket.recv(1024).decode('utf8')
            print('接收到{}的访问'.format(client_addr[0]))

            path = ''
            if data:
                path = data.splitlines()[0].split(' ')[1]
                print('请求路径为:{}\n'.format(path))

            client_header = 'HTTP/1.1 200 OK\n'
            if path == '/login':
                client_body = '欢迎来到登录页面！'
            elif path == '/register':
                client_body = load_file('注册.html')
            elif path == '/':
                client_body = load_file('首页.html')
            else:
                client_header = 'HTTP/1.1 404 Page Not Found\n'
                client_body = '<h1 style="text-align: center;">对不起，您访问的页面不存在！</h1>'

            client_header += 'content-type:text/html;charset=utf8\n'
            client_header += '\n'

            response = client_header + client_body
            # # 设置一个响应头就换一行
            # client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
            # client_socket.send('\n'.encode('utf8'))

            # 给客户端返回消息
            client_socket.send(response.encode('utf8'))


def load_file(file_name, **kwargs):
    try:
        with open(file_name, 'r', encoding='utf8') as file:
            count = file.read()
            if kwargs:
                count = count.format(**kwargs)
            return count
    except FileExistsError:
        print('文件未找到!')


sever = MySever('0.0.0.0', 9000)
sever.run_forever()
