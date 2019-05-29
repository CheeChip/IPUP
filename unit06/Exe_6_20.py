# Exe 20

from math import sqrt


def distance(x1, y1, x2, y2):
    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist


def main(args):
    try:
        x1, y1 = args[1], args[2]
        x2, y2 = args[3], args[4]
    except IndexError:
        x1, y1 = eval(input("Enter coordinate of P1: "))
        x2, y2 = eval(input("Enter coordinate of P2: "))

    print("Distance between P1 and P2 is",
          format(distance(x1, y1, x2, y2), '.3f'))
        
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
