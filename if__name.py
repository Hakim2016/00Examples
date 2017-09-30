"""
__name__ 是每一个python文件都包含的内置变量"
当前文件运行时__name__ 等于 "文件名.py"

在其他问价中引用该包
__name__ 就显示该文件的文件名 "if__name" 不存在后缀
"""

print("I am the 1st")

print("__name__ is " + __name__)

if __name__ == '__main__':
    print("I am the 2nd")