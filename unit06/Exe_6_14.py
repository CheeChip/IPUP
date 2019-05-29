# Exe 14

def getpi(i):
    m = 0.0
    for n in range(1, i+1):
        m += (-1 if n % 2 == 0 else 1) /  (2 * n - 1)
    m *= 4

    return m


def printFigure(n):
    print(format('i', '^8s') + '|' + format('m(i)', '^8s'))
    print('-' * 8 + '|' + '-' * 8)
    i = 1
    while i <= n:
        print(format(i, '^8d') + '|' + format(getpi(i), '^8.4f'))
        i += 100

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
