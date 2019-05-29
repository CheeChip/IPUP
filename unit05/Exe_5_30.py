#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_30.py
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
#  Exe 30
#  题目：显示每个月的第一天


def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False

def main(args):
    MONTH = ["January", "February", "Match", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]
    DAYS_OF_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]
    year = int(input("Enter year: "))
    weekday = int(input("Enter weekday of Jan 1st (0 for Sun, 6 for Saturday): "))

    if isLeap(year):
        DAYS_OF_MONTH[1] = 29

    for i in range(0, 12):
        print("{} 1, {} is {}".format(MONTH[i], year, WEEKDAYS[weekday]))
        weekday = (weekday + DAYS_OF_MONTH[i]) % 7

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
