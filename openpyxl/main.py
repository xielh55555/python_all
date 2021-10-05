# from openpyxl import Workbook
# from openpyxl import load_workbook
import openpyxl
# import time
# wb=Workbook()
# wb1=wb.create_sheet('统计表',0)
# now=time.strftime('%x')

# wb1['a1']='你好！'
# wb1['b1']='计算'
# wb1['c1']='统计'
# wb1['d1']=now
# wb1.cell(row=1,column=5).value=45
# rows = (
#     (88, 46, 57),
#     (89, 38, 12),
#     (23, 59, 78),
#     (56, 21, 98),
#     (24, 18, 43),
#     (34, 15, 67)
# )
# for row in rows:
#     wb1.append(row)
# wb.save('Z.xlsx')
# row=()
# rows=()
# wb=openpyxl.load_workbook('Z.xlsx')
# 统计表=wb.active
# a1=wb1['a1']
# b1=wb1['b1']
# c1=wb1.cell(row=1,column=3)
# print(a1.value,b1.value,c1.value)
# cells=统计表['a1':'c7']
# for c1, c2 ,c3 in cells:
#     print("{0:3} {1:6} {2:8}".format(c1.value, c2.value,c3.value))

# for col in 统计表.iter_cols(min_row=1,min_col=1,max_row=7,max_col=3):
#     for cell in col:
#         row=row+(cell.value,)
        # print(cell.value,end=' ')
    # print()
#     rows+=(row,)
#     row=()
# print(rows)
# wb2=wb.create_sheet('新表',1)
# 新表=wb.active
# for row in rows:
#     wb2.append(row)
# # wb.save('Z.xlsx')
# wb=openpyxl.load_workbook('Z.xlsx')
# 统计表=wb.active
# a1=统计表['a1']
# 新表=wb.active
# b1=新表['a3']
# print(a1.value,b1.value)
# wb=openpyxl.load_workbook('Z.xlsx')
# 统计表=wb.active
# rows=统计表.rows
# list1=[]
# for row in rows:
#     for cell in row:
#         list1.append(cell.value)
# print(list1)
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

data = [
    ['Item', 'Colour'],
    ['pen', 'brown'],
    ['book', 'black'],
    ['plate', 'white'],
    ['chair', 'brown'],
    ['coin', 'gold'],
    ['bed', 'brown'],
    ['notebook', 'white'],
]

for r in data:
    sheet.append(r)

sheet.auto_filter.ref = 'A1:B8'
sheet.auto_filter.add_filter_column(1, ['brown', 'white'])
sheet.auto_filter.add_sort_condition('B2:B8')

wb.save('filtered.xlsx')