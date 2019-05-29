#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （几何方面：三角形的面积）编写一个程序，提示用户
#   输入三角形的三个顶点 (x1, y1), (x2, y2), (x3, y3)
#   然后显示它的面积。计算三角形面积的海伦公式为
#       s = (side1 + side2 + side3) / 2
#       area = sqrt{s * (s-side1) * (s-side2) * (s-side3)}
#++++++++++++++++++++++++++++++++++++++++++++++++

import turtle as t

x1, y1 = eval(input("Enter the coordinate of point 1: "))
x2, y2 = eval(input("Enter the coordinate of point 2: "))
x3, y3 = eval(input("Enter the coordinate of point 3: "))

t.setup(width = 0.5, height=0.75)
t.penup()
t.goto(x1, y1)
t.pendown()
t.write('(%s, %s)'% (x1, y1))

t.goto(x2, y2)
t.write('(%s, %s)'% (x2, y2))

t.goto(x3, y3)
t.write('(%s, %s)'% (x3, y3))

t.goto(x1, y1)

side1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
side2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
area = round(area, 4)
print("The area of the triangle is", area)

t.penup()
t.home()
t.write('area is %s' % area)
t.done()