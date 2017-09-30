import requests
import os

dir = "D://00python//pics//"
url = "http://img0.dili360.com/rw9/ga/M01/49/84/wKgBy1muH-iAbYO2AARbOIF1-EU776.tub.jpg"
saveto = dir + url.split('/')[-1]

print saveto
# print url.split('/')

try:
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.exists(saveto):
        r = requests.get(url)
        with open(saveto,'wb') as f:
            f.write(r.content)
            f.close()
            print "pic save success"
    else:
        print "pic already exist"
except:
    print "fail to get the pic"