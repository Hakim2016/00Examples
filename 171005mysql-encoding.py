import pymysql as mysql
import traceback

def encdCHAR(str):
    type(str)
    return str.encode('utf8')

# open database
conn = mysql.connect(host='localhost', user='root', passwd='root', db='testdb', port=3306, charset='utf8')

# user cursor() to get cursor operation
cursor = conn.cursor()

# SQL insert into table employee
sql = "insert into employee(first_name, last_name, age, sex) values(%s, %s, %s, 'M')"
# params = ("晶晶".encode('utf-8'),"何".encode('utf-8'))
params = ("晶晶 san","何", 5)
# params = ("晶晶".decode('gbk').encode('utf-8'),"何".decode('gbk').encode('utf-8'))
# "".encode().decode()
# "晶晶".encode('utf-8')

try:
    # execute this sql
    cursor.execute(sql, params)
    # cursor.execute(sql)
    # commit to mysql datebase to execute
    conn.commit()
except:
    print('error happens')
    traceback.print_exc()
    # if err happens rollback
    conn.rollback()

# close the connecttion
conn.close()