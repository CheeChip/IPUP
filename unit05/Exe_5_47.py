#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_47.py
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
from random import randint

def main(args):
    t.penup()
    t.goto(60, 50)
    t.pendown()
    for i in range(2):
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(120)
        
    t.penup()
    t.hideturtle()
    
    x = y = None
    for i in range(10):
        x = randint(-59, 59)
        y = randint(-49, 49)
        t.goto(x, y)
        t.dot()
    
    t.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
