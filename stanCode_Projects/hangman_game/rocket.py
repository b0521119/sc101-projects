"""
File: rocket.py
Name: Jennifer Chueh
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This program is to built a rocket in different sizes.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	:return: Built a rocket head.
	"""
	for i in range(SIZE):
		for j in range(SIZE-i):
			print(' ', end='')
		for k in range(i+1):
			print('/', end='')
		for m in range(i+1):
			print('\\', end='')
		print("")


def belt():
	"""
	:return: Built a rocket belt.
	"""
	for i in range(1):
		print('+', end='')
		for j in range(SIZE*2):
			print('=', end='')
		print('+', end='')
		print("")


def upper():
	"""
	:return: Built a rocket upper-body.
	"""
	for i in range(SIZE):
		for j in range(1):
			print('|', end='')
		for k in range(SIZE-i-1):
			print('.', end='')
		for m in range(i+1):
			print('/\\', end='')
		for n in range(SIZE-i-1):
			print('.', end='')
		for o in range(1):
			print('|', end='')
		print("")


def lower():
	"""
	:return: Built a rocket lower-body.
	"""
	for i in range(SIZE):
		for j in range(1):
			print('|', end='')
		for k in range(i):
			print('.', end='')
		for m in range(SIZE-i):
			print('\\/', end='')
		for n in range(i):
			print('.', end='')
		for o in range(1):
			print('|', end='')
		print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()