# _*_ cording:utf-8 _*_
from bs4 import BeautifulSoup
import requests
def excute():
    data = []
    url = "http://neunews.neu.edu.cn/campus/part/XKJS.html"
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    infoList = soup.select('.ny_middle')[0].select('li')
    for one in infoList:
        item = {}
        item['url'] = 'http://neunews.neu.edu.cn'+one.select('a')[0]['href']
        item['title'] = one.select('a')[0].get_text().strip('·').strip()
        item['date'] = one.select('span')[0].get_text().strip('·').strip()
        data.append(item)
    return data

