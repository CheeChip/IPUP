#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （人口预测）改下练习题 1.11 来提升用户键入年数，然后显示那么多年后
#   的人口数。
#   每 7 秒 1 人出生
#   每 13 秒 1 人死亡
#   每 45 秒 1 个新移民
#++++++++++++++++++++++++++++++++++++++++++++++++

years = int(input("Enter the number of years: "))

seconds = years * 365 * 24 * 60 * 60
base = 3120324986

born = seconds // 7
death = seconds //13
immigrant = seconds // 45

population = base + born - death + immigrant

print("The poulation in %d years is %d" % (years, population))