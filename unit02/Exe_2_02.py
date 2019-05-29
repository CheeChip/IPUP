#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#       （计算圆柱体的体积）编写一个读取圆柱的半径和高度
#   并利用下面的公式计算圆柱体的底面积和体积的程序：
#       area = radius * radius * pi
#       volume = area * height
#++++++++++++++++++++++++++++++++++++++++++++++++

PI = 3.1415

radius = eval(input('Enter the Radius: '))
height = eval(input('Enter the Height: '))

area = radius * radius * PI
volume = area * height

print('The area is', area)
print('The volume is', volume)