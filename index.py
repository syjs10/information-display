from flask import Flask, render_template, url_for
import os
import database
app = Flask(__name__)
schoolList = []
#获取配置学校列表
f = open('conf/script.conf', mode='r')
for line in f:
    data = {}
    data['scriptName'] = line.split()[0]
    data['schoolName'] = line.split()[1]
    schoolList.append(data)

@app.route('/')
def index():
    datas = database.getData('dongbeidaxue')
    return render_template('newsList.html', datas=datas);

@app.route('/school/<school>')
def get_school_news(school):
    for one in schoolList:
        if school not in one.values():
            return "no message"
    datas = database.getData(school)
    return render_template('newsList.html', datas=datas);

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)