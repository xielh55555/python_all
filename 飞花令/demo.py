import requests
from lxml import etree
import re

def fhl(key):
    url='https://www.gushici.net/chaxun/all/{}'.format(key)
    req=requests.get(url=url)
    req.encoding='utf-8'
    pa=etree.HTML(req.text).xpath('/html/body/div[2]/div[1]/div[1]/span//text()')[0]
    page1=re.findall('\/\s(\d*)',pa)[0]
    print(page1)
    for i in range(1,int(page1)+1):
        url='https://www.gushici.net/chaxun/all/{}/{}'.format(key,i)
        req=requests.get(url=url)
        req.encoding='utf-8'
        pap=etree.HTML(req.text).xpath('/html/body/div[2]/div[1]/div[@class="gushici"]')
        for pa in pap:
            title=''.join(pa.xpath('div[1]/p[1]/a/b//text()')).strip()
            source=''.join(pa.xpath('div[1]/p[2]//text()')).strip()
            shici=''.join(pa.xpath('div[1]/div//text()')).strip()
            print(title,source,shici)
     
if __name__ == '__main__':
    key=input('请输入关键字：')
    fhl(key)
    

