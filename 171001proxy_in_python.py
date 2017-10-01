import requests
import re
from bs4 import BeautifulSoup

proxies = {
	'http': 'http://71346904:h71346904@g-proxy.hitachi.cn:8080',
	'https': 'https://71346904:h71346904@g-proxy.hitachi.cn:8080'
}
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {
	'Host':'www.baidu.com',
	'Referer':'https://www.baidu.com/',
	'User-Agent':agent,
	'X-Requested-With':'XMLHttpRequest'
}
url = 'http://www.baidu.com'
r=requests.get(url, headers=headers, proxies=proxies)
soup = BeautifulSoup(r.text, 'html.parser')

print(r.status_code)
print(soup)