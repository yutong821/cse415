	# Top side
	if i == 0:
		# left top conner
		if j == 0:
			if current_s[len(row)][len(column)] == " ":
				count = count + 1
			for m in (0,1):
				if current_s[len(row)][j+m] == " ":
					count = count + 1
				if current_s[i+m][len(column)] == " ":
					count = count + 1
		# right top conner
		elif j == len(column):
			if current_s[len(row)][0] == " ":
				count = count +1
			for m in (1,0):
				if current_s[len(row)][j-m] == " ":
					count = count + 1
				if current_s[i-m][0] == " ":
					count = count + 1
		# else
		else:
			for n in (1, 0 ,-1):
				if current_s[len(row)][j-n] == " ":
					count = count + 1
				if current_s[i-n][j-n] == " ":
					count = count +1
	 # Bottom side
	elif i == len(row):
		# left bottom conner
		if j == 0:
			if current_s[0][len(column)] == " ":
				count = count + 1
			for m in (0,1):
				if current_s[0][j+m] == " ":
					count = count + 1
				if current_s[i+m][len(column)] == " ":
					count = count + 1
		# right bottom conner
		elif j == len(column):
				if current_s[0][0] == " ":
					count = count + 1
				for m in (1, 0):
					if current_s[0][j-m] == " ":
						count = count + 1
					if current_s[i-m][0] == " ":
						count = count + 1
				else:
					for n in (1, 0 , -1):
						if current_s[0][j-n] == " ":
							count = count + 1
						if current_s[i-n]





	elif i != 0 and j != 0 and i!= len(row) and j!= len(column):
		for m in (1, 0, -1):
			for n in (1, 0, -1):
				current_s[i-m][j-n] == " ":
				count = count +1
	return count
