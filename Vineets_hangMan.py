import random
import sys

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
MAX_INCORRECT = len(HANGMAN) - 1
WORD_LIST = ("Google", "Dell", "Cloud", "Ram", "Address")
WORD = random.choice(WORD_LIST)

word = WORD.lower()
incorrect = 0
letters_used = []

def get_letter():
	if sys.version_info[0] < 3:
		user_input = raw_input("Enter a letter -> ").lower()
	else:
		user_input = input("Enter a letter -> ").lower()
	
	# if user wants to exit
	if user_input == 'exit':
		sys.exit(0)
	
	# if length of String input isn't 1 (it isn't a character)
	if len(user_input) != 1:
		print("\nInput is too long!\n")
		return ''
	
	# if character is not a letter
	if not user_input.isalpha():
		print("\nInput is not a character!\n")
		return ''
	
	# if the letter is previously used
	if user_input in letters_used:
		print("\nYou have previously guessed this letter!\n")
		return ''
	
	return user_input

def print_word_letters():
	output = ""
	# print dashes, and letters used
	for letter in WORD.lower():
		if letter in word:
			output += "_ "
		else:
			output += (letter.upper() + " ")
	print(output + "\n")

def print_letters_guessed():
	output = "Letters guessed: "
	for letter in letters_used:
		output += (letter.upper() + " ")
	print(output + "\n")

print(WORD)

while incorrect < MAX_INCORRECT:
	print(HANGMAN[incorrect])
	
	print_word_letters()
	print_letters_guessed()
	print("\n")
	
	# no do-while loop in Python!
	letter = get_letter()
	while letter == '':
		letter = get_letter()
	
	letters_used.append(letter)
	if letter.lower() not in word.lower():
		print("Incorrect guess!")
		incorrect += 1
	else:
		print("Correct guess!")
		word = word.replace(letter, '')
		# if the word is empty (Strings are falsey)
		if not word:
			print("\n")
			print_word_letters()
			print("You won!")
			break;
else:
	print(HANGMAN[incorrect])
	print("You lost!")
	print("The word was: " + WORD)

print("\n\nThanks for playing!\n\n")
