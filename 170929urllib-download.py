# -*- coding: utf-8 -*-
import requests
import re
import urllib
import urllib3

# vid_reg = re.compile('\d')
# vid_reg = re.compile('source src=\"(.*?)\" type=\"video/mp4\"', re.S)
header = {
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Origin': 'http://www.gayporntube.tv',
    'Range': 'bytes=32768-',
    'Referer': 'http://www.gayporntube.tv/movies/1116502/bare-interracial',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
pageurl = 'http://www.gayporntube.tv'
page = requests.get(pageurl, headers = header)
vid_reg = re.compile('source src=\"(.*?)\" type=\"video/mp4\"')
url = 'http://www.gayporntube.tv/movies/1116502/bare-interracial'

r = requests.get(url, headers=header)
print(r.status_code)
contents = vid_reg.findall(r.text)[0]
print(contents)
r3 = urllib.request.urlopen(contents)
print("r3 status code = " + r3.status_code)
r2 = requests.get(contents, headers=header)
print(r2.status_code)
print(contents)
urllib.request.urlretrieve(contents, "D:/00python/hakim.mp4")
