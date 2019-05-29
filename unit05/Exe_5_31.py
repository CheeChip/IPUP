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
#  Exe 31
#  ¥Ú”°»’¿˙


def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False


def printCalendar(year, month, weekday):
    MONTH = ["January", "February", "Match", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]
    DAYS_OF_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    if isLeap(year):
        DAYS_OF_MONTH[1] = 29
    calendar = [' ' * 3] * weekday
    for day in range(1, DAYS_OF_MONTH[month] + 1):
        calendar.append('{:3d}'.format(day))
        
    print("{:^34}".format(MONTH[month] + ' ' + str(year)))
    print("-"*34)
    print('  '.join(WEEKDAYS))
    
    for i in range(len(calendar)):
        print(calendar[i], end="")
        if (i + 1) % 7 == 0:
            print()
        else:
            print('  ', end='')
    weekday = (weekday + DAYS_OF_MONTH[month]) % 7
    return weekday
def main(args):
    
    year = int(input("Enter year: "))
    weekday = int(input("Enter weekday of Jan 1st (0 for Sun, 6 for Saturday): "))

    for i in range(0, 12):
        weekday = printCalendar(year, i, weekday)
        print("\n\n")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
