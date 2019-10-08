# 1. five_x_cubed_plus_2(3) -> 137
def five_x_cubed_plus_2(x):
	print(x**3*5+2)
five_x_cubed_plus_2(3)	
five_x_cubed_plus_2(30)
five_x_cubed_plus_2(1)

# 2. triple_up([2, 5, 1.5, 100, 3, 8, 7, 1, 1, 0, -2])  ->  [[2, 5, 1.5], [100, 3, 8], [7, 1, 1], [0, -2]]

def triple_up(x):
	print([x[i:i+3] for i in range(0,len(x),3)])
triple_up([2, 5, 1.5, 100, 3, 8, 7, 1, 1, 0, -2])
triple_up([5, 8, 9, 10, 788, 23, 4, 7, 0, 24]) 
triple_up([5, 6, 7, 8])

# 3. mystery_code("abc Iz th1s Secure? n0, no, 9!")

def mystery_code(x):
	result = ""
	offset = ord("V") - ord("A")
	offset_isupper = ord("Z") - ord("U")
	for i in x:
		if i.isalpha():
			if ord(i) > ord("e") and i.islower():
				new_cha = chr(ord(i.swapcase()) - offset_isupper)
			elif ord(i) > ord("E") and i.isupper():
				new_cha = chr(ord(i.swapcase()) - offset_isupper)
			else:
				new_cha = chr(ord(i.swapcase())	+ offset)
		else:
			new_cha = i

		result = result + new_cha
	print(result)

mystery_code("abc Iz th1s Secure? n0, no, 9!")
mystery_code("what do y0u Wantt2 kNow? An9thin9! I0!")	
mystery_code("Hello! I 0m a G00d PERson!")
 
# 4. future_tense(['Yesterday', 'I', 'ate', 'pasta', 'and', 'today', 'I', 'am', 'having', 'soup']) ->
# ['Tomorrow', 'I', 'will', 'eat', 'pasta', 'and', 'tomorrow', 'I', 'will', 'be', 'having', 'soup']

#  future_tense(['Life', 'is', 'good', 'now']) ->
# ['Life', 'will', 'be', 'good', 'tomorrow']
def future_tense(x):
	dic = {"is":["will","be"], "are":["will"," be"], "am":["will"," be"], "Yesterday":"Tomorrow", "yesterday":"tomorrow",
	"now":"tomorrow", "Now":"Tomorrow", "today":"tomorrow", "Today": "Tomorrow",
	 "ate":["will", "eat"], "eat":["will", "eat"], "had" : ["will"," have"], "have":["will", "have"],
	 "did":["will","do"], "do" : ["will","do"], "went": ["will","go"], "go":["will","go"]
	}
	result = []
	for i in x:
		if i in dic.keys():
			ele = dic[i]
			if isinstance(ele, list):
				result = result + ele
			else:
				result.append(ele)
		else:
			result.append(i)
	print(result)	
future_tense(['Yesterday', 'I', 'ate', 'pasta', 'and', 'today', 'I', 'am', 'having', 'soup']) 

future_tense(["I", "am", "taking", "CSE", "415","now", "!", "It", "is", "a", "fun", "class", "."])

future_tense(["This", "class", "is", "fun"])
