#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （金融应用程序：投资额）假如你想将一笔钱以固定的年利率存入账户。
#   如果你希望三年账户账户中有 5000 美元，你现在需要存多少钱？使用
#   下面的公式可以计算出初始存款
#       最初存款额 = \frac {最终金额值} {(1 + 月利率)^{月数}}
#   
#   编写一个程序，要求用户输入最终金额、百分比的年利率（注意公式给的
#   是月利率）以及年数，然后显示最初的存款额。
#++++++++++++++++++++++++++++++++++++++++++++++++

val_final = eval(input("Enter final account value: "))
interest_rate = eval(input("Enter annual interest rate in percent: ")) / 12
years = eval(input("Enter number of years: "))

val_init = val_final / (1 + interest_rate / 100) **( (years) * 12)

print("\nInitial deposit value is", round(val_init, 2))