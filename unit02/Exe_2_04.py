#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#       （将磅转换为千克）编写一个程序将磅转换为千克。
#       1 pound = 0.454 kilogram
#++++++++++++++++++++++++++++++++++++++++++++++++

pounds = eval(input('Enter a value in pounds: '))
kilograms = 0.454 * pounds
print(pounds, 'pounds is', kilograms, 'kilograms')