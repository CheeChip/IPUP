#!/usr/bin/env python3

# Exe 4 反向显示一个整数

def reverse(number):
	rev = 0
	while number > 0:
		rev = 10 * rev + number % 10
		number //= 10
	
	return rev


def main(args):
	try:
		number = int(args[1])
	except IndexError:
		number = int(input("输入一个整数："))
	print(number, "的反转是", reverse(number))
	
	return 0


if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
