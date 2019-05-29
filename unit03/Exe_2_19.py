import turtle as t
import math
t.screensize(1920, 1080)
t.speed(10)
t.pensize(3)
f = ('Times', 10, 'normal')

p1 = tuple(eval(input("输入第 1 个点的坐标：")))
p2 = tuple(eval(input("输入第 2 个点的坐标：")))

t.penup()
t.goto(*p1)
t.pendown()
t.goto(*p2)
t.penup()
t.goto(*p1)
t.write("p1 " + str(p1), font=f)
t.goto(*p2)
t.write("p2 " + str(p2), font=f)
t.hideturtle()

t.done()