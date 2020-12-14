import re
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

# high level function to run various key checks
# return false if any fail. If all passed, return true
def check(passport):
	if not byr_check(passport['byr']):
		return False
	if not iyr_check(passport['iyr']):
		return False
	if not eyr_check(passport['eyr']):
		return False
	if not hgt_check(passport['hgt']):
		return False
	if not hcl_check(passport['hcl']):
		return False
	if not ecl_check(passport['ecl']):
		return False
	if not pid_check(passport['pid']):
		return False
	if 'cid' in passport:
		if not cid_check(passport['cid']):
			return False
	return True

# functions for key checking.
# returns true if valid, false if invalid
def byr_check(byr):
	if 1920 <= int(byr) <= 2002:
		return True
	return False
def iyr_check(iyr):
	if 2010 <= int(iyr) <= 2020:
		return True
	return False
def eyr_check(eyr):
	if 2020 <= int(eyr) <= 2030:
		return True
	return False
def hgt_check(hgt):
	if 'cm' in hgt:
		split = hgt.split('cm')
		if 150 <= int(split[0]) <= 193:
			return True
	elif 'in' in hgt:
		split = hgt.split('in')
		if 59 <= int(split[0]) <= 76:
			return True
	return False
def hcl_check(hcl):
	match = re.match(r'^#[0-9a-fA-F]{6}$', hcl)
	if match:
		return True
	return False
def ecl_check(ecl):
	ecl_valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if ecl in ecl_valid:
		return True
	return False
def pid_check(pid):
	if len(pid) == 9 and pid.isnumeric():
		return True
	return False
def cid_check(cid):
	return True

# check required keys for validity. Assumptions:
# 	8=valid number
# 	7=valid number (if cid is the missing key)
valid = 0
for passport in passports:
	length = len(passport)
	if length == 7:
		if 'cid' not in passport:
			if check(passport):
				valid += 1
	elif length == 8:
		if check(passport):
			valid += 1
print(valid)
