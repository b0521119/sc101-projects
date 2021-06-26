"""
File: coin_flip_runs.py
Name: Jennifer Chueh (2hr)
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r
import random


NUM_ROLLS = 15


def main():
	"""
	This program should simulate coin flip(s)
	with the number of runs input by users.
	"""
	print('Let\'s flip a coin!')
	num_runs = int(input('Number of runs: '))

	coin1 = random.choice('HT')  # coin1 = random.choice(['H','T'])
	run = 0
	sequence = coin1
	is_in_a_row = False  # is it a run?

	while True:
		coin2 = random.choice('HT')
		if coin1 == coin2:
			if not is_in_a_row:
				run += 1
				is_in_a_row = True
				sequence = sequence + coin2
				if run == num_runs:
					break
		else:
			is_in_a_row = False
			sequence = sequence + coin2
		coin1 = coin2
	print(sequence)






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
