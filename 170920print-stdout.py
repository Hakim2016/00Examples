import time
import sys

str = 'Hello Hakim'
# conclusion: print(str) = sys.stdout.write(str + '\n')
print('print Hakim')
print('print Hakim2')

sys.stdout.write('stdout Hakim')
sys.stdout.write('stdout Hakim2' + '\n')

print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})

print('%(a)s is happy who has %(b)d hobbies' % {'a':'Hakim', 'b':3})

percent = 20
sys.stdout.write("\r%d%%" % percent + ' complete')
sys.stdout.flush()

for i in range(3):
    sys.stdout.write('\rstdout Hakim ' + '%d'%i)  # 或者用：print '\b\b\b\b', i,
    time.sleep(0.5)
    sys.stdout.flush()
print()

for i in range(5):
    print('%d'%i)
    time.sleep(0.5)
    sys.stdout.flush()#刷新输出 linux 下是必须的
