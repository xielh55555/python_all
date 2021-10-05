import pandas as pd 
pdf=pd.read_excel(r'C:\Users\谢立虎\Desktop\新建文件夹\5.26多门店报量(1).xlsx',header=None)
m=int(pdf.shape[1])
list1=[]
list2=[]
x=0
for i in range(5,m):
    for p in pdf[i][1:]:
        x+=1
        if pd.isnull(p):
            pass
        else:
            list1.append(pdf[i][0])
            list1.append(pdf[1][x])
            list1.append(pdf[2][x])
            list1.append(pdf[3][x])
            list1.append(p)
            list2.append(list1)
            list1=[]
    x=0
pdf=pd.DataFrame(list2)
pdf
pdf.to_excel(r'C:\Users\谢立虎\Desktop\新建文件夹\lesson.xlsx')


