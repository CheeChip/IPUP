#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_33.py
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
#  Exe 33
#  题目：（财务应用程序：计算 CD 价值）


def main(args):
    deposit = eval(input("Enter the initial deposit amount: "))
    yield_rate = eval(input("Enter annual percentage yield: ")) / 100
    months = eval(input("Enter maturity period (number of months): "))

    print("Month\tCD Value")
    for i in range(1, months + 1):
        deposit = deposit * (1 + yield_rate / 12)
        print("{}\t{:.2f}".format(i, deposit))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
