#Types of functions

#a function is declared
#print
#input
#len
# round

# Types of errors
#

#When you run the code, errors are identified one at a time. So won't move to the next error unless previous one is fixed

#IndentationError
#SyntaxError
# NameError (variable names)
# TypeError

#Day 1 - Printing, Commenting, Debugging, String Manipulation, and Variables

#1.1 Printing
#Print is a function
#the function is declared like this: print("what to print")
#single or double quotes to interpret a str. Both are fine.
#content inside '' or "" is interpreted as str not code. Hence don't use two "" or two '' in the same line. Use both. Example below:
#print('print("what to print")') or print("print('what to print')") Reasoning below
#because if the line is print("print("what to print")"), it will give a syntax error. Reasoning below
#Python considers "print(" as str and ")" as str and what to print as code.
#\n for printing content on the next line but written inside quotes "" like below. 
#print("Hello World!\nHello World!") no gaps between each line before and after \n unless a space needed before first word
#Str concatination adding + between characters to merge into one
#Python reads from inside to outside

#1.2 Debugging
# Tip - Notice the color change of the code. Ex, Syntax highlighting

#1.3 Commenting
# Tip - Make a comment above a line

#1.4 String Manipulation

#input("prompt for the user")
#The program ends only after the user adds a prompt

#len
#print(len(input("What is your name? ")))

#1.5 Variables
# assigns and saves anything after the = to the bucket to before the =
# the bucket is called a variable
# print(variable) allows the variable's content to be printed at any point inside the code
# the content assigned to a variable can change
# naming variables - Make the code readable
# can't have space in between words in a variable. Use _
# numbers cannot be at the start of the name
# don't use function names to name a variable

# Switch the values of the two variables around
#a = input("a: ")

# b = input("b: ")
# c = a
# a = b
# b = c
# print(a)
# print(b)

#Day 2
# datatype, numbers, operations, Type conversions, f-strings

#2.1 Datatypes

#String str " "

# Subscripting is pulling out a particular element from a str:
# print("Hello"[0]) will give H

#Integer int

# whole numbers. To declare an integer, write a number without anything else. Ex, 1234 + 455 will add these numbers.
# To make a number more readable, can use _ in stead of , and the computer will interpret it as one number. Ex, 100_000_000 will be 100000000 for the computer

#Float float
# decimal numbers

#Boolean bool
# Two possible values
# True
# False
# Starts with a capital letter has no "" marks

# check type like so: type(variable)

#2.2 Numbers

#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#number = input("Please enter a two digit number\n")
#first_digit = int(number[0])
#second_digit = int(number[1])
#new_digit = first_digit + second_digit
#print(new_digit)

# 2.3 Operations

#Addition                               2+3
#Subtraction                            2-3
#Multiplication                         2*3
#Division                               2/3     Always prints float
#Exponents                              2**3    2 to the power of 3 = 8
# Greater than                          2>3
# Less than                             2<3
# Greater than and equal to             2>=3
# Lesser than and equal to              2<=3
# Equal to                              2==3
# Not equal to                          2!=3
# Modulo (remainder after division)     7 % 2 gives 1


#Priority (when more than one operation in one line of code) explained below:
# PEMDAS
# Paranthesis
#Exponents
#Multiplication
#Division
#Addition
#Subtraction
# rounding numbers
# floored division // used when you want to chop off digits after the decimal, converting it to int. Example below
# number = (8//3)
# print(type(number))
# the below is a shortcut to manipulate a value based on previous value saved in a variable
# number/=2
# number-=2
# number+=2
# number*=2
#Note: 'Multiplication and Division' and 'Addition and Subtraction' are equally important. The calculation most to the left is prioritized

#Example below:
#number = 3*3+3/3-3
# Result will be 7.0

# 2.4 Data conversion

# Rounding numbers
# use round function. If precision for how many digits after decimal is needed for the code, add , and digit to round to
# numbers = round(8/3, 4)
# print(numbers)

#2.5 f-Strings
# f-Strings makes it easy to mix str and other datatypes without converting.
# Add the character f added in front of the "" or ''. This is now f-string. Use {} to add the variable name for f-string
# Does the converting behind the scene. Example below:
# score = 0
# height = 1.8
# iswinning = True
# print(f"Your score is {score}, your height is {height}, and you are winning is {iswinning}")
# Different datatypes got converted in a str in the same line of code

# Life in weeks: Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Longer version
# age = input("What is your current age?\n")
# average_age = 90
# days_in_a_year = 365
# weeks_in_a_year = 52
# months_in_a_year = 12
# years_left = average_age - int(age)
# days_left = years_left*days_in_a_year
# weeks_left = years_left*weeks_in_a_year
# months_left = years_left*months_in_a_year
# print(f"You have, {days_left} days, {weeks_left} weeks, {months_left} months left.")

# age = input("What is your current age?\n")
# comment - average age in this problem is 90 years and there are 365 days, 52 weeks and 12 months in a year
# comment - PAMDAS, type conversion and f-string tested here
# days_left = (90 - int(age))*365
# weeks_left = (90 - int(age))*52
# months_left = (90 - int(age))*12
# comment - you can do calculations within the curly brackets as seen below
# print(f"You have {90 - int(age)} years left i.e. {days_left} days, {weeks_left} weeks, {months_left} months left.")
# comment - save in variable for more readability
# life_left = f"You have {90 - int(age)} years left i.e. {days_left} days, {weeks_left} weeks, {months_left} months left."
# print(life_left)

# 2.6 end of day quiz

# Which of the following will give an error

# name = input("What is your name?\n")
# print(f"Hello, {name}")

# name = input("What is your name")
# print("Hello, " + name)

# age = 12
# print(f"You are {age} years old")

# The below code will give a TypeError because age is an int.
# age = 12
# print("You are " + age + "years old")
# Debugging above code:
# age = 12
# print(("You are ") + str(age) + (" years old"))

# 2.7 Final project of the day - Tip calculator. Check 100_daysof_projects.py for the problem and solution

#Day 3
# Conditional statements, Logical operators, Code blocks, scope

# 3.1 Conditional statements
# if
# else
# elif
# Important elements - condition in check, syntax and indentation
# Everything indented after the if, else and elif is their block of code. So what follows the colon and indentation, gets the instruction from the condition
# Comparative operations used often

# Odd or even number (use of % modulo)
# number = int(input("Which number do you want to check?\n"))
# if number % 2 == 0:
#     print("This is an even number")
# if number % 2 != 0:
#     print("This is an odd number")

# Nested if...else statement
# Once the 1st condition is passed, we can check another


# Multiple if statements in succession. example below
# print("Welcome to the roller coaster ride. Please answer a few quick questions")
# height = int(input("What is your height in cm?\n"))
# if height <= 120:
#     print("Sorry, you can't ride")
# else:
# age and photo have same indentation
# Variable 'bill' is created to add it inside the f-string and {}
    # age = int(input("How old are you?\n"))
    # if age <= 12:
    #     bill = 5
    #     print("Child ticket is $5")
    # elif age <= 18:
    #     bill = 7
    #     print("Youth ticket is $7")
    # else:
    #     bill = 12
    #     print("Adult ticket is $12")
    # photo = input("Do you want your photo taken for an additional $3? Y or N.\n")
    # if photo == "Y":
    #     bill_photo = 3
    #     print(f"Your total bill is ${bill_photo + bill}")
    # else:
    #     print(f"Your total bill is ${bill}")

# Pizza order code - multiple if statements


# print("Welcome to Python Pizza Deliveries. Let's start your order")
# size = input("What size pizza would you like? S, M or L\n")
# add_pepporoni = input("Do you want pepporoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")
# bill = 0
# if size == "S":
#     bill = bill + 15
# elif size == "M":
#     bill = bill + 20
# elif size == "L":
#     bill = bill + 25
#
# if add_pepporoni == "Y":
#     bill = current value of bill + 2
    # if size == "S":
    #     bill = bill + 2
    # elif size == "M":
    #     bill = bill + 3
    # elif size == "L":
    #     bill = bill + 3
#
# if extra_cheese == "Y":
#     bill = bill + 1
# print(f"Your total bill is ${bill}")

# 3.2 Combining conditions - logical operations

#Multiple conditions in the same line of code
# if condition1 & condition2 & condition3
#     do this
#else:
#   do this

#Logical operators:
# A and B
# They both have to be true for the entire line of code to be true


# C or D    C and D
# C and D: If one of them is false, the entire line evaluates as False. If both conditions are true, the entire line gets evaluated as true. use
# C or D: Only with C or D is false, the line because False

# not E
# Reverses the condition. If the condition is False than it becomes true, if the condition is True then it becomes False
# Example: a = 12
# not a > 15
# Returns back True

# Love calculator
# your_name = input("What is your name?\n")
# their_name = input("What is your partner's name?\n")
# combined_names = your_name + their_name
# lower_names = combined_names.lower()
#
# T = lower_names.count("t")
# R = lower_names.count("r")
# U = lower_names.count("u")
# E = lower_names.count("e")
# true_sum = T + R + U + E
# L = lower_names.count("l")
# O = lower_names.count("o")
# V = lower_names.count("v")
# E = lower_names.count("e")
# love_sum = L + O + V + E
#
# love_score = int(str(true_sum) + str(love_sum))
# if love_score <= 10 or love_score >= 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >=40 and love_score <= 50:
#     print(f"Your score is {love_score}, you are alright together")
# else:
#     print(f"Your score is {love_score}")
#
# Treasure Island
# input("Welcome to the Treasure Island. Your mission is to find the treasure.")
# direction = input("Where do you want to go?\n")
# if direction == "Right":
#     print("Game Over!")
# else:
#     choice = input("Do you want to swim or wait? Select Swim or Wait\n")
#     if choice == "Swim":
#         print("Game over!")
#     else:
#         door = input("Which door? Select Blue, Yellow, or Red\n")
#         if door == "Blue" or door == "Red":
#             print("Game Over!")
#         else:
#             print("You win!")
        # or
        # path of least resistance code bellow
        # if door == "Yellow":
        # print ("You win!")
        # else:
        # print ("Game over")
# Tip You can get python to ignore the symbol (that can be mistaken as code) within the code using \ so You\'re for You're
# making sure all cases are covered, all caps, uppercase, lower case.
# One way is converting the input to lower by using .lower



