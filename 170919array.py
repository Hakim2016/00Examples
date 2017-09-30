import time
import os

lst_arr = [
    {
        'name':'zhangsan',
        'age':'23'
    },
    {
        'name':'lisi',
        'age':'24'
    }
]

lst_arr2 = [1,2,5,9]
print(len(lst_arr))
for i in range(len(lst_arr)):
    print(lst_arr[i]['name'])