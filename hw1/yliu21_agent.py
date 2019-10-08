from re import * 
import random 

def introduce():
    return("My name is Yoto, and I am waitress in our local resuanrant. I was programed by Yutong." \
        "If you don't like the way I deal, contact her at yliu21@uw.edu." \
        "Hello. How can I help you? ")

def agentName():
    return 'Yoto'


def Shrink():
    while True:
        theInput = input('TYPE HERE:>> ')
        if match('bye',theInput):
            return('Goodbye!')
        
        respond(theInput)


def respond(theInput):
	wordlist = split(' ',remove_punctuation(theInput))
    # undo any initial capitalization:
	wordlist[0]=wordlist[0].lower()
	mapped_wordlist = you_me_map(wordlist)
	mapped_wordlist[0]=mapped_wordlist[0].capitalize()

	# Rule 1: Open words: help
	if ("Hi" or "Hello") in wordlist:
		return("Hello. I am Yoto. How can I help you?")


	# Rule 2: Table 
	if 'reservation' in wordlist:
		return("Please wait. How many people for you group?")
	if "smoking" in wordlist:
		return("Sorry, there is no smoking")

	# Rule 3: Check number of people 
	if wordlist[0].isnumeric():
		if int(wordlist[0]) > 20:
			return("Sorry, your reservation is for 19 person.")
		else:
			return("Follow me. There is your table.")

	# Rule 4: Menu
	if "menu" in wordlist:
		return("There is today's menu. what do want first?" )

	
	# Rule 5: Circle respond (question for order)
	if ("recommendation" or "advice") in wordlist:
		return circlerespond1()
 	
 	# Rule 6: Random(Drink recommendation)
	if "drinks" in wordlist:
			return RandomDrink()

	# Rule 7: Random(appetizer recommendation)
	if "appetizers" in wordlist:
			return RandomAppetizer()

	# Rule8: Random(main recommendation)
	if "main" in wordlist:
			return RandomMain()

	# Rule 9: Random(dessert)
	global store
	if "desserts" in wordlist:
		store = RandomDessert()
		return("Do you want a small bowl of " + store)
		return

	# Rule9: Circle(maindish recommendation)
	if set(Meatlist) & set(wordlist):
		return MeatRecommendation(theInput)
	elif 'meat' in wordlist:
		return circlerespond2()

	# Rule 10: memory
	if "more" in wordlist:
		return("Do you want more " + store)

	# # Rule 11: memory + no
	if "than" in wordlist:
		return("Sorry, we only have " + store)

	# Rule 12: check
	if 'full' in wordlist:
		return("Are you ready to check?")

	# Rule 13:no wine
	if "wine" in wordlist:
		return("Sorry, but the bar is closed.")


	# Rule 14: finish
	if "check" in wordlist:
		return('No problem. There you are. Have a good night. bye')

	if 'bye' in wordlist:
		return('bye')

	#15 other thing
	return ("Hello. How can I help you? ")
	# return("Sorry, do you want to try different thing?")

# create the circle respond for asking order
circleRes = ["Do you want desserts?",
"Do you want drinks?",
"Do you want appetizers?",
"Do you want main courses?"]

count = 0
def circlerespond1():
    global count
    count += 1
    return(circleRes[count % 4])




# create the circle respond for food type
Meatlist =["beef", "chicken", "seafood", "lamb"]
count2 = 0
def circlerespond2():
    global count2
    count2 += 1
    return("Sorry, we do not have that. Any other meat main dishes? How about "+Meatlist[count2%4])

# create the random feature
def RandomDrink():
    randomIndex = random.randint(0,4)
    Randomrespond = ["soda", "tea", "wine", "water", "cocktail"]
    RecommendationDrink = "Do you want a cup of " + Randomrespond[randomIndex] + "?"
    return(RecommendationDrink)

def RandomAppetizer():
    # random suggest Appetizer 
    randomIndex = random.randint(0,4);
    Randomrespond = ["fried chicken", "fresh oyster", "crab cake", "Lemon Pepper Shrimp", "Light & Crispy Baked Onion Rings"]
    RecommendationAppetizer = "Do you want a plate of " + Randomrespond[randomIndex] + "?"
    return(RecommendationAppetizer)

count1 =-1
def RandomMain():
    # cycle suggest Main
    global count1
    count1 += 1
    Randomrespond = ["vege", "meat"]
    RecommendationMain = "Do you want the " + Randomrespond[count1 % 2] + " as your main dishes?"
    return(RecommendationMain)

def RandomDessert():
 	# random suggest dessert
 	randomIndex = random.randint(0,3);
 	Randomrespond = ["icecream", "cake", "macaroon", "mochi"]
 	RecommendationDessert =Randomrespond[randomIndex]
 	return RecommendationDessert

def MeatRecommendation(theInput):
	randomIndex = random.randint(0,4);
	beef = ["Ribeye Steak", "Spencer Steak", "Delmonico Steak", "Cowboy Steak", "Rib Steak"]
	chicken = ["fried chicken", "Bbq chicken", "G chicken",  "G chicken", "G chicken",]
	if 'beef' in theInput:
		Recommendation= "Do you want the combo specical  " + beef[randomIndex]
	elif 'chicken' in theInput:
		Recommendation = "Do you want the combo specical  " + chicken[randomIndex]
	return(Recommendation)





def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")    

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where','how'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do','can','should','would'])

PUNTS = ['Please go on.',
         'Tell me more.',
         'I see.',
         'What does that indicate?',
         'But why be concerned about it?',
         'Just tell me how you feel.']

punt_count = 0
def punt():
    'Returns one from a list of default responds.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])

# Shrink() 