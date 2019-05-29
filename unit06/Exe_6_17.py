# Exe 17

def isValid(side1, side2, side3):
    try:
        assert side1 > 0 and side2 > 0 and side3 > 0
        if side1 + side2 > side3 and abs(side1 - side2) < side3:
            return True
        else:
            return False
    except AssertionError:
        return False


def area(side1, side2, side3):
    from math import sqrt
    s = (side1 + side2 + side3) / 2
    area = sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


if __name__ == '__main__':
    s1, s2, s3 = eval(input("Enter there sides: "))
    
    if isValid(s1, s2, s3):
        print("The area of the trangle is", format(area(s1, s2, s3), '.4f'))
    else:
        print("Input is invalid")
