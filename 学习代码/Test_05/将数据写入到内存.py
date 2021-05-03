from io import StringIO, BytesIO

s_io = StringIO()

s_io.write('hello')     # 将数据写入到缓存中
print(' world', file=s_io)   # 将数据写入到缓存中

b_io = BytesIO()
b_io.write('hello'.encode('utf8'))

print(b_io.getvalue().decode('utf8'))
print(s_io.getvalue())  # 将数据打印出来

s_io.close()
b_io.close()
