#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （科学：计算能量）编写一个程序，计算将水从初始温度加热到
#   最终温度所需的能量。程序应该体术用户输入以千克计算的水量
#   以及水的初始温度和最终温度。计算能量的公式是
#       Q = M * (T_{final} - T_{initial}) * 4184
#   这里的 M 是水的质量，单位是千克，温度是摄氏温度，热量 Q
#   的单位是焦耳。
#++++++++++++++++++++++++++++++++++++++++++++++++

m = eval(input('Enter the amount of water in kilograms: '))
t_init = eval(input('Enter the initial temperature: '))
t_fin = eval(input('Enter the final temperature: '))

q = m * (t_fin - t_init) * 4184

print('\nThe energy needed is', q)