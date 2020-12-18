# read values from input file
file_path = 'Day 6/input.txt'
with open(file_path, 'r') as file:
	input_file = file.read()

# split input file into groups on double line break
groups = input_file.split('\n\n')

# part 1
# iterate through groups on plane, calculate total counts
total = 0
for group in groups:
	# remove line breaks and convert to set of unique letters
	answers = set(group.replace('\n', ''))
	# length will equal unique answers - add to total
	total += len(answers)

print(total)