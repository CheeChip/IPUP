import turtle as t

x, y = eval(input("Enter a point with two coordinates: "))

text = None

if abs(x-0) <= 100/2 and abs(y-0) <= 50/2:
    text = 'Point ({}, {}) is in the rectangle'.format(x, y)
else:
    text = 'Point ({}, {}) is not in the rectangle'.format(x, y)

font = ("Times", 11)

t.screensize(1920, 1080)
t.penup()
t.goto(100/2, 50/2)
t.pendown()
for i in range(2):
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
t.penup()
t.goto(x, y)
t.dot(6)
t.goto(-90, -50)
t.write(text, font=font)
t.hideturtle()
t.done()
