#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （计算年数和天数）编写一个程序，提升用户输入分钟数，
#   然后将分钟转换为年数和天数并显示在屏幕上。简单起见，
#   嘉定一年有 365 天。
#++++++++++++++++++++++++++++++++++++++++++++++++

MIN_IN_DAY = 60 * 24
MIN_IN_YEAR = MIN_IN_DAY * 365

minutes = int(input('Enter the number of minutes: '))
years = minutes // MIN_IN_YEAR
days = (minutes % MIN_IN_YEAR) // MIN_IN_DAY

print(minutes, 'is approximately', years, 'years and', days, 'days.')
