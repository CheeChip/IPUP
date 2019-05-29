#!/usr/bin/env python3

# Exe 03 判断回文数

def reverse(number):
	res = 0
	while number > 0:
		res = 10 * res + number % 10
		number //= 10
	return res


def isPallindrome(number):
	revNumber = reverse(number)
	return number == revNumber
	

def main(args):
	try:
		number = int(args[1])
	except IndexError:
		number = int(input("输入一个整数："))
	print(number, 
		("是" if isPallindrome(number) else "不是") + "一个回文数")
	return 0


if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

