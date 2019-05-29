#!/usr/bin/env python3
# 模拟抛硬币一百万次，然后显示正反面出现的次数。

from random import random

def toss():
    return random() >= 0.5

def main(args):
    heads = 0
    tails = 0
    for i in range(1000000):
        if toss():
            heads += 1
        else:
            tails += 1

    print("Heads:", heads)
    print("Tails:", tails)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
