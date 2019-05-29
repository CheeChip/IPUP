#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_27.py
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
#  Exe 28
#  题目：（计算e）收敛非常非常非常快

def calc_e(upperbound):
    item = 1
    e = 1
    for i in range(1, upperbound+1):
        item = item / i
        e = e + item
    return e


def main(args):
    i = 10000
    while i <= 100000:
        print("{:>6d}\t{:.15f}".format(i, calc_e(i)))
        i += 10000
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
