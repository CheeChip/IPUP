# Exe 21

def sqrt(n):
    guess = 1

    for _ in range(100):
        guess = (guess + n / guess) / 2

    return guess


def main(args):
    try:
        n = args[1]
    except IndexError:
        n = eval(input("Enter an non-negetive number: "))

    print("square root of {} is {:.4f}".format(n, sqrt(n)))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
