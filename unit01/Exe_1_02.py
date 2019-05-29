#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目：
#   （显示同样的消息五次）编写程序显示"Welcome to Python" 五次。
#++++++++++++++++++++++++++++++++++++++++++++++++

class Exe_1_02():

    def __init__(self):
        pass
    
    def execute(self, n=5):
        for i in range(n):
            print("Welcome to Python.")

if __name__=="__main__":
    e = Exe_1_02()
    e.execute()
