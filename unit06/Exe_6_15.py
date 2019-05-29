# Exe 15

def computerTax(status, taxableIncome):
    if status == 1:
        return singleTax(taxableIncome)
    elif status == 2:
        return mJointTax(taxableIncome)
    elif status == 3:
        return mSepTax(taxableIncome)
    elif status == 4:
        return headTax(taxableIncome)


def singleTax(taxableIncome):
    if taxableIncome <= 8350:       # 0.1
        tax = taxableIncome * 0.1
    elif taxableIncome <= 33950:    # 0.15
        tax = 8350 * 0.1 \
              + (taxableIncome - 8350) * 0.15
    elif taxableIncome <= 82250:    # 0.25
        tax = 8350 * 0.1 \
              + (33950 - 8350) * 0.15 \
              + (taxableIncome - 33950) * 0.25
    elif taxableIncome <= 171550:   # 0.28
        tax = 8350 * 0.1 \
              + (33950 - 8350) * 0.15 \
              + (82250 - 33950) * 0.25 \
              + (taxableIncome - 82250) * 0.28
    elif taxableIncome <= 372950:   # 0.33
        tax = 8350 * 0.1 \
              + (33950 - 8350) * 0.15 \
              + (82250 - 33950) * 0.25 \
              + (171550 - 82250) * 0.28 \
              + (taxableIncome - 171550) * 0.33
    else:                           # 0.35
        tax = 8350 * 0.1 \
              + (33950 - 8350) * 0.15 \
              + (82250 - 33950) * 0.25 \
              + (171550 - 82250) * 0.28 \
              + (372950 - 171550) * 0.33 \
              + (taxableIncome - 372950) * 0.35

    return tax


def mJointTax(taxableIncome):
    if taxableIncome <= 16700:      # 0.1
        tax = taxableIncome * 0.1
    elif taxableIncome <= 67900:    # 0.15
        tax = 16700 * 0.1 \
              + (taxableIncome - 16700) * 0.15
    elif taxableIncome <= 137050:   # 0.25
        tax = 16700 * 0.1 \
              + (67900 - 16700) * 0.15 \
              + (taxableIncome - 67900) * 0.25
    elif taxableIncome <= 208850:   # 0.28
        tax = 16700 * 0.1 \
              + (67900 - 16700) * 0.15 \
              + (137050 - 67900) * 0.25 \
              + (taxableIncome - 137050) * 0.28
    elif taxableIncome <= 372950:   # 0.33
        tax = 16700 * 0.1 \
              + (67900 - 16700) * 0.15 \
              + (137050 - 67900) * 0.25 \
              + (208850 - 137050) * 0.28 \
              + (taxableIncome - 208850) * 0.33
    else:                           # 0.35
        tax = 16700 * 0.1 \
              + (67900 - 16700) * 0.15 \
              + (137050 - 67900) * 0.25 \
              + (208850 - 137050) * 0.28 \
              + (372950 - 208850) * 0.33 \
              + (taxableIncome - 372950) * 0.35
    return tax


def mSepTax(taxableIncome):
    if taxableIncome <= 8350:       # 0.1
        tax = taxableIncome * 0.1
    elif taxableIncome <= 33950:    # 0.15
        tax = 8350 * 0.1 \
              + (taxableIncome - 8350) * 0.15
    elif taxableIncome <= 68525:    # 0.25
        tax = 8350 * 0.1 \
              + (33950 - 8350) * 0.15 \
              + (taxableIncome - 33950) * 0.25
    elif taxableIncome <= 104425:   # 0.28
        tax = 8350 * 0.1 \
              + (33950 - 8350) * 0.15 \
              + (68525 - 33950) * 0.25 \
              + (taxableIncome - 68525) * 0.28
    elif taxableIncome <= 186475:   # 0.33
        tax = 8350 * 0.1 \
              + (33950 - 8350) * 0.15 \
              + (68525 - 33950) * 0.25 \
              + (104425 - 68525) * 0.28 \
              + (taxableIncome - 104425) * 0.33
    else:                           # 0.35
        tax = 8350 * 0.1 \
              + (33950 - 8350) * 0.15 \
              + (68525 - 33950) * 0.25 \
              + (104425 - 68525) * 0.28 \
              + (186475 - 104425) * 0.33 \
              + (taxableIncome - 186475) * 0.35

    return tax


def headTax(taxableIncome):
    if taxableIncome <= 11950:      # 0.1
        tax = taxableIncome * 0.1
    elif taxableIncome <= 45500:    # 0.15
        tax = 11950 * 0.1 \
              + (taxableIncome - 11950) * 0.15
    elif taxableIncome <= 117450:   # 0.25
        tax = 11950 * 0.1 \
              + (45500 - 11950) * 0.15 \
              + (taxableIncome - 45500) * 0.25
    elif taxableIncome <= 190200:   # 0.28
        tax = 11950 * 0.1 \
              + (45500 - 11950) * 0.15 \
              + (117450 - 45500) * 0.25 \
              + (taxableIncome - 117450) * 0.28
    elif taxableIncome <= 372950:   # 0.33
        tax = 11950 * 0.1 \
              + (45500 - 11950) * 0.15 \
              + (117450 - 45500) * 0.25 \
              + (190200 - 117450) * 0.28 \
              + (taxableIncome - 190200) * 0.33
    else:                           # 0.35
        tax = 11950 * 0.1 \
              + (45500 - 11950) * 0.15 \
              + (117450 - 45500) * 0.25 \
              + (190200 - 117450) * 0.28 \
              + (372950 - 190200) * 0.33 \
              + (taxableIncome - 372950) * 0.35

    return tax


def main(args):
    print(' Taxable Income |'
          + format('Single', '^16s') + '|'
          + format('Married Joint', '^16s') + '|'
          + format('Married Seperate', '^16s') + '|'
          + format('Head of a House', '^16s'))
    print('-' * 16 + '+' + '-' * 16 + '+' + '-' * 16 + '+'
          + '-' * 16 + '+' + '-' * 16)
    
    income = 50000
    while income <= 60000:
        print(format(income, '^16d') + '|' +
              format(computerTax(1, income), '^16.0f') + '|' +
              format(computerTax(2, income), '^16.0f') + '|' +
              format(computerTax(3, income), '^16.0f') + '|' +
              format(computerTax(4, income), '^16.0f'))
        income += 50
        
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
