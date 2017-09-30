import time
import os

# time.strftime('%Y-%m-%d',time.localtime(time.time()))
ymd = time.strftime('%Y%m%d',time.localtime(time.time()))
loc = "d:\\00python\\" + time.strftime('%Y%m%d',time.localtime(time.time()))
print(time.time())
print(time.strftime('%Y%m%d',time.localtime(time.time())))
if os.path.exists(loc):
    print(loc + "存在")
else:
    print(loc + "不存在\n准备创建")
    os.mkdir(loc)

print(time.time())
print(time.localtime(time.time()))
print(str(int(time.time()*1000)))
# 1506403581410
# 1506475457172