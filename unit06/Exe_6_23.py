# Exe 23

def convertMillis(millis):
    time = {}
    time['second'] = millis % (60 * 1000) // 1000
    time['minute'] = millis % (3600 * 1000) // (60 * 1000)
    time['hour'] = millis // (3600 * 1000)
    
    return time


def main(args):
    try:
        millis = args[1]
    except IndexError:
        millis = eval(input("Enter millis: "))

    t = convertMillis(millis)
    print('{:d}:{:2d}:{:2d}'.format(t['hour'], t['minute'], t['second']))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
