import requests
import re
from lxml import etree
url='http://www.xbiquge.la/10/10489/'
req=requests.get(url=url)
req.encoding='utf-8'
req_xp=etree.HTML(req.text)
li=req_xp.xpath('//*[@id="list"]/dl/dd/a')
i=0
for li_1 in li:
    li_title=li_1.text
    li_href=li_1.get('href')
    url_all='http://www.xbiquge.la/10/10489/'+li_href.split('/')[-1]
    req_all=requests.get(url=url_all)
    req_all.encoding='utf-8'
    list_data=re.findall('<div id="content">(.*?)<p>',req_all.text)
    list_data=str(li_title)+'\n'+list_data[0].replace('&nbsp;','').replace('<br />','\n')
    i+=1
    print('正在下载{}......'.format(li_title))
    with open('C:\\电脑\\趣儿编备课\\PYTHON\\PYTHON\\三寸天堂\\三寸天堂\\'+ str(i) + str(li_title)+'.txt',mode='a',encoding='utf-8') as f :
        f.write(list_data)
