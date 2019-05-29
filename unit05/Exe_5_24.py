#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_24.py
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
#  Exe 24
#  题目：（财务应用程序：贷款摊销时间表）一笔给定的贷款每个月支付额包括本金和利息。月利息
#  可以通过计算月利率乘以结余（余下的本金）得到。每个月支付的本金就是每月支付额加上每月的
#  利息。编写程序让用户输入贷款额、年数以及利率，然后显示贷款额摊销时间表。

def payment(loan, years, rate):
    rate = rate / 100
    month_rate = rate / 12
    month_payment = loan * month_rate \
        / (1 - (1 + month_rate) ** (years * -12))
    return (month_payment, month_payment * years * 12)

def main(args):
    loan = int(input("Enter Loan Amount: "))
    years = int(input("Enter Number of Years: "))
    rate = eval(input("Enter Interest Rate: "))
    
    monthly_payment, total = payment(loan, years, rate)
    print("Monthly Payment: {}\nTotal Payment: {}".format(
        monthly_payment, total))
    monthly_interest_rate = rate / 12
    balance = loan
    print("Payment#\tInterest\tPrinciple\tBalance")
    for i in range(1, years * 12 + 1):
        interest = monthly_interest_rate / 100 * balance
        principle = monthly_payment - interest
        balance -= principle
        print("{:2d}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(
            i, interest, principle, balance))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
