import turtle as t

t.screensize(1920, 1080)
side = eval(input("Enter teh side of star: "))
for i in range(5):
    t.forward(side)
    t.right(144)
t.done()