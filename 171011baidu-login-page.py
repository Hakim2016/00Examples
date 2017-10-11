import requests
from _10python._Common.Utility import output_html

# login_url = 'https://passport.baidu.com/v2/'
pan_url = 'https://pan.baidu.com/'
# login_url = 'https://passport.baidu.com/v2/?login'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache - Control': 'max-age = 0',
    'Connection': 'keep-alive',
    'Host': 'pan.baidu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': agent
}
session = requests.session()
ss = session.get(pan_url, headers=headers)
print(ss.cookies)
ss.encoding = 'utf-8'
output_html(ss.text, 'pan_lohin.html')
