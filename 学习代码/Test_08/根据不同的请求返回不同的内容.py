import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 8090))
server_socket.listen(128)
while True:
    client_socket, client_addr = server_socket.accept()

    # 从客户端的 socket 获取数据
    data = client_socket.recv(1024).decode('utf8')
    print('接收到{}的访问:\n{}'.format(client_addr[0], data))

    path = ''
    if data:
        path = data.splitlines()[0].split(' ')[1]
        print('请求为:{}'.format(path))
    client_header = 'HTTP/1.1 200 OK\n'
    if path == '/register':
        client_body = '欢迎来到注册页面！'
    elif path == '/login':
        client_body = '欢迎来到登录页面！'
    elif path == '/':
        client_body = '<h1 style="text-align: center;background-color: red;color: rgb(255,255,255);">欢迎来到我的首页！</h1>'
    else:
        client_header = 'HTTP/1.1 404 Page Not Found\n'
        client_body = '<h4 style="text-align: center;">对不起，您访问的页面不存在！</h4>'

    client_header += 'content-type:text/html;charset=utf8\n'
    client_header += '\n'

    response = client_header + client_body
    # # 设置一个响应头就换一行
    # client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
    # client_socket.send('\n'.encode('utf8'))

    # 给客户端返回消息
    client_socket.send(response.encode('utf8'))
