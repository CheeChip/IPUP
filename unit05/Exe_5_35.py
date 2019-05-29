#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_35.py
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
#  Exe 35
#  （完全数）如果一个正整数等于除它自身之外的所有正因子之和，那么这个数被称为完全数。找出
#   10000 以内所有的完全数

def isCompleteNum(num):
    factorSum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            factorSum += i
            
    return factorSum == num


def main(args):
    for i in range(1,  10000):
        if isCompleteNum(i):
            print(i)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
