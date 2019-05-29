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


p1 = tuple(eval(input("输入第 1 个点的坐标：")))
p2 = tuple(eval(input("输入第 2 个点的坐标：")))
p3 = tuple(eval(input("输入第 3 个点的坐标：")))

c = get_dist(*p1, *p2)
a = get_dist(*p2, *p3)
b = get_dist(*p3, *p1)

A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
C = math.acos((c * c - b * b - a * a) / (-2 * a * b))
A = math.degrees(A)
B = math.degrees(B)
C = math.degrees(C)
f = ('Times', 10, 'normal')
t.penup()
t.goto(*p1)
t.pendown()
t.goto(*p2)
t.goto(*p3)
t.goto(*p1)
t.hideturtle()
t.penup()
t.write("A " + format(A, ".2f") + '\u00b0', font=f)
t.goto(*p2)
t.write("B " + format(B, ".2f") + '\u00b0', font=f)
t.goto(*p3)
t.write("C " + format(C, ".2f") + '\u00b0', font=f)

t.done()