#!/usr/bin/env python3
# Exe 38 倒计时

from time import sleep

def main(args):
    t = eval(input("Enter the number of seconds: "))

    while t > 0:
        print(t, "seconds remaining")
        sleep(1)
        t -= 1

    print("Stopped")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
