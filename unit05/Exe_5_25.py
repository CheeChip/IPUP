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
#  ��Ŀ������ʾ�������󣩵������һ���ǳ��������һ���ǳ�С����ʱ���ͻ�����������󡣴���
#  ���ܻ������С������Ϊ�˱����������󲢻�ȡ����ȷ�Ľ����Ӧ����ϸѡ������˳�����磺
#  �ڼ���Ĺ����в�ȡ���ҵ�����Ǵ����ҵ�˳���������Ի�ø���ȷ�Ľ����
#  ��д����Ƚϴ���������ҵ������Ľ����


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
