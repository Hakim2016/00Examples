import urllib
import requests
import sys


# url = 'http://vcdn01.gayporntube.tv/video12/8/8e/cc08ec1746acb35da4ac11acdb519a8e.mp4?validfrom=1505825493&validto=1505870493&rate=1082k&hash=ruL89b6ULBrFAldvhuP14iHAxqM%3D'
# urllib.request.urlretrieve(url, 'D:/00python/fist.mp4')
url = 'https://yqall01.baidupcs.com/file/9be97b48e2e7b817920cd394c722af1c?bkt=p3-14009be97b48e2e7b817920cd394c722af1c665f86580000006d3a9f&fid=271491244-250528-861137420553556&time=1505915201&sign=FDTAXGERQBHSK-DCb740ccc5511e5e8fedcff06b081203-NfALLpffQY3zuB67amAqwuUiC9Q%3D&to=74&size=7158431&sta_dx=7158431&sta_cs=1&sta_ft=rar&sta_ct=4&sta_mt=4&fm2=MH,Yangquan,Netizen-anywhere,,shanghai,ct&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=14009be97b48e2e7b817920cd394c722af1c665f86580000006d3a9f&expires=8h&rt=pr&r=280182346&mlogid=6097565394942121431&vuk=271491244&vbdid=1331248354&fin=51CTO%E4%B8%8B%E8%BD%BD-crt.rar&fn=51CTO%E4%B8%8B%E8%BD%BD-crt.rar&rtype=1&iv=2&dp-logid=6097565395076339159&dp-callid=0.1.1&hps=1&tsl=0&csl=0&csign=DOfLsPqXfcw%2BKbsA4Vwx%2FIfSgxQ%3D&so=0&ut=1&uter=4&serv=0&uc=4236781674&ic=1748928515&ti=5325d25af8f94b43630fe3e45b1da596e96f8a660cdcca12&by=themis'

getFile = url
saveFile = 'D:/00python/vid-progress.rar'
fileName = 'vid-progress'
name = fileName

def report(count, blockSize, totalSize):
  percent = int(count*blockSize*100/totalSize)
  sys.stdout.write("\r%d%%" % percent + ' complete' + '['+ '%d'%count*blockSize*100 +'/'+ '%d'%totalSize +']')
  sys.stdout.flush()

sys.stdout.write('\rFetching ' + name + '...\n')
urllib.request.urlretrieve(getFile, saveFile, reporthook=report)
sys.stdout.write("\rDownload complete, saved as %s" % (fileName) + '\n\n')
sys.stdout.flush()