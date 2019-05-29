#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_54.py
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
import math

def main(args):
    
    t.penup()
    t.goto(-125, 0)
    t.pendown()
    t.forward(250)
    t.left(150)
    t.forward(20)
    t.goto(125, 0)
    t.left(60)
    t.forward(20)

    t.penup()

    t.goto(0, -75)
    t.pendown()

    t.setheading(90)
    t.forward(150)
    t.right(150)
    t.forward(20)
    t.goto(0, 75)
    t.right(60)
    t.forward(20)
    
    t.penup()
    t.hideturtle()
    t.goto(-100, 100)
    t.pendown()
    for x in range(-100, 100):
        t.goto(x, x ** 2 / 100)

    t.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
