# read values from data file
file_path = 'Day 2/Data.txt'
file = open(file_path, 'r')
strings = file.readlines()
# generate master password list
# [
# 	{
# 		'password': 'abc',
#		'letter': 'x',
#		'pos_1': 0,
#		'pos_2': 999
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
	# policy_tuple = ('policy_pos', ' ', 'letter')
	policy_tuple = policy.partition(' ')
	policy_pos = policy_tuple[0]
	policy_letter = policy_tuple[2]
	#pos_tuple = ('pos_1', '-', 'pos_2')
	pos_tuple = policy_pos.partition('-')
	pos_1 = pos_tuple[0]
	pos_2 = pos_tuple[2]
	# create dict for each password
	pass_dict = {}
	pass_dict['password'] = password
	pass_dict['letter'] = policy_letter
	pass_dict['pos_1'] = int(pos_1)
	pass_dict['pos_2'] = int(pos_2)
	pass_list.append(pass_dict)

# Check that the letter occurs EITHER in position 1 or 2 of password.
# Count total number of valid passwords
valid_count = 0
for entry in pass_list:
	password = entry['password']
	letter = entry['letter']
	pos_1 = entry['pos_1']
	pos_2 = entry['pos_2']
	check_1 = password[pos_1 - 1] == letter
	check_2 = password[pos_2 - 1] == letter
	if (check_1 + check_2) == 1:
		valid_count += 1

print(valid_count)
