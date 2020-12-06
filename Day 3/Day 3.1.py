# read values from data file
file_path = 'Day 3/Data.txt'
file = open(file_path, 'r')
strings = file.readlines()
# clean up strings list by removing line breaks
for i, string in enumerate(strings):
	strings[i] = string.strip()
# init trees hit, steps right per row (e.g. 3 right/1 down),
# and length of each row
trees = 0
right = 3
row_max = strings[0].__len__()
# Iterate through rows to at given slope
for i, row in enumerate(strings):
	# current horiz position
	horiz_raw = i * right
	# effective horiz position, since row repeats after row_max
	horiz = horiz_raw % row_max
	# Increment trees for each tree at position horiz
	if row[horiz] == '#':
		trees += 1
print(trees)