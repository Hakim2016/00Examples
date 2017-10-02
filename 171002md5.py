import hashlib

str = '0513865210hjj'
str = str.encode('gbk')
m = hashlib.md5()
m.update(str)
print(m.hexdigest())
print(m.digest())