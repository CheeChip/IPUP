#!/usr/bin/env python3

# Exe 01 五角数

def getPentagonalNumber(n):
    return n * (3 * n - 1) // 2

def main(args):
    for i in range(1, 101):
        print(format(getPentagonalNumber(i), "5d"), 
                end = ('\n' if i % 10 == 0 else ' '))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
