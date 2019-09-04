python版本3.6
1.进入项目目录执行pip3 install -r requirements.txt
2.启动本地mysql，默认用户root，密码123456，可以根据自己的mysql配置更改
3.登陆mysql，创建数据库create database deployment，注意字符集为utf-8
4.初始化数据库python manager.py create_db
5.启动python manager.py runserver
6.如果想重制数据库python manager.py drop_db
