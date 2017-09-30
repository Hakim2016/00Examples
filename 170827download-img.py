import requests
import time
import os

agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = {
    'Host': 'www.zhihu.com',
    'Origin': 'https://www.zhihu.com',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': agent
}


session = requests.session()
curr_sec = str(int(time.time()*1000))
captcha_url = 'http://www.zhihu.com/captcha.gif?r='+curr_sec+'&type=login&lang=cn'
print(captcha_url)
# r = requests.get(captcha_url)
r = session.get(url=captcha_url,headers=headers)
with open('captcha_zhihu.png', 'wb') as f:
    f.write(r.content)
    f.close()