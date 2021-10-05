import requests
import re
from lxml import etree

shci = ''
url = 'https://so.gushiwen.cn/gushi/shijing.aspx'
response = requests.get(url=url)
# print(response.text)
chars = re.findall('<span><a href="(.*?)" target="_blank">(.*?)</a></span>', response.text)
# print(chars)
for char in chars:
    try:
        char_li = char[0]
        url_all = 'https://so.gushiwen.cn' + char_li
        response_all = requests.get(url_all)
        # print(response_all)
        chars_all = re.findall(
            '<textarea style=" background-color:#F0EFE2; border:0px;overflow:hidden;" cols="1" rows="1" id="(.*?)">(.*?)——(.*?)《(.*?)》https://so.gushiwen.cn/shiwenv_(.*?).aspx</textarea>',
            response_all.text)[0]

        data_shiming = chars_all[3]
        data_zuozhe = chars_all[2]
        data_shici = chars_all[1]


        print('正在下载：', data_shiming)
        data_yiwen = re.findall('<p>译文<br />(.*?)</p>', response_all.text)[0]
        data_yiwens=data_yiwen.replace('<br />',"")
        # print(data_yiwen)
        shci = shci + '\n' + '                        ' + data_shiming + '\n' + '[' + data_zuozhe + ']' + '\n' + data_shici + '\n' + '\n' + '译文：' + data_yiwens + '\n'

    except Exception as e:
        continue
with open('shijin.word', mode='w', encoding='utf-8') as f:
    f.write(shci)
