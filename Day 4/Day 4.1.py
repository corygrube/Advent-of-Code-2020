import pprint
# read values from data file
file_path = 'Day 4/Data.txt'
with open(file_path, 'r') as file:
	file_read = file.read()

#split into list on double line break
strings = file_read.split('\n\n')
# separate key:value pairs by ' '. Removes misc line breaks.
# generate list of dictionary
passports = []
for string in strings:
	passport_str = string.replace('\n', ' ')
	passport = {
		s.split(':')[0] : s.split(':')[1] for s in passport_str.split(' ')
	}
	passports.append(passport)

# check required keys. Assumptions:
# 	8=valid
# 	7=valid if cid is the missing key
# 	no passports will have more than 8 keys
valid = 0
for passport in passports:
	length = len(passport)
	if length <= 6:
		continue
	elif length == 7:
		if 'cid' not in passport:
			valid += 1
	else:
		valid += 1
print(valid)