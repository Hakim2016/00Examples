import time
import os

# loc = 'd:/00python/path'
loc = 'e:/00python/path/01/02'
path = './others/'

if os.path.isdir(loc) & 1:
	print("This is a path")

print(os.path.isdir(loc) & 2)

# if os.path.exists(loc):
#     print("路径："+ loc + "存在")
# else:
#     print("Prepare to create this path")
#     # os.mkdir(loc)
#     os.makedirs(loc)

# with open('./README.md', 'r') as f:
#     print(f.read())

# if os.path.exists(path):
#     pass
# else:
#     print('this path need to create!')
#     os.makedirs(path)
# wrt = 'test for writing!'
# with open(path + 'write.txt', 'w') as f:
#     f.write(wrt)
