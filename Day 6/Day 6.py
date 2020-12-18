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

# part 2
# iterate through groups on place, calculate new total
total = 0
for group in groups:
	# split group into list of people, iterate
	people = group.splitlines()
	# create list of sets (one per person)
	sets = [set(person) for person in people]
	# check intersection of sets 1+ with set 0 - add to total
	answers = sets[0].intersection(*sets[1:])
	total += len(answers)

print(total)