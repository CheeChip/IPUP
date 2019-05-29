#!/usr/bin/env python3

# 读取 score.txt ，求成绩的平均值与标准方差
def mean(*args):
    total = 0
    for s in args:
        total += int(s)
    
    return total / len(args)


def deviation(*args):
    from math import sqrt

    total_sq = 0
    total = 0

    for s in args:
        total += int(s)
        total_sq += int(s) ** 2
    total = total ** 2

    return sqrt(abs(total_sq - total) / (len(args) - 1))

def main():
    f = open('score.txt', 'r')
    scores = f.readlines()
    f.close()
    # print(scores)
    # print(type(scores))

    m = mean(*scores)
    dev = deviation(*scores)

    print("The mean is", m)
    print("The standard deviation is", dev)


if __name__ == '__main__':
    main()
