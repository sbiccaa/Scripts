#!/bin/python3


#print string 
print("Strings and Things:")
print("""Hello this is 
a milti-line string""")
print("This is "+" a String")
print("\n") #new line

#maths
print("math time")
print(50 + 550) #add
print(50 - 50) #subtract
print(50 * 59) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 500) #PEMDAS
print(50 ** 2) #exponent
print(50 % 6) #modulo
print(50 // 6) #number without leftovers

print("\n") #new line

# variable & methods
print("Fun with variables & methods:")
quote = "all is fare in love and war"
print(len(quote)) #length
print(quote.upper()) #turns all in tio uppcase 
print(quote.lower()) #turns all lowercase
print(quote.title()) #turns all into title form


name = "Alberto"
age = 52 #int
IQ = 180.0 #float

print(int(age))
print(int(52.11)) #wont round the number
print("my name is " + name +  " and I am " + str(age) + " years old ")

print("\n") #new line

#functions
print("now some functions:")
def Who_am_I():
	name = "Alberto"
	age = 52
	print("my name is " + name +  " and I am " + str(age) + " years old ")
Who_am_I()

#adding new perameters
def add_one_hundred(num):
	print(num + 1000)

add_one_hundred(100)

#add in multiple peramters 

def add(x,y):
	print(x + y)

add(1,7)
add(300,300)


#using return

def multiply(x,y):
	return x * y

print(multiply(7,7))


#square root
def square_root(x):
	return x ** .5

print(square_root(11625000))






