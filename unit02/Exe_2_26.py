#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （Turtle：绘制一个圆）编写一个程序，提示用户输入圆心和半径，
#   在屏幕上显示圆并在圆心出显示它的面积
#++++++++++++++++++++++++++++++++++++++++++++++++

import turtle
PI = 3.1415926

x, y = eval(input('输入圆心坐标（如， 10, 10）：'))
radius = eval(input("输入圆的半径："))
area = PI * radius * radius

turtle.penup()
turtle.goto(x, y)
turtle.write(area)

turtle.goto(x, y-radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()