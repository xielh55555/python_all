import requests
import re
import time
import pprint
from lxml import etree
# !   https://www.ximalaya.com/youshengshu/3416829/p39/
#! https://audiopay.cos.tx.xmcdn.com/download/1.0.0/group1/M06/D4/2D/wKgJN1vXKf_CgnfwAIr4D9tT5eY940.m4a?buy_key=111962652672&sign=c0ef0f4ba08a446a8d128ff1c8b897de&token=9890&timestamp=1614916194&duration=1124
#! https://audiopay.cos.tx.xmcdn.com/download/1.0.0/group1/M06/D4/2D/wKgJN1vXKf_CgnfwAIr4D9tT5eY940.m4a?buy_key=111962652672&sign=c0ef0f4ba08a446a8d128ff1c8b897de&token=9890&timestamp=1614916194&duration=1124
#! https://audiopay.cos.tx.xmcdn.com/download/1.0.0/group1/M0A/D4/2D/wKgJN1vXKhLBSrX9ANIkZjRNKtE522.m4a?buy_key=111962652672&sign=d47980f37fecf13684d7995d36ecc3fa&token=2984&timestamp=1614916551&duration=1701
#! https://audiopay.cos.tx.xmcdn.com/download/1.0.0/group1/M0A/D4/2D/wKgJN1vXKhLBSrX9ANIkZjRNKtE522.m4a?buy_key=111962652672&sign=d47980f37fecf13684d7995d36ecc3fa&token=2984&timestamp=1614916551&duration=1701
#! https://audiopay.cos.tx.xmcdn.com/download/1.0.0/group5/M09/D0/7B/wKgPE17pppuR5OFYAGNz-Bpdrv0649.m4a?buy_key=111962652672&sign=fd312da3473eea160f1a217bf163f1a7&token=2129&timestamp=1614916856&duration=804
page=''
y=1
for i in range(1):

    url='https://www.ximalaya.com/youshengshu/3416829/'+page
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
    }
    req=requests.get(url=url,headers=headers)
    req.encoding='utf-8'
    htmlx = etree.HTML(req.text)
    li=htmlx.xpath('//div[@class="sound-list _is"]//ul//li[@class="lF_"]//a')
    for li_1 in li:
        # print(li_1)
        li_title=li_1[0].text
        li_href=li_1.get('href')
        print(li_title,li_href)
    y+=1
    page='p'+str(y)