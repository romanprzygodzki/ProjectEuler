"""
Project Euler
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Natural Numbers are counting numbers, generally limited to non-negative integers. Whether zero is a natural number is up for debate but moot for this problem.
"""

import numpy as np

natural_numbers = np.arange(1000)

natural_number_sum = 0
for i in natural_numbers:
	if (i % 3 == 0) or (i % 5 == 0):
		natural_number_sum += i

print "The sum of all natural numbers that are a multiple of 3 or 5 is %s" % '{:,.0f}'.format(natural_number_sum)