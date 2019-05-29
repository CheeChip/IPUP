#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （健康应用程序：计算 BMI）身体质量指数（BMI）是以体重
#   衡量健康的一种指数。以千克为单位的体重除以以米为单位的
#   身高的平方就可以计算它的值。
#   编写一个程序，提升用户输入以磅值单位的体重和以英尺为
#   单位的身高，然后显示 BMI 的值。
#   1 pound = 0.453 592 37 kilogram
#   1 inch = 0.0254 meter
#++++++++++++++++++++++++++++++++++++++++++++++++

w = eval(input("Enter weight in pounds: "))
h = eval(input("Enter height in inches: "))
w = w * 0.45359237
h = h * 0.0254
bmi = w / h ** 2
bmi = round(bmi, 4)

print("BMI is %f" % (bmi))