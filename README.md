# dbbackup-multiple
### 介绍

整合网上的教程。写了一个自动备份mysql的python脚本。

### 功能
1. 可以同时备份多个数据库。
2. 可以设置保留最后几个备份，多出的删除。

### 使用

DBS = [{'DB_HOST' : 'localhost', 'DB_USER' : 'USERNAME','DB_USER_PASSWORD':'PASSWORD','DB_NAME':'NAME' },
{'DB_HOST' : 'localhost', 'DB_USER' : 'USERNAME','DB_USER_PASSWORD':'PASSWORD','DB_NAME':'NAME' }];

只需要配置好多个数据库。然后把python加到 linux 或 windows 计划任务

###linux 计划任务使用方法。

先ssh到主机

1. 把py文件通过ftp到服务器:
2. 输入sudo crontab -e
3. 在后面加上每天凌晨2点运行
4. 0 2 * * * /usr/bin/python dbbackup.py

