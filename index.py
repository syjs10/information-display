from flask import Flask, render_template, url_for
import database
app = Flask(__name__)

@app.route('/')
def index():
    datas = database.getData('dongbeidaxue')
    base_url = url_for("static", filename='')
    return render_template('newsList.html', datas=datas, base_url=base_url);

@app.route('/school/<school>')
def get_school_news(school):
    data = database.getData('dongbeidaxue')
    return data[0]['title']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)