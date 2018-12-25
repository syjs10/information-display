from pymongo import MongoClient
import datetime
import dateutil.parser
import re
conn = MongoClient('127.0.0.1', 27017)
db = conn.info

# 无重复插入数据
def insertData(school, dataList):
    my_set = db.school
    for one in dataList:
        one['school']=school
        one['date'] = dateutil.parser.parse(one['date']).strftime("%Y-%m-%d")
        my_set.update(one, {'$set':one}, True)
# 按学校获取数据
def getData(school):
    dataList = []
    my_set = db.school
    for data in my_set.find({'school':school}):
        dataList.append(data)
    return dataList
def getNewData():
    dataList = []
    my_set = db.school
    for data in my_set.find():
        dataList.append(data)
    dataList.sort(key=lambda data:data['date'], reverse=True)
    return dataList
def searchData(keyword):
    dataList = []
    my_set = db.school
    for data in my_set.find({'title':{'$regex':keyword}}):
        dataList.append(data)
    return dataList
