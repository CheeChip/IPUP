#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （Turtle：绘制四个正六边形）编写一个程序，让用户输入边长，
#   在屏幕中画出四个正六边形
#++++++++++++++++++++++++++++++++++++++++++++++++

import turtle

side = eval(input("输入六边形边长："))

pos = side * 3 ** 0.5 / 2
turtle.penup()
turtle.goto(-pos, 0)
turtle.pendown()
turtle.left(30)
for i in range(6):
    turtle.forward(side)
    turtle.left(60)
turtle.right(60)
for i in range(6):
    turtle.forward(side)
    turtle.right(60)

turtle.penup()
turtle.goto(pos, 0)
turtle.pendown()
turtle.left(60)
for i in range(6):
    turtle.forward(side)
    turtle.left(60)
turtle.right(60)
for i in range(6):
    turtle.forward(side)
    turtle.right(60)

turtle.done()