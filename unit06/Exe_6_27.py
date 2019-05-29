# Exe 27

def isPrime(num):
    from math import sqrt
    
    if num <= 1:
        return False
    elif num == 2 or num == 3 or num == 5 \
         or num == 7 or num == 11 or num == 13 \
         or num == 17 or num == 19 or num == 23:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 \
         or num % 7 == 0 or num % 11 == 0 or num % 13 == 0 \
         or num % 17 == 0 or num % 19 == 0 or num % 23 == 0:
        return False
    
    for i in range(29, int(sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True


def main(args):
    n = 2
    while n + 2 < 1000:
        if isPrime(n) and isPrime(n+2):
            print('({}, {})'.format(n, n+2))
        n += 1

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
