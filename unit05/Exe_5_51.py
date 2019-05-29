#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_51.py
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

def main(args):
    t.hideturtle()
    t.speed(10)
    
    x = -85
    y = 85

    for i in range(18):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(170)
        y -= 10
        
    y += 10
    t.setheading(90)
    for i in range(18):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(170)
        x += 10
    
    
    t.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
