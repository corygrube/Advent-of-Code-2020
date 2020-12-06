# read values from data file
file_path = 'Day 2/Data.txt'
file = open(file_path, 'r')
strings = file.readlines()
# generate master password list
# [
# 	{
# 		'password': 'abc',
#		'letter': 'x',
#		'range_min': 0,
#		'range_max': 999
# 	},
#	...
# ]
pass_list = []
for string in strings:
	# string = 'policy : password'
	# pass_tuple = ('policy', ':', 'password')
	pass_tuple = string.partition(':')
	policy = pass_tuple[0].strip()
	password = pass_tuple[2].strip()
	# policy_tuple = ('policy_range', ' ', 'letter')
	policy_tuple = policy.partition(' ')
	policy_range = policy_tuple[0]
	policy_letter = policy_tuple[2]
	#range_tuple = ('range_min', '-', 'range-max')
	range_tuple = policy_tuple[0].partition('-')
	range_min = range_tuple[0]
	range_max = range_tuple[2]
	# create dict for each password
	pass_dict = {}
	pass_dict['password'] = password
	pass_dict['letter'] = policy_letter
	pass_dict['range_min'] = int(range_min)
	pass_dict['range_max'] = int(range_max)
	pass_list.append(pass_dict)

# count characters within each password to find
# total number of valid passwords
valid_count = 0
for entry in pass_list:
	password = entry['password']
	letter = entry['letter']
	count = password.count(letter)
	range_min = entry['range_min']
	range_max = entry['range_max']
	if range_min <= count <= range_max:
		valid_count += 1

print(valid_count)