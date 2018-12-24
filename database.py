from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.info

# 无重复插入数据
def insertData(school, dataList):
    my_set = db[school]
    for one in dataList:
        my_set.update(one, {'$set':one}, True)
# 按学校获取数据
def getData(school):
    dataList = []
    my_set = db[school]
    for data in my_set.find():
        dataList.append(data)
    return dataList
