import math
import random
def get_callback():
    loopabc = '0123456789abcdefghijklmnopqrstuvwxyz'
    prefix = "bd__cbs__"
    n = math.floor(random.random() * 2147483648)
    a = []
    i = 1
    while n != 0:
        print(i)
        print('Before n = '+str(n))
        a.append(loopabc[n % 36])
        print(a)
        n = n // 36
        print('After n = '+str(n))
        i=i+1
    a.reverse()
    callback = prefix + ''.join(a)
    return callback

if __name__ == '__main__':
    # print(get_callback())
    n = math.floor(random.random() * 2147483648)
    rd = random.random()
    rd_int = rd * 2147483648
    flr = math.floor(rd_int)
    print(rd)
    print(rd_int)
    print(flr)
    n = flr
    # print('####################')
    pass