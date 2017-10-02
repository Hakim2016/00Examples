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
# zh_jsn_url = 'https://www.zhihu.com/api/v4/members/ke-ren-33-46/activities?limit=20&after_id=1504206499&desktop=True'
# zh_jsn_url = 'https://zhuanlan.zhihu.com/api/posts/29761037/comments?limit=10&offset=0'
data = session.get(url=zh_jsn_url, headers=headers).text
# print(type(data))
print('old = '+data)

# need to
data = data.replace('\\"', '\"')
data = data.encode('utf-8').decode('unicode_escape')
data_jsn = json.dumps(data,ensure_ascii=False)
print('new = '+data)
print(data_jsn)
# json_str = json.dumps(data,ensure_ascii=False)
# json_str = json.dumps(data, ensure_ascii=False, indent=4)#.encode('gb2312')
# print(json_str)

###########################################

# data = [{"a":"aaa","b":"bbb","c":[1,2,3,(4,5,6)]},33,'tantengvip',True]
# data2 = json.dumps(data)
# print(data2)
# f = open('./tt.txt','a')
# json.dump(data2,f)


###########################################
s = '\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'
print(s)

############################################
str = '{"error": {"message": "\u672a\u8bbe\u7f6e\u9a8c\u8bc1\u65b9\u5f0f", "code": 602}}'
print(str)
