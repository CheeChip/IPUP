#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#       （财务应用程序：计算消费）编写一个读取小计和酬金率
#   然后计算小费以及合计金额的程序。
#   例如：如果用户键入的小计是 10，酬金率是 15% ，程序就会显示
#   小费是 1.5 ，合计金额是 11.5 。
#++++++++++++++++++++++++++++++++++++++++++++++++

subtotal, rate = eval(input('Enter the subtotal and a gratuity rate: '))
tip = round(subtotal * rate/ 100, 2)
total = subtotal + tip
print('The gratuity is', tip, 'and the total is', total)