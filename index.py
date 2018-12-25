from flask import Flask, render_template, url_for, request
import os
import database
app = Flask(__name__)
schoolList = {}
#获取配置学校列表
f = open('conf/script.conf', mode='r')
for line in f:
    schoolList[line.split()[0]] = line.split()[1]

@app.route('/')
def index():
    datas = database.getNewData()
    return render_template('index.html', datas=datas, schoolList=schoolList)

@app.route('/school/<school>')
def get_school_news(school):
    if school not in schoolList.keys():
        return "no message"
    datas = database.getData(school)
    return render_template('newsList.html', datas=datas, schoolName=schoolList[school])

@app.route('/search/', methods=['POST'])
def search_school_news():
    error = None
    if request.method == 'POST':
        datas = database.searchData(request.form['keyword'])
        return render_template('newsList.html', datas=datas)

if __name__ == '__main__':
    app.run(host='0.0.0.0')