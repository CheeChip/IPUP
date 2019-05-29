#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#       （将英尺数转换为米数）编写一个程序，它读取英尺数
#   然后将它转换成米数并显示结果。
#       1 foot = 0.305 meter
#++++++++++++++++++++++++++++++++++++++++++++++++

feet = eval(input('Enter a value for feet: '))
meters = feet * 0.305
print(feet, 'feet is', meters, 'meters')