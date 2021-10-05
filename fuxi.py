import turtle                      #! 导入画图
import time                       #! 导入时间
t=turtle.Pen()                     #! 拿出笔
t.pencolor('DeepSkyBlue')           #!笔的色
turtle.bgcolor('#08203D')           #!背景色

def hua():                          #!给这个画图的过程取一个名字：hua()
    for i in range(3600):
        t.forward(i*3)
        t.right(121)
    
def Home(d):                        #!把回到原点的过程取一个名字：Home()
    t.penup()
    t.home()
    t.right(d)
    t.pendown()

n=0
while 1:                      #! 一直重复执行，不停下来
    turtle.tracer(0)          #!直接生成图像，不出现画图过程
    t.clear()                   #! 屏幕清干净

    Home(20*n)
    hua()
    
    n+=1
    turtle.update()      
    time.sleep(0.01)   





turtle.done()      #!放好画布





