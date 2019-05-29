#!/usr/bin/env python3

# Exe 07 计算未来投资值
import logging

# logging.basicConfig(level=logging.DEBUG)

def displayList(investmentAmount,
                monthlyInterestRate, years):
    logging.debug('interest rate is {}'.format(monthlyInterestRate))
    logging.debug('investmentAmount rate is {}'.format(investmentAmount))
    print('Years' + ' ' * 4 + 'Future Value')
    for i in range(years):
        investment = futureInvestmentValue(investmentAmount,
                                           monthlyInterestRate, i+1)
        print(format(i+1, '<5d') + ' '*4
              + format(investment, '10.2f'))


def futureInvestmentValue(investmentAmount,
                          monthlyInterestRate, years):
    investment = investmentAmount
    logging.debug('investment rate is {}'.format(investment))
    for _ in range(years * 12):
        investment = investment * (1 + monthlyInterestRate)
    return investment


def main(args):
    investmentAmount = eval(input("The amount invested: "))
    rate = eval(input("Annual interest rate: ")) / 1200
    displayList(investmentAmount, rate, 30)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
