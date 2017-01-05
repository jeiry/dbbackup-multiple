# dbbackup-multiple
### 介绍

自动备份mysql的python脚本。可以同时备份多个数据库。

### 使用

DBS = [{'DB_HOST' : 'localhost', 'DB_USER' : 'USERNAME','DB_USER_PASSWORD':'PASSWORD','DB_NAME':'NAME' },
{'DB_HOST' : 'localhost', 'DB_USER' : 'USERNAME','DB_USER_PASSWORD':'PASSWORD','DB_NAME':'NAME' }];
只需要配置好多个数据库。然后把python加到 linux 或 windows 计划任务

###linux 计划任务使用方法。

先ssh到主机

把py文件通过ftp到服务器:
输入
sudo crontab -e
在后面加上每天凌晨2点允许
0 2 * * * /usr/bin/python dbbackup.py

