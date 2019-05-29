# Exe 26

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
    n = 1
    print('{:<2s}{:>15s}'.format('p', '2^p - 1'))
    
    while n < 31:
        num = 2 ** n - 1
        if isPrime(num):
            print('{:<2d}{:>12d}'.format(n, num))
        n += 1
        
    return 0
            

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
