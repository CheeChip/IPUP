#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_25.py
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
#  Exe 25
#  题目：（演示消除错误）当你操作一个非常大的数和一个非常小的数时，就会出现消除错误。大数
#  可能会抵消较小的数。为了避免消除错误并获取更精确的结果，应该仔细选择计算的顺序。例如：
#  在计算的过程中采取从右到左而非从左到右的顺序，这样可以获得更精确的结果。
#  编写程序比较从左到右与从右到左计算的结果。


def main(args):
    total = 0.0
    for n in range(1, 50001):
        total = total + 1 / n
    print("Left to right: {:.20f}".format(total))
    
    total = 0.0
    for n in range(50000, 0, -1):
        total = total + 1 / n
    print("Right to left: {:.20f}".format(total))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
