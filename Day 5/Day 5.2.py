# read values from data file
file_path = 'Day 5/Data.txt'
with open(file_path, 'r') as file:
	manifest = file.readlines()

# seat ID calc function
def seat_id(seat):
	# convert row substring to binary, then to int
	row_code = seat[:7].replace('F', '0').replace('B', '1')
	row = int(row_code, 2)
	
	# convert col substring to binary, then to int
	col_code = seat[7:].replace('L', '0').replace('R', '1')
	col = int(col_code, 2)
	
	# convert row/col to seat_id
	seat_id = row * 8 + col
	return seat_id

# loop through different passenger seat codes. 
# Track found seats in list.
highest = 0
seats = []
for seat in manifest:
	seat = seat_id(seat)
	seats.append(seat)

# sort seats, init missing seat var
seats.sort()
missing = 0
# Check each seat to see if (next seat - 1) is the same.
# If different, (seat + 1) must be missing
for i in range(len(seats)):
	print(seats[i])
	if seats[i] == (seats[i+1] - 1):
		continue
	else:
		missing = seats[i] + 1
		break

print(missing)