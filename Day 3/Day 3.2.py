# read values from data file
file_path = 'Day 3/Data.txt'
file = open(file_path, 'r')
strings = file.readlines()
# clean up strings list by removing line breaks
for i, string in enumerate(strings):
	strings[i] = string.strip()

def trees(right, down, row_max):
	trees = 0
	row_count = 0
	# Iterate through rows to at given slope
	for i, row in enumerate(strings):
		# Skip rows that aren't multiples of (down)
		if (i % down) != 0:
			continue 
		print('row ' + str(i) + ' passed')
		print(row)
		# current horiz position
		horiz_raw = row_count * right
		# effective horiz position, since row repeats after row_max
		horiz = horiz_raw % row_max
		print('row horiz: ' + str(horiz))
		# Increment trees for each tree at position horiz
		if row[horiz] == '#':
			trees += 1
			print('TREE')
		row_count += 1
		print('--------\n\n')
	return trees

# init length of each row
row_max = strings[0].__len__()
# eval different scenarios
trees_1 = trees(1, 1, row_max)
trees_2 = trees(3, 1, row_max)
trees_3 = trees(5, 1, row_max)
trees_4 = trees(7, 1, row_max)
trees_5 = trees(1, 2, row_max)
# multiple results together
product = trees_1 * trees_2 * trees_3 * trees_4 * trees_5
print(product)