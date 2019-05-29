# Exe 08 摄氏度与华氏度互相转换

def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32


def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


def displayFigure():
    celsius = 40.0
    fahrenheit = 120.0
    
    print('{:^15s}{:^15s}|{:^15s}{:^15s}'.format(
        'Celsius', 'Fahrenheit', 'Fahrenheit', 'Celsius'))
    print('-'*30 + '+' + '-'*30)
    while celsius >= 31 and fahrenheit >= 30:
        print('{:^15.1f}{:^15.1f}|{:^15.1f}{:^15.1f}'.format(
            celsius, celsiusToFahrenheit(celsius),
            fahrenheit, fahrenheitToCelsius(fahrenheit)))
        celsius -= 1
        fahrenheit -= 10


def main(args):
    displayFigure()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
