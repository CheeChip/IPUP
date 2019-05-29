import turtle as t

def getval(x0, y0, x1, y1, x2, y2):
    val = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return val

x0, y0 = eval(input("Enter coordinates for point p0: "))
x1, y1 = eval(input("Enter coordinates for point p1: "))
x2, y2 = eval(input("Enter coordinates for point p2: "))

val = getval(x0, y0, x1, y1, x2, y2)
text = None
if val > 0:
    text = "p2 is on the left side of the line"
elif val < 0:
    text = "p2 is on the right side of the line"
else:
    text = "p2 is on the same line"

font = ("Times", 11)

t.screensize(1920, 1080)
t.penup()
t.goto(x0, y0)
t.pendown()
t.write('p0 ({}, {})'.format(x0, y0), font=font)
t.goto(x1, y1)
t.write('p1 ({}, {})'.format(x1, y1), font=font)
t.penup()
t.goto(x2, y2)
t.dot(5)
t.write('p2 ({}, {})'.format(x2, y2), font=font)
t.setheading(-90)
t.forward(20)
t.right(90)
t.forward(70)
t.write(text, font=font)
t.hideturtle()

t.done()