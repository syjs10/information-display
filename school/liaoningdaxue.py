# _*_ cording:utf-8 _*_
from bs4 import BeautifulSoup
import requests
def excute():
    data = []
    url = "http://kjc.lnu.edu.cn/cgtg.htm"
    wb_data = requests.get(url)
    wb_data.encoding = 'utf8'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    infoList = soup.select('.winstyle12592')[0].select('tr')
    for one in infoList:
        item = {}
        newOne = one.select('a.c12592')
        if len(newOne) == 0:
            continue
        item['url'] = 'http://kjc.lnu.edu.cn/'+newOne[0]['href']
        item['title'] = newOne[0].get_text()
        item['date'] = one.select('span.timestyle12592')[0].get_text().strip()
        data.append(item)
    return data
