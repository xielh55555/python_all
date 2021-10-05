import urllib.request
import json
import os
import re
 
# 皮肤下载地址
skin_link = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
# 英雄主页
hero_link = 'https://pvp.qq.com/web201605/herodetail/'
# 英雄数据文件
json_link = 'https://pvp.qq.com/web201605/js/herolist.json'
# 载入英雄数据
json_data = urllib.request.urlopen(json_link)
# 获取英雄列表
hero_list = json.loads(json_data.read().decode('utf-8'))
# 显示英雄数量
print('本次共抓取到' + str(len(hero_list)) + '个英雄数据')
# 询问保存路径
r = True
while r:
    des_dir = input('请输入想要保存的路径：')
    if des_dir == '':
        print('不能为空')
    if des_dir != '':
        if not os.path.exists(des_dir):
            os.mkdir(des_dir)
        r = False
 
for hero in hero_list:
    hero_name = hero['cname']
    ename = str(hero['ename'])
    print('正在下载' + hero_name)
 
    # 不使用直接读取json文件的皮肤数据原因是，官方的json文件里面的英雄皮肤写的不全
    # skin_name = hero['skin_name']
    # if not skin_name:
    #     skin_name = hero['skin_title']
    # pf = skin_name.split('|')  # 文本分割
 
    url1 = hero_link + ename + '.shtml'  # 英雄主页网址
    url1 = ((urllib.request.urlopen(url1)).read()).decode('gbk')  # 获取源码，并且转码为gbk
    pf = re.compile('data-imgname="' + '(.*?)' + '">', re.S).findall(url1)  # 取出皮肤名字
    pf = pf[0]
    """删除沉余字符"""
    pf = pf.replace('&', '', )
    pf = pf.replace('0', '', )
    pf = pf.replace('1', '', )
    pf = pf.replace('2', '', )
    pf = pf.replace('3', '', )
    pf = pf.replace('4', '', )
    pf = pf.replace('5', '', )
    pf = pf.replace('6', '', )
    pf = pf.replace('7', '', )
    pf = pf.replace('8', '', )
    pf = pf.replace('9', '', )
 
    pf = pf.split('|')  # 文本分割
 
    print(pf)
  
    for i1 in range(0, len(pf)):
        print(hero_name + '-' + pf[i1])
        # 皮肤图片下载地址
        img_url = skin_link + ename + '/' + ename + '-bigskin-' + str(i1 + 1) + '.jpg'
        # 皮肤保存路径
        skin_dir = des_dir + '/' + hero_name
        if not os.path.exists(skin_dir):
            os.mkdir(skin_dir)
        urllib.request.urlretrieve(img_url, des_dir + '/' + hero_name + '/' + hero_name + '-' + pf[i1] + '.jpg')  # 下载
