# -*- coding: utf-8 -*-
import requests
import urllib
import urllib3
import re

to_replace = 'http://vcdn01.gayporntube.tv/video2/0/0c/b75e14260c60ab7dd2fcc07a317dd20c.mp4?validfrom=1505670816&validto=1505715816&rate=839k&hash=yYxksfklpLPkjDQ433seTPfgM6g%3D'
url = 'http://vcdn01.gayporntube.tv/video16/a/a1/b5d06ec9a305df01d804304323b684a1.mp4?validfrom=1505636814&validto=1505681814&rate=596k&hash=%2FAs5kfUTo%2FvnNL9d4iCsZ%2FI6Sas%3D'
url2 = 'http://vcdn01.gayporntube.tv/video16/2/27/f0f41b164f7b80a322344aaf150f2a27.mp4?validfrom=1505660404&validto=1505705404&rate=676k&hash=dgneUR9jdOnJ6C5BumJz0E76nWg%3D'

amp_reg = re.compile('amp;')
replaced = amp_reg.sub('', to_replace)
print(replaced)