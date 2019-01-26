# _*_ cording:utf-8 _*_
import os
import database
f = open('conf/script.conf', mode='r')
for line in f:
    scriptName = line.split()[0]
    exec('from school.'+scriptName+' import excute')
    data = excute()
    database.insertData(scriptName,data)
f.close()


