#!/usr/bin/env python3

# Exe 02 求整数各位的和

def sumDigits(n):
    s = 0

    while n > 0:
        s += n % 10
        n //= 10

    return s


def main(args):
    try:
        n = int(args[1])
    except IndexError:
        n = int(input("输入一个整数："))

    print(n, "各位数加和为", sumDigits(n))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
