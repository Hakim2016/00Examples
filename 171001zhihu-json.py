import requests
import http.cookiejar as cookielib
import json

agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = {
	'accept':'application/json, text/plain, */*',
	'Accept-Encoding':'gzip, deflate, sdch, br',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
	'Connection':'keep-alive',
	'Host':'zhuanlan.zhihu.com',
	'Referer':'https://zhuanlan.zhihu.com/p/29807392',
	'User-Agent':agent,
	'x-udid':'"AJBCjhC4dQyPTletgT0S1vi9dMqlQg_VuwU=|1506838418"',
	'x-xsrf-token':'2|f3d009f8|f936cb7b5f44268de58b4acf6515492e|1506838423'
}
######构造用于网络请求的session
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')

try:
	session.cookies.load(ignore_discard=True)
except Exception as e:
	pass

###########################################
zh_jsn_url = 'https://zhuanlan.zhihu.com/api/recommendations/posts?limit=3&seed=99'
data=session.get(url=zh_jsn_url, headers=headers).text
print(data)
json_str = json.dumps(data,ensure_ascii=False)
print(json_str)
