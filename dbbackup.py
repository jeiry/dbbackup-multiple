#!/usr/bin/python
###########################################################
#
# This python script is used for mysql database backup
# using mysqldump utility.
# update by jeiry 05/01/2017
# it can backup multiple database in one loops
#
##########################################################

# Import required python libraries
import os
import time
import datetime

# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup.
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databses names one on each line and assignd to DB_NAME variable.
DBS = [{'DB_HOST' : 'localhost', 'DB_USER' : 'USERNAME','DB_USER_PASSWORD':'PASSWORD','DB_NAME':'NAME' },
{'DB_HOST' : 'localhost', 'DB_USER' : 'USERNAME','DB_USER_PASSWORD':'PASSWORD','DB_NAME':'NAME' }];
BACKUP_PATH = '/backup/dbbackup/'
LIMIT = 5
# Getting current datetime to create seprate backup folder like "12012013-071334".
DATETIME = time.strftime('%m%d%Y-%H%M%S')


    
def manageFolder(DB_NAME):
    compareBackupPath = BACKUP_PATH + DB_NAME
    iterms = os.listdir(compareBackupPath)
    iterms.sort()  
    iterms.reverse()
    print iterms
    i = 0
    for filename in iterms:
        if i < LIMIT:
            print filename
        else:
            __import__('shutil').rmtree(BACKUP_PATH + DB_NAME + '/'+filename)
            print 'delete'+filename
        i += 1



# Checking if backup folder already exists or not. If not exists will create it.
print "creating backup folder"
def createFolder(TODAYBACKUPPATH):
    if not os.path.exists(TODAYBACKUPPATH):
        os.makedirs(TODAYBACKUPPATH)


# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
def databaseBackUp(DB_NAME,DB_USER,DB_USER_PASSWORD,TODAYBACKUPPATH):
    print "checking for databases names file."
    if os.path.exists(DB_NAME):
        file1 = open(DB_NAME)
        multi = 1
        print "Databases file found..."
        print "Starting backup of all dbs listed in file " + DB_NAME
    else:
        print "Databases file not found..."
        print "Starting backup of database " + DB_NAME
        multi = 0

    # Starting actual database backup process.
    if multi:
       in_file = open(DB_NAME,"r")
       flength = len(in_file.readlines())
       in_file.close()
       p = 1
       dbfile = open(DB_NAME,"r")

       while p <= flength:
           db = dbfile.readline()   # reading database name from file
           db = db[:-1]         # deletes extra line
           dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
           os.system(dumpcmd)
           p = p + 1
       dbfile.close()
    else:
       db = DB_NAME
       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
       os.system(dumpcmd)

    print "Backup script completed"
    print "Your backups has been created in '" + TODAYBACKUPPATH + "' directory"
    
    
#backup loop
for subDB in DBS: 
    TODAYBACKUPPATH = BACKUP_PATH + subDB['DB_NAME'] + '/'+DATETIME
    createFolder(TODAYBACKUPPATH)
    manageFolder(subDB['DB_NAME'])
    databaseBackUp(subDB['DB_NAME'],subDB['DB_USER'],subDB['DB_USER_PASSWORD'],TODAYBACKUPPATH)
    print subDB