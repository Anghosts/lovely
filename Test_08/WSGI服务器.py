from wsgiref import simple_server
from wsgiref.simple_server import make_server


def show_login():
    return '登录页面'


def show_register():
    return load_file('注册.html', city='湖南永州')


def info():
    return load_file('首页.html')


def error():
    return '页面不存在'


def download_file():
    return '下载文件'


url = {
    '/': info,
    '/login': show_login,
    '/register': show_register,
    '/download': download_file
}


# 第 0 个参数, 表示环境(电脑的环境；请求路径相关的环境)
# 第 1 个参数, 是一个函数，用来返回响应头
def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    status_code = '200 OK'
    print('path: {}'.format(path))

    method = url.get(path)
    if method:
        response = method()
    else:
        status_code = '404 Not Found'
        response = error()

    # 响应头
    start_response(status_code, [('Content-Type', 'text/html;charset=utf8')])
    return [response.encode('utf8')]  # 浏览器显示的内容


def load_file(file_name, **kwargs):
    try:
        with open(file_name, 'r', encoding='utf8') as file:
            count = file.read()
            if kwargs:
                count = count.format(**kwargs)
            return count
    except FileExistsError:
        print('文件未找到!')


if __name__ == '__main__':
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")

    # # 打开浏览器，并在浏览器里输入http://localhost:8000/xyz?abc地址
    # import webbrowser
    # webbrowser.open('http://localhost:8000/xyz?abc')

    # 只处理一次请求
    # httpd.handle_request()  # serve one request, then exit
    # 服务器一直运行
    httpd.serve_forever()
