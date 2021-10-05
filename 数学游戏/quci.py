import re

def quci():
    list_1 = []
    mmm = []
    with open('shici.txt', 'r', encoding='UTF-8') as f:
        for i in f.readlines():
            ret = re.findall('.*[\u4e00-\u9fa5]+.*\s', i)
            list_1 += ret
    for list_11 in list_1:
        for i in list_11:
            if i != ' ':
                mmm += i
    return mmm

def colors():
    color_list = []
    with open('color.word', 'r', encoding='UTF-8') as fo:
        for i in fo.readlines():
            ret = re.findall('#\w{6}', i)
            color_list += ret
    return color_list