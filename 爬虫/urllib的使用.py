import urllib
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

url = 'https://movie.douban.com/top250?start='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
# req = {
#     'req': '{"sid":"nHimsCdsUfH22XR3pp0b800xIe8y1PGS", "user":{"user_id":28998310, "username":"伴阴凉", "urlname":"gr98gfy6ab", "avatar":{"id":107985900, "farm":"farm1", "bucket":"hbimg", "key":"996808d96e82abc809c1d5fcb5deabba777498975b-GDB4uy", "type":"image/png", "height":"100", "width":"100", "frames":"1"}, "rating":8191, "bindings":{"qzone":"qzone-A76E12427B2BD3A7451CB2E3A14A8AD6"}, "profile":{}, "status":{"newbietask":0, "featuretask":11, "invites":0, "share":0}, "extra":{"job_id":999}, "board_count":9, "pin_count":284, "like_count":0, "boards_like_count":1, "follower_count":9, "following_count":25, "creations_count":0, "is_huhua":false, "is_pro":false}, "ongoing_activities":[{"activity_id":117, "seq":116, "title":"《梦幻西游》手游门派NPC设计大赛", "status":1, "extra":{"thumb_image":{"bucket":"hbfile", "key":"6851dfcff87b17741473380e4998787f12b6d59d531d8"}, "url":"http://event.huaban.com/art/116/"}, "created_at":1618934400, "expired_at":1623254340}, {"activity_id":118, "seq":117, "title":"AGON虚拟形象有奖征集大赛", "status":1, "extra":{"thumb_image":{"bucket":"hbfile", "key":"54399cc5c295a6a59db9a367e9f325aa025e09444a2d19"}, "url":"http://event.huaban.com/art/117/"}, "created_at":1619366400, "expired_at":1621958340}, {"activity_id":116, "seq":115, "title":"宋城-国潮神兽节游戏原画征集大赛", "status":1, "extra":{"thumb_image":{"bucket":"hbfile", "key":"555e64123983a41d4b3dce88dda247f48d9d476c41937"}, "url":"http://event.huaban.com/art/113/"}, "created_at":1612001580, "expired_at":1620230340}], "ads":{"1":{"promotion":{"id":9, "name":"live_2663_梵高"}, "position":{"id":1, "name":"pc-吸顶", "alias":"top", "slide":false, "width":2000, "height":null, "closable":true}, "showcase":{"id":181, "closable":false}, "material":{"type":"image", "showcase_id":181, "id":1786, "link":"http://live.huaban.com/live/2663?utm_source=huaban&utm_medium=top&utm_campaign=ads-2663", "width":2000, "tracker":null, "tag":"课程", "data":{"id":664, "name":"吸顶 2000×60.jpg", "length":99589, "bucket_name":"hbimg-other", "bucket_key":"8b245ba436f9cea1017d8a170e3d844950a0354216197467050Ty1BlNl", "content_type":"image/jpeg", "created_at":"2021-04-30T01:38:26.119441Z", "metadata":{"frames":1, "width":2000, "height":60}}, "weight":100, "height":60}}, "19":{"promotion":{"id":22, "name":"导航右侧打底"}, "position":{"id":19, "name":"pc-导航条-右侧", "alias":"navi", "slide":false, "width":null, "height":32, "closable":false}, "showcase":{"id":95, "closable":false}, "material":{"type":"html", "showcase_id":95, "id":785, "link":"http://live.huaban.com/?utm_source=huaban&utm_medium=navi-login&utm_campaign=resident&utm_content=pa", "width":null, "tracker":null, "tag":"", "data":"<div class=\"hr--prom nav-tab\">\n<img src=\"/img/navigator/live.svg\" style=\"\n    padding: 4px 0;\n\">\n</div>", "weight":10, "height":32}}}, "notifications":undefined, "notificationsRead":undefined, "unread_messages":86, "unread_mentions":0, "unread_activities":86, "unread_dm":51, "unread_system_dm":51};'
# }
# data = bytes(urlencode(req), encoding='utf8')

request = Request(url, headers=headers)
try:
    # timeout: 超时处理
    response = urlopen(request, timeout=3)

    # 打印User-Agent
    # print(request.get_header('User-agent'))

    # 获取响应头
    # print(response.getheaders())

    # 获取状态码
    # print(response.status)

    # 获取html信息
    info = response.read()
    print(info.decode('utf8'))

except urllib.error.URLError as e:
    print("time out!")
