import os
file_name = input('请输入文件路径：')
if os.path.isfile(file_name):

    old_file = open(file_name, 'rb')

    names = os.path.splitext(file_name)     # (,)
    new_file_name = names[0] + '.bak' + names[1]

    new_file = open(new_file_name, 'wb')

    while True:
        coutend = old_file.read(1024)
        # 把旧文件里的内容读取到新文件中
        new_file.write(coutend)
        if not coutend:
            break

    old_file.close()
    new_file.close()
else:
    print('文件不存在')

