import turtle as t

x1, y1 = eval(input("Enter r1's center x-, y-coordinates: "))
w1, h1 = eval(input("and r1's width and height: "))
x2, y2 = eval(input("Enter r2's center x-, y-coordinates: "))
w2, h2 = eval(input("and r2's width and height: "))

text = None
if abs(x1 - x2) >= (w1 + w2) / 2 \
    or abs(y1 - y2) >= (h1 + h2) / 2:
    text = "r2 does not overlap r1."
elif abs(x1 - x2) <= (w1 - w2) / 2 \
    and abs(y1 - y2) <= (h1 - h2) / 2:
    text = "r2 is in r1."
else:
    text = "r2 overlaps r1."

font = ("Times", 11)
t.screensize(1920, 1080)

t.penup()
t.goto(x1 + w1/2, y1 + h1/2)
t.pendown()
for i in range(4):
    t.right(90)
    t.forward(h1 if i % 2 == 0 else w1)

t.penup()
t.goto(x2 + w2/2, y2+h2/2)
t.pendown()
for i in range(4):
    t.right(90)
    t.forward(h2 if i % 2 == 0 else w2)

t.penup()
t.goto(200, 200)

t.write(text, font=font)

t.hideturtle()
t.done()
