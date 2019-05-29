#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （Turtle：绘制一个矩形）编写一个程序，提升用户输入矩形的
#   中心、长和宽，然后画出这个矩形。
#++++++++++++++++++++++++++++++++++++++++++++++++

import turtle

x, y = eval(input('输入矩形的中心坐标（如， 10, 10）：'))
length, width = eval(input("输入矩形的长和宽（如， 30, 40）："))

turtle.penup()
turtle.goto(x+length/2, y+width/2)
turtle.pendown()

for i in range(2):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)

turtle.penup()
turtle.home()

turtle.done()