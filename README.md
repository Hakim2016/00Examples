# 00Examples

30-Sep-2017 First submit examples to Github!

05-Oct-2017
    catch exception import traceback
    insert into table with Chinese characters
    encoding settings
    1 conn = mysql.connect(host='localhost', user='root', passwd='root', db='testdb', port=3306, charset='utf8')
    2 encode the Chinese characters
        "好好学习天天向上".decode('gbk').encode('utf8')  for python2 not python3

     drop table employee;
     CREATE TABLE IF NOT EXISTS `employee`(
           `first_name` VARCHAR(100) NOT NULL,
           `last_name` VARCHAR(40) NOT NULL,
           `age` int(2),
           `sex` char(2)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;
     show create table employee;

06-Oct-2017
COMMAND WINDOW:
insert into employee(first_name, last_name, age, sex) values('晶晶', 'gtdfdfdfsfddfsdsfs', 24, 'M');
error 1366 Chinese characters insert error.
set names gbk;
then fixed.

Python insert into mysql via pymysql
insert success, Chinese characters displayed in unreadable code.
myabe this code "set names gbk" help a lot

show full columns from employee;
show create table employee;
alter table employee character set gbk;