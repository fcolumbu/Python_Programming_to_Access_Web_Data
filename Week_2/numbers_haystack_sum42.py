# numbers_haystack.py
#
# Author: Francis M. Columbus
# Date: 09/17/2016
# This program iterates through a text file and through the use of regular expressions,
# finds randomly embedded numbers and finds the sum of the numbers.
#
#

import re

def main():
# Initialize the variables
	lines =[]
	numbers = []
	total = 0
	line_count = 0
	num_count = 0

# Read the file and create a list of lines.
	lines = tuple(open('regex_sum_42.txt', 'r'))

	print'The file contains: ',len(lines),' lines.'
	print

# Using a regular expression, parse each line for embedded numbers.
	for line_count in range (0, len(lines) ):
		numbers = numbers + re.findall('[0-9]+',lines[line_count])

# Convert the number strings to integers and compute the sum.
	for num_count in range (0, len(numbers)):
		total = total + int(numbers[num_count])
#		print(int(numbers[num_count]))
		
	print
	print'We found the following numbers: ', (numbers)
	print
	print'The quantity of embedded numbers are: ', (len(numbers))
	print
	print'The sum of the embedded numbers in the file is:', (total)

	return 
main()