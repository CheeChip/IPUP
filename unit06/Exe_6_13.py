# Exe 13

def getm(n):
    s = 0.0
    for i in range(1, n+1):
        s += i / (i+1)

    return s


def printFigure(n):
    print(format('i', '^8s') + '|' + format('m(i)', '^8s'))
    print('-' * 8 + '|' + '-' * 8)
    for i in range(1, n+1):
        print(format(i, '^8d') + '|' + format(getm(i), '^8.4f'))


def main(args):
    try:
        num = int(args[1])
    except IndexError:
        num = int(input("输入行数："))

    printFigure(num)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
