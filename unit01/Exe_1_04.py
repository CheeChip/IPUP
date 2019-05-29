#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目：
#   （打印表格）编写程序显示下面的表格
#       a       a^2     a^3
#       1       1       1
#       2       4       8
#       3       9       27
#       4       16      64
#++++++++++++++++++++++++++++++++++++++++++++++++

class Exe_1_04():
    def __init__(self):
        pass

    def execute(self, n=4):
        print('a\ta^2\ta^3')
        for i in range(n):
            print(str(i) + '\t' 
                + str(i**2) + '\t' 
                + str(i**3))

if __name__ == '__main__':
    e = Exe_1_04()
    e.execute()