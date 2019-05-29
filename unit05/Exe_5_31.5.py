#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_31.py
#  
#  Copyright 2019 chee <983184728@qq.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Exe 31.5
#  打印日历,升级版，同一行打印好几个月

def getYear():
    import time
    t = int(time.time())
    years = 1970 + t // 60 // 60 // 24 // 365
    return years

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False


def getCalendar(lst, year, month, weekday):
    MONTH = ["January", "February", "Match", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]
    DAYS_OF_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    if isLeap(year):
        DAYS_OF_MONTH[1] = 29
    cal = []
    cal.append("{:^33}".format(MONTH[month] + ' ' + str(year)))
    cal.append("-"*33)
    cal.append('  '.join(WEEKDAYS))
    
    calendar = [' ' * 3] * weekday
    for day in range(1, DAYS_OF_MONTH[month] + 1):
        calendar.append('{:3d}'.format(day))
        
    weekday = (weekday + DAYS_OF_MONTH[month]) % 7
    for i in range(7 - weekday):
        calendar.append(' '*3)
        
    for i in range(0, len(calendar), 7):
        s = ""
        for j in range(i, i+7):
            try:
                s += calendar[j]
                if (j + 1) % 7 != 0:
                    s += ' ' * 2
            except IndexError:
                break
        cal.append(s)
    lst.append(cal)
    return weekday

def zeler(year):
    year -= 1
    m = 1
    q = 1
    j = year // 100
    k = year % 100
    
    h = q + (26 * (m + 1)) // 10 + k + k // 4 + j // 4 + 5 * j
    h %= 7
    
    return (h - 1) % 7
   
def main(args):
    year = getYear() if len(args) == 1 else int(args[1])
    weekday = zeler(year)

    month_lst = []
    
    for i in range(0, 12):
        weekday = getCalendar(month_lst, year, i, weekday)

    maxLen = 0
    for i in month_lst:
        if maxLen < len(i):
            maxLen = len(i)
    for i in month_lst:
        while len(i) < maxLen:
            i.append(" "*33)
        i.append(" "*33)
    for r in range(4):
        for line in range(maxLen):
            row = '   '.join([month_lst[3 * r + i][line] for i in range(3)])
            print(row)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
