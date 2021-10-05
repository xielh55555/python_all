import os 
list1=os.listdir('C:\\电脑\\趣儿编备课\\PYTHON\\PYTHON\\三寸天堂\\三寸天堂\\')
# print(list1)
for list_filename in list1:
    with open('C:\\电脑\\趣儿编备课\\PYTHON\\PYTHON\\三寸天堂\\三寸天堂\\'+list_filename,mode='r',encoding='utf=8') as f :
        for readlist in f.readlines():
            if readlist[0]=='\n':
                pass
            else:
                with open('C:\\电脑\\趣儿编备课\\PYTHON\\PYTHON\\三寸天堂\\三寸天堂1.0\\'+list_filename,mode='a',encoding='utf-8') as f :
                    f.write(readlist)

