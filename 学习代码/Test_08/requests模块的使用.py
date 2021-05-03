import requests

url = 'https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login_window'
r = requests.get(url)
# print(r)  # 结果是Response对象

# 获取源码
# print(r.content.decode('utf8'))
print(r.text)

print(r.status_code)  # 状态码
