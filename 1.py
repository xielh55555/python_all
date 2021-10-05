import turtle
t=turtle.Pen()


t.penup()
t.forward(200)
t.pendown()

t.right(90)
for i in range(4):
    t.left(90)
    t.forward(-50)
    t.right(90)
    t.circle(50*(i+1)) 




turtle.done()

# print(range(4))