#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#       （将摄氏度转化为华氏温度）编写一个从控制台读取摄氏温度
#   并将它转化为华氏温度并予以显示的程序。转换公式为
#       fahrenheit = (9 / 5) * celsius + 32
#++++++++++++++++++++++++++++++++++++++++++++++++

celsius = eval(input('Enter a celsius temperature: '))
fahrenheit = (9 / 5) * celsius + 32
print(celsius, 'Celsius is', fahrenheit, 'Fahrenheit')