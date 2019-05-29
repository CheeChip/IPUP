# Exe 25

def isPrime(num):
    from math import sqrt
    if num == 2 or num == 3 or num == 5 \
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


def reverse(num):
    rev = 0
    while num > 0:
        rev = 10 * rev + num % 10
        num //= 10
    return rev


def isPalindrome(num):        
    return num == reverse(num)


def main(args):
    cnt = 0
    num = 2
    
    while cnt < 100:
        if not isPalindrome(num) and isPrime(num) and isPrime(reverse(num)):
            cnt += 1
            print(format(num, '>4d'), end = '\n' if cnt % 10 == 0 else ' ')
        num += 1
        
    return 0
            

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
