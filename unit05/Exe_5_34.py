#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exe_5_34.py
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
#  Exe 34
#  题目：（游戏：彩票）产生一个两位数随机数彩票，要求两位数不能相同

from random import randrange

def main(args):
    digit1 = randrange(10)
    digit2 = randrange(10)

    # 排除掉两位相同或高位为 0 的情况
    while digit1 == digit2 or digit2 == 0:
        digit2 = randrange(10)
    lottery = 10 * digit2 + digit1
    print("Lottery is {}".format(lottery))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
