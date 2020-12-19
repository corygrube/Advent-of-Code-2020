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

# function to recursively search through bags
# returns true if 'shiny gold' is found.
def bag_search(color):
	# arg check
	if color not in rules:
		return False
	
	# iterate through list of tuples (contained bags)
	# return True on shiny gold
	# recurse through any other colors. If gold found, return True
	for bag in rules[color]:
		if bag[1] == 'shiny gold':
			return True
		if bag_search(bag[1]):
			return True
	
	return False

# part 1
# run bag_search for each rule in rules. 
# Add 1 for each shiny gold found
count = 0
for color in rules:
	if bag_search(color):
		count += 1
print(count)