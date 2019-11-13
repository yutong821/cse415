def neighbors_location(i, j):
	# current_s = self.board
	current_s = \
               [[' ','-',' ',' '],
                [' ','-',' ','-'],
                ['-','-',' ',' '],
                [' ',' ','-',' ']]
	count = 0
	row = len(current_s)
	column = len(current_s[0])
	print(row)
	print(column)
	direction = [None]*8
	# dir 1
	if i == 0:
		if j == 0:
			direction[0] = [row, column]
		else:
			direction[0] = [row, j - 1]
	elif i == row:
		if j == 0:
			direction[0] = [i-1, column]
		else:
			direction[0] = [i-1, j -1]
	else:
		direction[0] = [i-1, j-1]

	# dir 2
	if i == 0:
		direction[1] = [row, j]
	else:
		direction[1] = [i-1, j]

	# dir 3
	if i == 0:
		if j == column:
			direction[2] = [row, 0]
		else:
			direction[2] = [row, j+1]
	elif i == row:
		if j == column:
			direction[2] = [i-1, j]
		else:
			direction[2] = [i-1, j+1]
	else:
		direction[2] = [i-1, j+1]

	# dir 4
	if j == 0:
		direction[3] = [i, column]
	else:
		direction[3] = [i, j-1]


	# dir 5
	if j == column:
		direction[4] = [i, 0]
	else:
		direction[4] = [i, j+1]

	# dir 6
	if i == row:
		if j == 0:
			direction[5] = [0, column]
		else:
			direction[5] = [0, j-1]
	elif i == 0:
		if j == 0:
			direction[5] = [i+1, column]
		else:
			direction[5] = [i+1, j-1]

	else:
		direction[5] = [i+1, j-1]

	# dir 7
	if i == row:
		direction[6] = [0, j]
	else:
		direction[6] = [i+1, j]

	# dir8
	if i == row:
		if j == column:
			direction[7] = [0, 0]
		else:
			direction[7] = [0, j+1]
	elif i == 0:
		if j == column:
			direction[7] = [i+1, 0]
		else:
			direction[7] = [i+1, j+1]
	else:
		direction[7] = [i+1, j+1]

# 	print(direction)
# neighbors_location(0,0)
