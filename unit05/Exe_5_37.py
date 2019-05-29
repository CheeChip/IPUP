#!/usr/bin/env python3
# 题目：（求和）

from math import sqrt

def main(args):
    total = 0

    for i in range(1, 625):
        total += 1 / (sqrt(i) + sqrt(i+1))

    print(total)
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
