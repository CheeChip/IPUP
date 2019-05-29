# Exe 22
from time import time

def getCurrentTime():
    current = {**getDate(), **getTime()}
    return current


def getTime():
    t = {}
    seconds = int(time())
    t['second'] = seconds % 60
    t['minute'] = seconds % 3600 // 60
    t['hour'] = seconds % (24 * 3600) // 3600
    return t


def getDate():
    date = {'year': 1970, 'month': 1, 'day': 1}
    getDay(date)
    getYear(date)
    getMonth(date)
    return date


def getDay(date):
    date['day'] += int(time()) // (24 * 3600)


def getYear(date):
    while date['day'] > 366:
        if isLeapYear(date['year']):
            date['day'] -= 366
        else:
            date['day'] -= 365
        date['year'] += 1
        
    if date['day'] == 366 and not isLeapYear(date['year']):
        date['day'] -= 365
        date['year'] += 1


def getMonth(date):
    monthDays = {1: 31,
                 2: 29 if isLeapYear(date['year']) else 28,
                 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                 9: 30, 10: 31, 11: 30, 12: 31,
        }

    for month in range(1, 13):
        if date['day'] > monthDays[month]:
            date['day'] -= monthDays[month]
        else:
            date['month'] = month
            break


def isLeapYear(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def main(args):
    now = getCurrentTime()
    print('{:0>2d}/{:0>2d}/{:4d} {:0>2d}:{:0>2d}:{:0>2d} GMT'.format(
        now['month'], now['day'],    now['year'],
        now['hour'],  now['minute'], now['second']))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
