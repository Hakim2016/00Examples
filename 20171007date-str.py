import time
date_str = '2014-4-28'
date = time.strptime(date_str, '%Y-%m-%d')
print(date)
print(time.localtime(time.time()))