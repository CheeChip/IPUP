#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Exe_5_23.py
#  
#  Copyright 2019 chee <chee@DESKTOP-IQF5EAT>
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
#  Exe 23
#  ��Ŀ����д�������û����������Լ�����Ϊ��λ�Ĵ������ڣ�Ȼ����ʾ���ʴ� 5% ��ʼ��ÿ��
#  ���� 1/8��ֱ�� 8% ��ÿ�»�������ܵĻ���

def payment(loan, years, rate):
    rate = rate / 100
    month_rate = rate / 12
    month_payment = loan * month_rate \
        / (1 - (1 + month_rate) ** (years * -12))
    return (month_payment, month_payment * years * 12)

def main(args):
    loan = int(input("Enter Loan Amount: "))
    years = int(input("Enter Number of Years: "))
    print('{:<20s}{:<20s}{:<20s}'.format(
        'Interest Rate', 'Monthly Payment', 'Total Payment'))
    rate = 5
    while rate <= 8:
        print('{:<20.3%}{:<20.2f}{:<20.2f}'.format(
            rate / 100, *payment(loan, years, rate)))
        rate += 1/8

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
