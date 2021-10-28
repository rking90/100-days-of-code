#100 days of code: Day 1
# 
# Printing
# 

print("Hello world!") 
# print - this command asks for the words within the brackets to be printed as requested
# functions are presented in yellow

#Strings
# A string of charactersIn our example above our string is Hello World
# " + " demonstrate the beginning and the end of the string of characters
# strings are presented in orange
#

#Exercise 1-1
# Request the computer to print the following statements
# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print
#

print("Day 1 - Python Print Function")

print("The function is declared like this:")

print("print('what to print')")

# python doesnt care if you use "" or '' to denote strings
# but in print fuction 3, you would have two sets of "", 
# so you need to differentiate between a string and a piece of the text that includes quotations.
# "print("what to print")" will produce a syntax error due to its inability to differentiate
# "print('what to print')" and 'print("what to print")' will run correctly and do exactly the same thing

#to create a new line and repeat the text

print("Hello world!\nHello world!")  

#concatenate strings
print("Hello" + "Rachel")
#This command will present HelloRachel as we have not requested for a space to be present between the words

#2 methods to rectify this

print("Hello " + "Rachel")
# Here I have created a space by adding one in to the hello string "hello "
# you could also create a space before the Rachel string " Rachel"

#or
print("Hello" + " " + "Rachel")
# Here I have created an space string entirely independent of the strings between the two + Symbols

#input function - Stepwise
input ("what is your name")
# a prompt for the user to input information requested - indicated by a blinking cursor
name = (input)
print("hello " + name)

#or
# input function as integrated steps
print("Hello " + input("what is your name?"))
# initially commits the request for the users name
# then commits the print function of "hello name"

#Input functions

name = input("what is your name? ") 
# a space between the prompt and the end ", will provide a space between the prompt and the cursor in the terminal
# requests the user to provide their name
print(len(name))
#len = length of the string
# prints the number of characters within the variable saved as name

#or

print( len( input("what is your name? ")))
# as before - provides a integrated command rather than a stepwise
# although input has been received, it does not save the name as a usable variable

# variables are presented in blue

# in the exercise below
# We are attempting to swap the contents of a and b when they are printed.
# the catch - without simply stating a=b and b=a.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
# c is then given the value provided to a
a = b
# a is then given the value provided to b
b = c
# b is then given the value provided for c (which is actually the value given to a)

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# when using variables, ensure you use logical names 
# so when you return in the future or someone else utilised your script that it all makes sense
# ANNOTATE EVERYTHING!!!

# End of day project - Band name generator - completed

#END OF DAY 1