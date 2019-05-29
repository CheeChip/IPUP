#!/usr/bin/env python3

def main(args):
    cnt = 0
    for i in range(1, 7):
        for j in range(i+1, 8):
            print(i, j)
            cnt += 1
    print("The total number of all combinations is", cnt)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
