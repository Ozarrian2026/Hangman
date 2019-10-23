import time
import os

ASCII = ['''
    +----+
    |    |
         |
         |
         |
 =========''','''
    +----+
    |    |
    O    |
         |
         |
 =========''','''
    +----+
    |    |
    O    |
    |    |
         |
 =========''','''
    +----+
    |    |
   \O    |
    |    |
         |
 =========''',''' 
    +----+
    |    |
   \O/   |
    |    |
         |
 =========''','''
    +----+
    |    |
   \O/   |
    |    |
   /     |
 =========''','''
    +----+
    |    |
   \O/   |
    |    |
   / \   |
 ========='''      ]


print(ASCII[0])
myWord = "minecraft"
Word = list(myWord)

print("Welcome to Hangman!")
guessList = []
missed = []
for letter in Word:
	guessList.append("_")
print(guessList)

while True:
	for letter in Word:
		guessList.append("_")
		print(guessList)
		guesses = input("Enter your letter: ")
	if guesses == "m":
		guessList[0] = "m"
		print(guessList)

	if guesses == "i":
		guessList[1] = "i"
		print(guessList)
	if guesses == "n":
		guessList[2] = "n"
		print(guessList)
	if guesses == "e":
		guessList[3] = "e"
		print(guessList)
	if guesses == "c":
		guessList[4] = "c"
		print(guessList)
	if guesses == "r":
		guessList[5] = "r"
		print(guessList)
	if guesses == "a":
		guessList[6] = "a"
		print(guessList)
	if guesses == "f":
		guessList[7] = "f"
		print(guessList)
	if guesses == "t":
		guessList[8] = "t"
		print(guessList)
	else:
		print(ASCII[1])
		print("This is not a letter and is added to the miss box")
		missed.append(guesses)
		print(missed)
		print("Try again")
	break
