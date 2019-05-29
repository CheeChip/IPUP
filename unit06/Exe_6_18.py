# Exe 18

from random import randint


def printMatrix(n):
    for __ in range(n):
        for _ in range(n):
            print(randint(0, 1), end = ' ')
        print()

def main(args):
    try:
        n = args[1]
    except IndexError:
        n = int(input("Enter a number: "))

    printMatrix(n)

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
