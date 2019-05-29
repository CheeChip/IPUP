#!/usr/bin/env python3
# Exe 41

def main(args):
    dic = {}
    while True:
        n = int(input("Enter a number (0: for end of input): "))
        if n == 0:
            break
        else:
            if n in dic.keys():
                dic[n] += 1
            else:
                dic[n] = 1
    maxium = 0
    for i in dic.keys():
        maxium = i if i > maxium else maxium

    print("The largest number is", maxium)
    print("The occurrence count of the largest number is", dic[maxium])
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
