import turtle

pen = turtle.Pen()
turtle.title("五字棋")
turtle.setup(width=1000, height=800)


# 移动到左上角画棋盘的四个边
def init():
    pen.speed(10)
    turtle.tracer(False)  # 关闭绘画过程
    pen.hideturtle()  # 隐藏画笔
    turtle.bgcolor('#E8B565')
    pen.shape('circle')
    pen.penup()
    pen.setposition(-495, 395)
    pen.pendown()
    for x in range(3):
        pen.pensize(10)
        pen.forward(985)
        pen.right(90)
    pen.forward(990)

    # 移动到左上角开始画棋盘横线
    pen.penup()
    pen.setposition(-300, 300)
    pen.pendown()
    pen.pensize(1)
    pen.right(90)
    for x in range(11):
        pen.forward(600)
        pen.backward(600)
        pen.penup()
        pen.right(90)
        pen.forward(60)
        pen.left(90)
        pen.pendown()

    # 移动到左上角开始画棋盘竖线
    pen.penup()
    pen.setposition(-300, 300)
    pen.pendown()
    pen.pensize(1)
    pen.right(90)
    for x in range(11):
        pen.forward(600)
        pen.backward(600)
        pen.left(90)
        pen.penup()
        pen.forward(60)
        pen.pendown()
        pen.right(90)

    # 在棋盘中心画一个红色原点
    pen.penup()
    pen.setposition(0, 0)
    pen.pendown()
    pen.dot(20, "red")

    # 移动到棋盘上边写上”五子棋“
    pen.penup()
    pen.goto(-60, 325)
    pen.pendown()
    pen.write("五子棋", move=False, align="left", font=("微软雅黑'", 25, "normal"))
    pen.hideturtle()

    # 画两个棋盒
    pen.penup()
    pen.goto(400, 0)
    pen.pendown()
    pen.dot(100, "black")
    pen.penup()
    pen.goto(375, 80)
    pen.pendown()
    pen.write("黑子", move=False, align="left", font=("微软雅黑'", 25, "normal"))
    pen.hideturtle()

    pen.penup()
    pen.goto(-400, 0)
    pen.pendown()
    pen.dot(100, "white")
    pen.penup()
    pen.goto(-425, 80)
    pen.pendown()
    pen.write("白子", move=False, align="left", font=("微软雅黑'", 25, "normal"))
    pen.hideturtle()


# 初始化棋盘主程序
init()

whitez = []  # 落下白子时记录坐标
blackz = []  # 落下黑子时记录坐标
mov = []  # 把已落子的坐标放入这个列表中，记录这个坐标是否可以落子
color = "white"  # 记录落子的颜色
t = 0  # 判断是否两次点鼠标
v = 0  # 返回黑白子是否胜利

# 定义变量用于判断黑方或白方胜
n = []
p = []
e = []
nh = []
ph = []
eh = []


# 判断黑子胜利
def winblackz(z, s, g):
    # 一横向胜
    for i in range(len(g)):
        n.append(g[i])
        u = n[i][0]
        if z == u:
            p.append(g[i])
    n.clear()
    for i in range(len(p)):
        n.append(p[i])
        u = n[i][1]
        e.append(u)
    if s + 1 in e and s + 2 in e and s + 3 in e and s + 4 in e:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if s - 1 in e and s + 1 in e and s + 2 in e and s + 3 in e:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if s - 2 in e and s - 1 in e and s + 1 in e and s + 2 in e:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if s - 3 in e and s - 2 in e and s - 1 in e and s + 1 in e:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if s - 4 in e and s - 3 in e and s - 2 in e and s - 1 in e:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    # 一竖行胜
    for i in range(len(g)):
        nh.append(g[i])
        u = nh[i][1]
        if s == u:
            ph.append(g[i])
            print("X坐标是", u)
            print("坐标：", ph)
        else:
            print(g)

    nh.clear()
    for i in range(len(ph)):
        nh.append(ph[i])
        u = nh[i][0]
        # print(u)
        eh.append(u)
    # print(e)
    if z + 1 in eh and z + 2 in eh and z + 3 in eh and z + 4 in eh:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if z - 1 in eh and z + 1 in eh and z + 2 in eh and z + 3 in eh:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if z - 2 in eh and z - 1 in eh and z + 1 in eh and z + 2 in eh:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if z - 3 in eh and z - 2 in eh and z - 1 in eh and z + 1 in eh:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if z - 4 in eh and z - 3 in eh and z - 2 in eh and z - 1 in eh:
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    # 从左到右向上胜
    if (z + 1, s + 1) in set(g) and (z + 2, s + 2) in set(g) and (z + 3, s + 3) in set(g) and (
            z + 4, s + 4) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if (z + 1, s + 1) in set(g) and (z + 2, s + 2) in set(g) and (z + 3, s + 3) in set(g) and (
            z - 1, s - 1) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if (z + 1, s + 1) in set(g) and (z + 2, s + 2) in set(g) and (z - 2, s - 2) in set(g) and (
            z - 1, s - 1) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if (z + 1, s + 1) in set(g) and (z - 3, s - 3) in set(g) and (z - 2, s - 2) in set(g) and (
            z - 1, s - 1) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if (z - 4, s - 4) in set(g) and (z - 3, s - 3) in set(g) and (z - 2, s - 2) in set(g) and (
            z - 1, s - 1) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))

    # 从左到右向下胜
    if (z + 1, s - 1) in set(g) and (z + 2, s - 2) in set(g) and (z + 3, s - 3) in set(g) and (
            z + 4, s - 4) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if (z + 1, s - 1) in set(g) and (z + 2, s - 2) in set(g) and (z + 3, s - 3) in set(g) and (
            z - 1, s + 1) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if (z + 1, s - 1) in set(g) and (z + 2, s - 2) in set(g) and (z - 2, s + 2) in set(g) and (
            z - 1, s + 1) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if (z + 1, s - 1) in set(g) and (z - 3, s + 3) in set(g) and (z - 2, s + 2) in set(g) and (
            z - 1, s + 1) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))
    if (z - 4, s + 4) in set(g) and (z - 3, s + 3) in set(g) and (z - 2, s + 2) in set(g) and (
            z - 1, s + 1) in set(g):
        print("ok")
        pen.penup()
        pen.goto(-50, -350)
        pen.write("黑方胜", move=False, align="left",
                  font=("微软雅黑'", 25, "normal"))


# 判断白子胜利
def winwhitez(x, y, v=0):
    return v


# 落子过程

def zhuojian(x, y):
    # 定义全局变量
    global color
    global a1
    global t
    global v
    global z
    global s

    t = 1

    if x < -300 or x > 300:
        return
    if y < -300 or y > 300:
        return
    a1 = (round(x / 60) * 60, round(y / 60) * 60)
    if (a1 in mov):
        return
    if color == "black":
        return
    z = round(x / 60)
    s = round(y / 60)

    winblackz(z, s, g=blackz)

    color = "black"
    pen.pencolor("black")
    pen.fillcolor("black")
    pen.pensize(50)
    pen.penup()
    pen.goto(340, 0)
    pen.pendown()
    pen.showturtle()
    turtle.tracer(True)
    pen.speed(3)
    pen.penup()
    pen.goto(round(x / 60) * 60, round(y / 60) * 60)
    pen.pendown()
    pen.dot(30)
    pen.hideturtle()
    turtle.tracer(False)
    a1 = (round(x / 60), round(y / 60))
    mov.append(a1)
    blackz.append(a1)
    t = 0
    print(blackz)


def youjian(x, y):
    global color
    global t
    t = 1
    if x < -300 or x > 300:
        return
    if y < -300 or y > 300:
        return
    a1 = (round(x / 60) * 60, round(y / 60) * 60)
    if (a1 in mov):
        return
    if color == "white":
        return
    z = round(x / 60)
    s = round(y / 60)
    winblackz(z, s, g=whitez)
    color = "white"
    pen.pencolor("white")
    pen.fillcolor("white")
    pen.pensize(30)
    pen.penup()
    pen.goto(-350, 0)
    pen.pendown()
    pen.showturtle()
    turtle.tracer(True)
    pen.speed(3)
    pen.penup()
    pen.goto(round(x / 60) * 60, round(y / 60) * 60)
    pen.pendown()
    pen.dot(30)
    pen.hideturtle()
    turtle.tracer(False)
    a1 = (round(x / 60), round(y / 60))
    mov.append(a1)
    whitez.append(a1)
    t = 0
    print(whitez)


# 按“c” 清空棋盘
def keypass(key):
    if key == "c":
        pen.reset()
        init()
        mov.clear()
        pen.hideturtle()


# 按”b"悔棋
def huiqi(key):
    global color
    if key == "b":
        if color == "black":
            for i in range(3):
                pen.undo()
            color = "white"

        # if color == "white":
        else:
            for i in range(4):
                pen.undo()
            color = "black"

    mov.pop()


# 监听键盘和鼠标
def jiace():
    turtle.onscreenclick(zhuojian, btn=1, )  # 获取鼠标点击的坐标，（btn中1是左，3是右）
    turtle.onscreenclick(youjian, btn=3, )
    turtle.onkeypress(lambda: keypass("c"), "c")
    turtle.onkeypress(lambda: huiqi("b"), "b")
    turtle.listen()


def main():
    global t
    if t != 1:
        jiace()
    else:
        return


if __name__ == '__main__':
    main()

turtle.done()
