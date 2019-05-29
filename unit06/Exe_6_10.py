# Exe 10 寻找素数

import math

def isPrime(n):
    import logging
    logging.basicConfig(level=logging.WARNING)
    divisor = 2
    while divisor <= int(math.sqrt(n)):
        logging.debug('divisor is {}'.format(divisor))
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def main(args):
    try:
        n = args[1]
    except IndexError:
        n = int(input("输入一个整数："))
    fmt = '{}d'.format(int(math.log(n, 10) + 1))
    
    cnt = 0
    for i in range(2, n + 1):
        if isPrime(i):
            cnt += 1
            print(format(i, fmt),
                  end = ('\n' if cnt % 10 == 0 else ' '))

    print("\n小于 {} 的素数有 {} 个".format(n, cnt))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
