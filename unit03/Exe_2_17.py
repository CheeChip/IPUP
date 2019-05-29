import turtle as t
import math
t.screensize(1920, 1080)
t.speed(10)

def get_dist(x1, y1, x2, y2):
    tmp = (x1 - x2) ** 2 + (y1 - y2) ** 2
    dist = math.sqrt(tmp)
    return dist

def get_area(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    tmp = s * (s - s1) * (s - s2) * (s - s3)
    area = math.sqrt(tmp)
    return area

def lowest_point(*p):
    lp = p[0]
    for point in p:
        if point[1] < lp[1]:
            lp = point
    return lp

p1 = tuple(eval(input("输入第 1 个点的坐标：")))
p2 = tuple(eval(input("输入第 2 个点的坐标：")))
p3 = tuple(eval(input("输入第 3 个点的坐标：")))

s1 = get_dist(*p1, *p2)
s2 = get_dist(*p2, *p3)
s3 = get_dist(*p3, *p1)

area = get_area(s1, s2, s3)
l_point = lowest_point(p1, p2, p3)

t.penup()
t.goto(*p1)
t.pendown()
t.goto(*p2)
t.goto(*p3)
t.goto(*p1)
t.hideturtle()
t.penup()
t.write("p1 " + str(p1), font=('Times', 10, 'normal'))
t.goto(*p2)
t.write("p2 " + str(p2), p2, font=('Times', 10, 'normal'))
t.goto(*p3)
t.write("p3 " + str(p3), p3, font=('Times', 10, 'normal'))
t.goto(*l_point)
t.setheading(-90)
t.forward(20)
t.write("The area of the triangle is " + format(area, ".2f"),
    font=('Times', 10, 'bold'))

t.done()