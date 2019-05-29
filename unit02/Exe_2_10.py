#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （物理方面：计算跑道长度）假定给出飞机的加速度 a 和
#   起飞速度 v，可以根据以下公式计算出飞机起飞所需要的
#   最短跑道长度。
#       length =  \frac {v^{2}} {2*a}
#   编写一个程序，提升用户输入以 m/s 为单位的 v 和以 
#   m/s^2 为单位的 a，然后计算出跑道长度。
#++++++++++++++++++++++++++++++++++++++++++++++++

v, a = eval(input('Enter speed and acceleration: '))

length = v**2 / (2 * a)

print('The minimum runway length for this airplane is',
    round(length, 3), 'meters')