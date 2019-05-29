import turtle as t

t.screensize(1920, 1080)

radius = eval(input("Enter the radius of the Five-Rings: "))
t.pensize(radius / 5)

t.penup()
t.goto(-2.4 *radius, 0)
t.pendown()
t.color("blue")
t.circle(radius)

t.penup()
t.goto(0, 0)
t.pendown()
t.color("black")
t.circle(radius)

t.penup()
t.goto(2.4 * radius, 0)
t.pendown()
t.color("red")
t.circle(radius)

t.penup()
t.goto(-1.2 * radius, -1 * radius)
t.pendown()
t.color("yellow")
t.circle(radius)

t.penup()
t.goto(1.2 * radius, -1 * radius)
t.pendown()
t.color("green")
t.circle(radius)

t.done()