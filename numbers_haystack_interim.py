# numbers_haystack.py
import re

def main():
	numbers = []
	total = 0
	line_count = 0
	num_count = 0
#	f = open ('regex_sum_317861.txt', 'r')
#	text_file = f.read()
	lines = tuple(open('regex_sum_317861.txt', 'r'))
#	print(text_file)
	print'The file contains: ',len(lines),' lines.'

	for line_count in range (0, len(lines) ):
		numbers = numbers + re.findall('[0-9]+',lines[line_count])

	for num_count in range (0, len(numbers)):
		total = total + int(numbers[num_count])
		print(int(numbers[num_count]))

	print(numbers)
	print(len(numbers))

	print(total)
#	f.close()
	return 
main()