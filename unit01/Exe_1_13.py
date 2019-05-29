#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目：
#   （Turtle：绘制十字）编写程序在屏幕中心绘制十字
#++++++++++++++++++++++++++++++++++++++++++++++++

import turtle as t

class Exe_1_13():
    def __init__(self):
        pass
    
    def execute(self, a = 100):
        t.penup()
        t.forward(a)
        t.pendown()
        t.right(180)
        t.forward(2 * a)
        t.penup()
        t.goto(0, a)
        t.pendown()
        t.left(90)
        t.forward(2 * a)
        t.done()
    
if __name__ == "__main__":
    e = Exe_1_13()
    e.execute()