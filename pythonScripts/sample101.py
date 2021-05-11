#!/bin/python3

# Importing

print("importing examples: ")

import sys #system functions and perameters 

from datetime import datetime
print(datetime.now())


	


# advance strings 

print("Advanced Strings:")
my_name = "Alberto"
print(my_name[0]) #First character
print(my_name[-1]) #Last character

sentence = "This sentence is pointless."

print(sentence[:4]) # first word 
print(sentence[-11:-1]) # last word no

print(sentence.split()) #split sentence by delkimter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception = " moaney is not my god, 'but need to earn to survive'"
print(quoteception)

quoteception = " to afirm, \"money is not my god\""
print(quoteception)

print("A in Apple")
letter = "A"
word = "Apple"
print(letter in word) # boolean

print("A in Apple")
letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) # boolean case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "     				delimeter 			"
print(too_much_space.strip())

full_name = "lberto sbicca"
print(full_name.replace("lberto", "alberto"))
print(full_name.find("sbicca"))


movie = "gladiator"
print("my favourite movie is {}.".format(movie))

def favourite_book(tittle, author):
	fav = "my favourite book is \"{}\", auther {}.".format(tittle, author)
	return fav
print(favourite_book("the trigger", "david icke"))

def new_line(): #define new line 
	print('\n') # auto print new line 
	
new_line()


# dictionaries {}

print("dictionaries are keys and values: ")
drinks = {"White Rissian": 7, "DepthCharge": 10, "BloodyMary": 5, "Martini": 12} # the drink is a key and the numerical is the value
print(drinks)

new_line()

employees = {"Finance": ["rob", "dave", "june"], "IT": ["mark", "Rebecca", "Ross"], "HR": ["dean", "alan", "chriss"]}
print(employees)

employees['Legal'] = ["judge-dredd"] #add new key & value pair
print(employees)

employees.update({"Sales": ["arnold", "luke", "mandy"]})
print(employees)

drinks['White Russin'] = 100
print(drinks)

print(drinks.get("White Rissian"))

print(drinks.get("martini"))







 
