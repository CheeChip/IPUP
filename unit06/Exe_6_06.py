#!/usr/bin/env python3

# Exe 6 显示图案

def displayPattern(n):
	width = getWidth(n)
	formatter = '{:%dd}' % (width)
	for row in range(1, n+1):
		print(' ' * (width + 1) * (n - row), end = '')
		print(*[formatter.format(i) \
			for i in range(row, 0, -1)], sep = ' ')


def getWidth(n):
	'''
	计算宽度，方便格式化对齐
	'''
	from math import log
	return int(log(n, 10)) + 1


def main(args):
	try:
		n = int(args[1])
	except IndexError:
		n = int(input("输入行数："))
		print()
	displayPattern(n)
	return 0


if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
