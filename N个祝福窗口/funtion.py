import re
def zhufuh():
    zhufu_list=[]
    with open('D:\\python\\PYTHON\\N个祝福窗口\\zhufu.txt','r',encoding='UTF-8') as fo:
        
        for i in fo.readlines():
            ret=re.findall('[\u4e00-\u9fa5]{4}',i)
            zhufu_list+=ret
    # print(zhufu_list)
    # m=len(zhufu_list)
    return zhufu_list
     

def colors():
    color_list=[]
    with open('D:\\python\\PYTHON\\N个祝福窗口\\color.txt','r',encoding='UTF-8') as fo:
        for i in fo.readlines():
            ret=re.findall('#\w{6}',i)
            color_list+=ret
    return color_list