import turtle as t
t.screensize(1920, 1080)
t.speed(10)
t.penup()
t.goto(0, -200)
t.pendown()
t.circle(200)
t.penup()
t.goto(0, 30)
t.pendown()
t.circle(-70, steps=3)

t.penup()
t.goto(90, 75)
t.dot(60)
t.goto(-90, 75)
t.dot(60)
t.goto(-110, -75)
t.pendown()
t.goto(0, -130)
t.goto(110, -75)
t.done()