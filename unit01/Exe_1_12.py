#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目：
#   （Turtle：绘制正方形）编写程序在屏幕中心绘制正方形
#++++++++++++++++++++++++++++++++++++++++++++++++

import turtle as t

class Exe_1_12():
    def __init__(self):
        pass
    
    def drawsquare(self, a):
        for i in range(3):
            t.forward(a)
            t.right(90)
        t.forward(a)
    
    def execute(self, a = 100):
        for i in range(4):
            self.drawsquare(a)
        t.done()
    
if __name__ == "__main__":
    e = Exe_1_12()
    e.execute()