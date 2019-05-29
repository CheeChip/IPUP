# Exe 08 米与英尺之间互相转换

def footToMeter(foot):
    return 0.305 * foot


def meterToFoot(meter):
    return meter / 0.305


def displayFigure():
    foot = 1.0
    meter = 20.0
    
    print('{:^15s}{:^15s}|{:^15s}{:^15s}'.format(
        'Feet', 'Meters', 'Meters', 'Feet'))
    print('-'*30 + '+' + '-'*30)
    
    while foot <= 10 and meter <= 65:
        print('{:^15.1f}{:^15.3f}|{:^15.1f}{:^15.3f}'.format(
            foot, footToMeter(foot),
            meter, meterToFoot(meter)))
        foot += 1
        meter += 5


def main(args):
    displayFigure()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
