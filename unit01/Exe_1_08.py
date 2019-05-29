#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目：
#   （圆的面积和周长）使用下面的公式编写程序，显示半径是 5.5 的圆的面积和周长
#       $$
#       area = radius \times radius \times \pi \\
#       perimeter = 2 \times radius \times \pi
#       $$
#++++++++++++++++++++++++++++++++++++++++++++++++

class Exe_1_08():
    PI = 3.14

    def __init__(self):
        pass
    
    def get_area(self, r):
        area = r * r * self.PI
        return area

    def get_perimeter(self, r):
        perimeter = 2 * r * self.PI
        return perimeter

    def execute(self, r=5.5):
        print('area is', self.get_area(r))
        print('perimeter is', self.get_perimeter(r))

if __name__ == "__main__":
    e = Exe_1_08()
    e.execute()