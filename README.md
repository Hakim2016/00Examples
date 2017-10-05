# 00Examples

30-Sep-2017 First submit examples to Github!

05-Oct-2017
    catch exception import traceback
    insert into table with Chinese characters
    encoding settings
    1 conn = mysql.connect(host='localhost', user='root', passwd='root', db='testdb', port=3306, charset='utf8')
    2 encode the Chinese characters
        "好好学习天天向上".decode('gbk').encode('utf8')