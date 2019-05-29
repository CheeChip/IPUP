import turtle as t
import math

x1, y1, r1 = eval(input("Enter circle's center x-, y-coordinates, and radius: "))
x2, y2, r2 = eval(input("Enter circle's center x-, y-coordinates, and radius: "))

dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

text = None
if dist >= r1 + r2:
    text = "circle2 does not overlap circle1."
elif dist <= r1 - r2:
    text = "circle2 is inside circle1."
else:
    text = "circle2 overlaps circle1."

font = ("Times", 11)
t.screensize(1920, 1080)

t.penup()
t.goto(x1, y1-r1)
t.pendown()
t.circle(r1)

t.penup()
t.goto(x2, y2-r2)
t.pendown()
t.circle(r2)

t.penup()
t.goto(200, 200)
t.write(text, font=font)
t.hideturtle()
t.done()
