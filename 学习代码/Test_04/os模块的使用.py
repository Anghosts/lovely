import os

print(os.name)  # 操作系统的名字   windows为 nt ，非windows为 posix
print(os.sep)   # 路径的分隔符    Windows为 \ ，非Windows为 /

print(os.path.abspath('file.csv'))  # 获取文件的绝对路径

print(os.path.isdir('file.csv'))    # 判断是否是文件夹

print(os.path.isfile('__init__.py'))    # 判断是否是文件

print(os.path.exists('file.csv'))   # 判断文件是否存在

# 获取文件的后缀
file_name = '2002.1.3.py'
print(os.path.splitext(file_name))
