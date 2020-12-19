# read values from input file
file_path = 'Day 7/input.txt'
with open(file_path, 'r') as file:
	lines = file.readlines()

# Create dict of rules.
# key is outer bag, value is list of tuples rules
# where tuple = (qty, color) of contained bag(s)
rules = {}
for line in lines:
	# remove line breaks
	line = line.strip()
	# partition into outer/inner components
	partition = line.partition(' contain ')
	# remove filler text in outer
	color = partition[0].replace(' bags', '')
	
	# skip if no inner bags
	if partition[2] == 'no other bags.':
		continue
	
	# Split into stadard lists of contents
	contents = partition[2].split(', ')
	rule = []
	# bag = [qty, adj, color, filler text]
	for bag in contents:
		words = bag.split(' ')
		qty = int(words[0])
		color_x = ' '.join([words[1], words[2]])
		# create/append tuple to rule list
		rule.append((qty, color_x))
	
	# insert rule into rules
	rules[color] = rule