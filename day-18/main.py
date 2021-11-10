"""
https://adventofcode.com/2021/day/18
"""

import sys

INPUT_FILE_PATH = "./part_01_example_input.txt"


def main():
	try:
		with open(INPUT_FILE_PATH) as input_raw:
			pass

	except IOError as ioe:
		print("{}\nError opening {}. Terminating process.".format(ioe, INPUT_FILE_PATH), file=sys.stderr)
		sys.exit(1)


def part_1():
	pass


def part_2():
	pass


if __name__ == '__main__':
	main()
