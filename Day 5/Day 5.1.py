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
# If a seat has a higher ID than any checked,
# 	mark it as the new highest
highest = 0
for seat in manifest:
	seat = seat_id(seat)
	print(seat)
	if seat > highest:
		highest = seat
print(highest)