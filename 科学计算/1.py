import requests
from lxml import etree

url='http://hap.highly.com.cn/hap/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'Cookie': 'SESSIONID_HAP=e5aade62-c991-4dfe-b5be-c434f8dafe0c; JSESSIONID=16A0C71B729F1855144DA4EF3339904E; LRToken=99ef7c54e8aef051cf03aa8bc56d20749d9f021a61635ea8881ba91057696a0dc92ee308ea0ee85a1442d35d9a2d3d799bf27719f51c3baaf45306051c4b9d537d0c7c867183efaf4e384f58004b0951fa2fb7f210e0c284fbfc154489de51d2f0bcec56b09ed68b859940bccc84d088ad51a49ce16bd74f2aaa1180356adf82Host: hap.highly.com.cn'
}
requsest=requests.get(url=url,headers=headers)
print(requsest.text)
#  htmlx = etree.HTML(requsest.text)
# html_data=requsest.text.encode('iso-8859-1').decode('gbk')
# print(type(html_data))
# htmlx = etree.HTML(html_data)
# print(htmlx)

# x=htmlx.xpath('//div[@class="k-grid-content k-auto-scrollable"]/tr//td')
# print(x)