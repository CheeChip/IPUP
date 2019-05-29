#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目：
#   （级数求和）编写程序显示 $1+2+3+4+5+6+7+8+9$ 的和。
#++++++++++++++++++++++++++++++++++++++++++++++++

class Exe_1_06():
    
    def __init__(self):
        pass

    def execute(self, n=9):
        sum = 0
        for i in range(1, n+1):
            sum += i
        return sum

if __name__ == "__main__":
    e = Exe_1_06()
    print(e.execute())
