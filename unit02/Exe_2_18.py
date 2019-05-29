#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （当前时间）修改清单 2-7 的程序使之提示用户输入时区，
#   这个时区是用距离 GMT 的小时数表示，然后显示指定时区的
#   时间。
#++++++++++++++++++++++++++++++++++++++++++++++++

import time

tz = int(input("Enter the timezone offset to GMT: "))

curtime = int(time.time())

seconds = curtime % 60
curtime //= 60
minutes = curtime % 60
curtime //= 60
hours = (curtime % 24 + tz) % 24

print('The current time is %2d:%2d:%2d' % (hours, minutes, seconds))