# Exe 19

def getValue(x0, y0, x1, y1, x2, y2):
    value = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return value


def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    return getValue(x0, y0, x1, y1, x2, y2) > 0


def rightOfTheLine(x0, y0, x1, y1, x2, y2):
    return getValue(x0, y0, x1, y1, x2, y2) == 0


def onTheLineSegment(x0, y0, x1, y1, x2, y2):
    return getValue(x0, y0, x1, y1, x2, y2) < 0


def main(args):
    try:
        x0, y0 = args[1], args[2]
        x1, y1 = args[3], args[4]
        x2, y2 = args[5], args[6]
    except IndexError:
        x0, y0 = eval(input("Enter coordinates of point 0: "))
        x1, y1 = eval(input("Enter coordinates of point 1: "))
        x2, y2 = eval(input("Enter coordinates of point 2: "))

    if leftOfTheLine(x0, y0, x1, y1, x2, y2):
        print("P2 is on the left side of the line from P0 to P1")
    elif rightOfTheLine(x0, y0, x1, y1, x2, y2):
        print("P2 is on the right side of the line from P0 to P1")
    elif onTheLineSegment(x0, y0, x1, y1, x2, y2):
        print("P2 is on the same line from P0 to P1")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
