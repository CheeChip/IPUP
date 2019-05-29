#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_55.py
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
#  Exe 55

import turtle as t

def main(args):
    #t.hideturtle()
    t.speed(10)
    # t.color('grey')
    # x = -80
    # y = 80

    # for i in range(9):
        # t.penup()
        # t.goto(x, y)
        # t.pendown()
        # t.forward(160)
        # y -= 20
        
    # y += 20
    
    # t.setheading(90)
    # for i in range(9):
        # t.penup()
        # t.goto(x, y)
        # t.pendown()
        # t.forward(160)
        # x += 20
    t.penup()
    t.goto(80, 80)
    t.pendown()
    t.setheading(90)
    t.color('black')
    for ___ in range(4):
        for __ in range(4):
            t.begin_fill()
            for _ in range(4):
                t.left(90)
                t.forward(20)
            t.end_fill()
            t.left(90)
            t.forward(40)
            t.right(90)
        t.backward(20)
        for __ in range(4):
            t.begin_fill()
            for _ in range(4):
                t.right(90)
                t.forward(20)
            t.end_fill()
            t.right(90)
            t.forward(40)
            t.left(90)
        t.backward(20)
    t.left(90)
    t.forward(160)
        
    t.hideturtle()
    t.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
