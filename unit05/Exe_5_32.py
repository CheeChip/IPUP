#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_32.py
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
#  Exe 32
#  题目：（财务应用程 序：复合值）假设你每月给账户中存储 100 元，且年利率为 5%。所以，
#  每个月的利率是 5% / 12 = 0.417%. 


def main(args):
    monthly_save = eval(input("Enter an amount: "))
    rate = eval(input("Enter interest rate of year: ")) / 100
    months = eval(input("Enter months: "))

    month_rate = rate / 12
    
    total = 0
    for i in range(months):
        total += monthly_save
        total = total * (1 + month_rate)
        print("After {}.th month, there's {:.3f} in your account".format(i+1, total))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
