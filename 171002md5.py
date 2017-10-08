import hashlib

str = 'abcdefg'
str = str.encode('gbk')
m = hashlib.md5()
m.update(str)
print(m.hexdigest())
print(m.digest())