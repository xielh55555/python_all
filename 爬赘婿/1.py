import requests
import re
import time
import pprint

url='http://www.paoshuzw.com/19/885/'
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
}
requstes=requests.get(url=url,headers=header)
# print(requstes.text)
dd=re.findall("<dd><a href='/0/885/(.*?)' >(.*?)</a></dd>",requstes.text)
# pprint.pprint(dd)
i=0
for dome in dd:
    try:
        i+=1
        print('正在下载第'+str(i)+'章：'+dome[1]+'....')
        url_1=dome[0]
        title_1=dome[1]
        urlall='http://www.paoshuzw.com/0/885/'+url_1
        # print(urlall)
        requstes=requests.get(url=urlall)
        requstes.encoding='utf-8'   
        x=re.findall(' <div id="content">(.*?)<p>',requstes.text)
        while 1==1:
            if x:
                x=x[0]
                x=x.replace('&nbsp;',' ').replace('<br />','\n')
                with open('zhuixu.word', mode='a', encoding='utf-8') as f:
                    f.write(dome[1])
                with open('zhuixu.word', mode='a', encoding='utf-8') as f:
                    f.write(x)
                break
            else:
                requstes=requests.get(url=urlall)
                requstes.encoding='utf-8'
                x=re.findall(' <div id="content">(.*?)<p>',requstes.text)

        
    except Exception as e:
        print(dome[1]+'下载失败！'+'*'*100)
        pprint.pprint(x)
        print(urlall)
        continue