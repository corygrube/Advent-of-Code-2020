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
	pass_dict['range_min'] = range_min
	pass_dict['range_max'] = range_max
	pass_list.append(pass_dict)

print(pass_list)