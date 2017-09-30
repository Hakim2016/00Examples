import time
import os

# loc = 'd:/00python/path'
loc = 'd:/00python/path/01/02'

if os.path.exists(loc):
    print("路径："+ loc + "存在")
else:
    print("Prepare to create this path")
    # os.mkdir(loc)
    os.makedirs(loc)
