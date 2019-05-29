#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （Turtle：绘制四个圆）提示用户输入半径并在平米左右画四个圆
#++++++++++++++++++++++++++++++++++++++++++++++++

import turtle

radius = eval(input("Enter the radius: "))

turtle.penup()
turtle.goto(-radius, 0)
turtle.pendown()
turtle.circle(radius)
turtle.circle(-radius)

turtle.penup()
turtle.goto(radius, 0)
turtle.pendown()
turtle.circle(radius)
turtle.circle(-radius)

turtle.done()