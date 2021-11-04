import requests, re, os

bv = 'BV1ZA41137TE'
url = 'https://www.bilibili.com/video/{}?spm_id_from=333.851.b_7265636f6d6d656e64.2'.format(bv)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Referer': 'https://www.bilibili.com/video/{}'.format(bv)
}

response = requests.get(url, headers=headers).text

title = re.findall(r'<title data-vue-meta="true">(.*?)</title>', response)[0]
print(title)
video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"', response)[0]
audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"', response)[0]

print('正在下载视频...')
v = requests.get(video_url, headers=headers).content
print('正在下载音频...')
a = requests.get(audio_url, headers=headers).content

title = re.sub('_哔哩哔哩 \(゜-゜\)つロ 干杯~-bilibili', '', title)
print(title)
if not os.path.exists(title):
    os.mkdir(title)
f = open('{}/video.mp4'.format(title), 'wb')
f.write(v)
f2 = open('{}/audio.mp3'.format(title), 'wb')
f2.write(a)
