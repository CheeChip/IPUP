# Exe 12 显示字符

def printChars(ch1, ch2, numberPerLine):
    start = ord(ch1)
    end   = ord(ch2) + 1
    cnt = 1
    for asc in range(start, end):
        print(chr(asc), end = ('\n' if cnt % numberPerLine == 0 else ' '))
        cnt += 1
    return


def main(args):
    try:
        ch1 = args[1]
        ch2 = args[2]
        npl = args[3]
    except IndexError:
        ch1 = input("输入开始字符：")
        ch2 = input("输入截止字符：")
        npl = int(input("输入每行显示的字符数："))
        
    try:
        ch1 = eval(ch1)
    except NameError:
        pass
    try:
        ch2 = eval(ch2)
    except NameError:
        pass
        
    printChars(ch1, ch2, npl)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
