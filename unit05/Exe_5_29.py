#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_29.py
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
#  Exe 29
#  显示 21 世纪所有的闰年，每行 10 个

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False


def main(args):
    cnt = 0
    for i in range(2001, 2101):
        if isLeap(i):
            print(i, end = ' ')
            cnt += 1
            if cnt % 10 == 0:
                print()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
