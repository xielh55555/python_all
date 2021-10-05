import turtle
t=turtle.Pen()
c=['red','blue','yellow','green']
for i in range(1000):
    turtle.tracer(False)
    for i in range(4):
        t.fillcolor(c[i%4])
        t.begin_fill()
        t.forward(200)
        t.left(90)
        t.circle(200,45)
        t.left(90)
        t.forward(200)
        t.left(180)
        t.end_fill()
    t.left(358)
    turtle.tracer(True)
turtle.done()




# turtle.tracer(False)  # 关闭绘画过程
#     pen.hideturtle()  # 隐藏画笔
# t.fillcolor('red')
# t.begin_fill()
# t.circle(200)
# t.end_fill()

# with open('C:\电脑\趣儿编备课\PYTHON\zhuixu.word',mode='r',encoding='utf-8') as f :
#     for i in f.readlines():
#         if i[0]=='\n':
#             pass
#         else:
#             with open('C:\电脑\趣儿编备课\PYTHON\zhuixu11.word',mode='a',encoding='utf-8') as f :
#                 f.write(i)
