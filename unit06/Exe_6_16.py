# Exe 16

def isLeapYear(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    return False

def getDays(year):
    if isLeapYear(year):
        days = 366
    else:
        days = 365

    return days


def main(args):
    year = 2010
    while year <= 2020:
        print(year, getDays(year))
        year += 1
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
