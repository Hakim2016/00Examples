# 元组类型
categories = ((1, '无标签'), (2, '词根词缀'), (3, '中口背诵单词'), (4, '新概念3'), (5, 'ebs'), (6, '黄老师翻译'), (7, 'sherlock holmes'))
cates = {}

# categories = ('hakim', 'zhangsan')
for x in categories:
    cates[x[1]] = x[0]

print(cates)
print(cates['无标签'])

fruit_dict = {'apple':1, 'banana':2, 'orange':3}

#将字典的key转换为元组:
xyz = tuple(fruit_dict)
#将字典的value转换为元组:
# tuple(fruit_dict.value())
print(xyz)

#将字典的key转换为列表:
xyz = list(fruit_dict)
#将字典的value转换为列表:
# list(fruit_dict.value())
print(xyz)

#附：
#将字典转换为字符串：
xyz = str(fruit_dict)
print(xyz)