#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_49.py
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
#  

import turtle as t

def genChart():
    table = [[i * j for i in range(1, 10)]
        for j in range(1, 10)]
    chart = ['{:^32}'.format("Multiplication Table")]
    s = ' ' * 3
    for i in table[0]:
        s += '{:>3d}'.format(i)
    chart.append(s)
    
    chart.append('-'*32)

    for row in table:
        s= str(row[0]) + ' |'
        for i in row:
            s += '{:>3d}'.format(i)
        chart.append(s)

    return chart

def main(args):
    font = ('Courier', 15)
    t.hideturtle()
    t.penup()
    t.goto(-180, 150)
    t.setheading(270)
    chart = genChart()
    for row in chart:
        t.write(row, font=font)
        t.forward(25)
    t.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
