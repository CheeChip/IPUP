#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （金融应用程序：计算未来投资额）使用下面的公式编写一个资源读取投资额、
#   年利率和年数，然后显示未来投资额的程序。
#       未来投资额 = 投资额 * (1+月投资率)^月数
#++++++++++++++++++++++++++++++++++++++++++++++++

investment = eval(input("Enter investment amount: "))
rate = eval(input("Enter annual interest rate: "))
years = int(input("Enter number of years: "))

accumulated_val = investment * (1 + rate / 1200) ** (years * 12)

print("Accumulated value is %f" % (accumulated_val))