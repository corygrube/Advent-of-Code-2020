# read values from data file
file_path = 'Day 1/Data.txt'
file = open(file_path, 'r')
strings = file.readlines()
# cast strings from data file to ints
ints = []
for string in strings:
	ints.append(int(string))
# sum all value pairs to find x + y + z = 2020
def search(ints):
	for x in ints:
		for y in ints:
			for z in ints:
				if (x + y + z) == 2020:
					result = x * y * z
					return result

result = search(ints)
print(result)