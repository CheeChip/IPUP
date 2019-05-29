#!/usr/bin/env python3

# Exe 5 对三个数排序

def bobbleSort(nums):
	length = len(nums)
	for i in range(length - 1):
		for j in range(i + 1, length):
			if nums[j-1] > nums[j]:
				nums[j-1], nums[j] = nums[j], nums[j-1]
	return nums

def main(args):
	try:
		nums = [args[1], args[2], args[3]]
	except IndexError:
		nums = list(eval(input("Enter three numbers: ")))
	
	print("The sorted numbers are", end=' ')
	print(*bobbleSort(nums), sep=', ')
	
	return 0


if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
