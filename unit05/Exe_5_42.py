#!/usr/bin/env python3
# Exe 42
from random import random

def main(args):
    cntDomain = 0
    cntAll = 0

    for i in range(10000):
        x = 2 * random() - 1
        y = 2 * random() - 1
        if x <= 0 or \
           (x > 0 and y > 0 and x + y < 1):
            cntDomain += 1
        cntAll += 1
    probablity = cntDomain / cntAll
    print("落到奇数区域的概率是 {:.4f}".format(probablity))

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
