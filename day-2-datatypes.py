#100 days of code: day 2

#Data types, numbers, operators, type conversions & f-strings

#DATA TYPES

# STRINGS - alphabetical values in a string 
# e.g. "hello"
"Hello"[0]
# will provide you with the 1st character in the string
# programmers ALWAYS begin counting from zero
# computers work in binary 1/0 therefore 0 is a crucial character
# any characters printed within "" are treated as a text string
# e.g 
print("123" + "456") #will be presented as 123456 and not 579 

# INTEGERS - numberical values

# , within a numerical value as _
# e.g. 
1,000,000 #as 
1_000_000 #will be presented as 
1000000


# floats - numerical values with a demical point
# e.g. 
3.14159


# booleans - 
# only has 2 possible values
True 
#or 
False
# note the use of capital letters

#DATA TYPES CONT

num_char = len( input("what is your name? "))
print("your name has " + num_char + " characters.")

# Here you will receive a type error as your are attempting to concatenate 
# a STRING and a INTEGER, which is not possible without additional functions

# type check
print( type( len( input("what is your name"))))
# to determine the data type of the answer

#TYPE CONVERSION / TYPE CASTING

num_char # = integer
# to conver to a string
new_num_char = str(num_char)
# now the integet will be presnted as a string

#now you can produce this command as:

num_char = len( input("what is your name? "))
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")

# this command will run as all the components are of the same data type (STRINGS)

#Day 2 exercise

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

digit_one = int(two_digit_number[0])
digit_two = int(two_digit_number[1])

#int converts the numbers which have previously existed as a string in to an integet so they can be added together.

result = (digit_one + digit_two)
print(result)

# this will present each individual number from the original two digit number added together

# MATHEMATICAL OPERATORS

# addition
7+3

# subtraction
7-3

# multiplication
7*3

# division
7/3
# even if a division rounds equally in to a whole number, it will be presented as a float.

# exponent
7**3
# 7 to the power of 3 / or 7 cubed

#BODMAS
#Brackets, over, Division, Miltiplication, Addition, Substraction

# &/or 

# PEMDAS
# Parentheses, Exponent, Multiplication, Division, Addition, Subtraction 

print(3 * 3 + 3 / 3 - 3)

3*3 = 9
3/3 = 1
9+1 = 10
10-3 = 7

#BMI CALCULATOR

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

result_height = float(height)
# converts height from a string to a float
result_weight = int(weight)
# just incase people are weird...

BMI = (result_weight / result_height**2)

BMI_as_int = int(BMI)
# converts the value from a float to an integer
# otherwise you will receive a value with a large number of values after the decimal
print(BMI_as_int)
# provides a whole number value

#Number manipulation and F Strings

print(8/3)
# will provide you with a floating value of 
2.66666666667

# by converting the the value to an integer (int)
print(int(8/3))
# this will simply chop off all values after the decimal to rpovide a single number value
# instead of rounding as we would traditionally do
2

# to round the number correctly (round)
print(round(8/3))
#this will provide you with a correctly rounded single number value
3

# to round the number precisely to a given number of decimal places (,2)
print(round(8/3, 2))
# will provide a number with two values after the decimal place
2.67

# to divide to produce a single values integer you can also use a floor division (//)
print(8 // 3)
# this will provide you with a value of:
3
# this calculation does not round though

#clean divisions will always be presented with decimal places
print(4/2) 
# which is equal to 2
# will be presented as:
2.0

# saving answers as a variable
result = 4/2
result /= 2
print(result)
1

# if you wanted to track a persons score
score = 0
#everytime a person scores
score += 1
print(score)
1

#F Strings
score = 1              #integer
isWinning = True       #boolean
print("Your score is " + score)
# will present a type error because you are attempting to combine a string and an integer which is not possible without conversion
# to make the string work
# you must use an f string
print(f"Your score is {score}, you are winning is {isWinning}")
#your score is 0, you are winning

# Challenge
# life in weeks until you are 90

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_integer = (int(age))

days_left = ((90-age_as_integer)*365)
weeks_left = ((90-age_as_integer)*52)
months_left = ((90-age_as_integer)*12)

message = f"you have {days_left} days left, {weeks_left} weeks left and {months_left} months left until you are 90"
print(message)