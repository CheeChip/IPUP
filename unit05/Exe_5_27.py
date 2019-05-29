#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_26.py
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
#  Exe 27
#  Ã‚ƒø£∫º∆À„ pi

def calc_pi(upperbound):
    total = 0.0
    for i in range(upperbound, 0, -1):
        total += (-1) ** (i+1) / (2 * i - 1)
    return 4 * total

def main(args):
    i = 10000
    while i <= 100000:
        print("{:>6d}\t{:.6f}".format(i, calc_pi(i)))
        i += 10000

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
