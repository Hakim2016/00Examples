import pymysql as mysql

# open database
conn = mysql.connect(host='localhost', user='root', passwd='root', db='mysql', port=3306)
print(conn.server_status)

# user cursor() to get cursor operation
cursor = conn.cursor()

# SQL insert into table employee
sql = """
    select host, user from user
"""

try:
    # execute this sql
    cursor.execute(sql)

    data = cursor.fetchall()
    # commit to mysql datebase to execute
    # db.commit()
    print(data)
except:
    print('error happens')
    # if err happens rollback
    conn.rollback()
finally:
    if conn:
        conn.close()
    pass