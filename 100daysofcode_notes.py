#Types of functions

#a function is declared
#print
#input
#len
# round

#Types of errors


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
# a = input("a: ")
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

#Addition           2+3
#Subtraction        2-3
#Multiplication     2*3
#Division           2/3     Always prints float
#Exponents          2**3    2 to the power of 3 = 8

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

# BMI calculator - convert BMI as a whole number (rounded)
# name = input("What's your name?\n")
# print("Hello, " + name)
# weight = int(input("Please enter your weight in kg:\n"))
# height = float(input("Please enter your height in meters:\n"))
# BMI = weight/height*height
# BMI_whole = int(BMI)
# print("Your BMI is " + str(BMI_whole))

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
#



#1.1 datatype
    # strings
    # integers
    # booleans
    # float

# 1.1.1 string str
    #pulling out each character of a string individually is done by putting the index/position of
    # the character we want
    # print("Hello"[4])
    #This method is called subscripting.
    # Remember to add the index after "" to not include it as a string i.e. piece of text but extraction

#1.1.2 integer int
    #can use operators to calculate two numbers without using "" but in () to add integers or for
    # Python to know it is an integer
        # print(123)
        # print(123 + 5)
    #In python, commas between numbers can be replaced with _ so (100_000) instead of (100,000)
    #and it will be interpreted by the computer as 100000 so the computer will remove _and ignores it

#1.1.3 Float float
    # floating point number (3.14)

#1.1.4 Boolean bool
    # Two possible values True or False
    # Capital T and F are important

# 1.1.5 Datatype and their conversions
    # len() gives an error when passing a number i.e int instead of a str
    # type() checks for what's in the parenthesis and gives you the type data that it is
    # can save a converted datatype into a new variable. for instance
        #num_char = len(input("What is your name?"
        #new_num_char = str(num_char)
        #print("Your name has " + new_num_char + " character.")

#2.1 Mathematical operations
    # subtraction -
    # multiplication *
    # divide - / will always get a float
    # Addition +
    # exponents (raise a number to the power) **
    # When you have more than one operation on the same line of code, there is priority
        #Follow PAMDAS - parenthesis, exponents, multiplication, division, addition, subtraction
        #Multiplication and division are equally imp, addition and subtraction are equally imp.
        #The one to the left has first priority in the above case
    #Adding () nested in (), the inside() gets prioritized. Low priority calculations become highest & would happen first

#2.2 Number manipulation
#The round() function rounds the number into a whole number (.5 rule for result). can specify how many decimal points to include in the rounding by adding comma. eg
    #print(3+4.41, 2) will result in 7.41
    #for getting back int not float, use // (3.0 // 2) will give you 5. Datatype will be int. Its called Floor division

#If we had saved the result of this calculation in a variable, then one of the things you can do is,
#comtimue performing calculations on this variable
    #x = 4/2
    #x =/ 2
    #Result will be 1
#score = 0
#user scores a point
    #score += 1
#result - score = 1

#3 F-strings
    #Makes it easy to mix strings and various datatypes
#instead of converting multiple datatypes in a line of code and separating them with a +, f-String can be used
#f goes in front of '' or ""
    #score = 0
    #height = 1.8
    #iswinning = True

    #print(f"your score is {score}, your height is{height}, you are winning is{iswinning}")
#Result = your score is 0, your height is 1.8, you are winning is True. Here, all the datatypes got converted to str
#Remember to add spaces when required

#score = 0
#height = 1.8
#iswinning = True

#print(f"your score is {score}, your height is {height}, you are winning is {iswinning}")

#total_individual_bill =] "{:.2f}".format(individual_tip_amount + total_bill/num_of_people)
#above is formatting for decimal places, f string

#Day 3
# conditional statements
# logical operators
# code blocks
# scope

#Syntax

#1.1 Conditions
#if condition:
    #do this
#else:
    #do this
#Everything written after the :, it is a block of code

#1.2 Comparision operators

# >     Greater than
# <     Less than
# >=    Greater than or equal to
# <=    Less than or equal to
# ==    equal to
# !=    not equal to

# %     modulo - will divide a number by another and give the remainder of that division as the return value
#remember example: 7% 2 = 1 because it is 2 + 2 + 2 + 1 and 7% 3 = 1 because it is 3 + 3 + 1

#1.3 Nested if and elif statement

#In a nested if, if one condition is passed, we check for another condition and then we can have another if else inside the if condition
#The computer looks at the overall condition and starts evaluating the first if statement. Here, it wants to find out if it needs to read through the else block or
#go to the nested if - else condition

#1.4 if condition:
    #if another condition:
        #do this
    #else:
        #do this
    #else:
        #do this

#To go to the 2nd if, the 1st if already has to be true

#Can use multiple elif between the nested if...else

#1.5 elif condition:
    #if condition1:
        #do this
    #elif condition2:
        #do this
    #else:
        #do this

# in a if...elif...else condition, only 1 condition will be
# carried out but in nested if, all conditions will be carried out

#2.1 Logical operators
    #Check for multiple conditions in the same line of code
#Three of them are useful:
    #and operator
    #     A and B are true for the entire line of code to be True.
    #or operator
    # A or B are true then the overall code evaluates to be False. If only needed one of the conditions to be True
        #then use or operator. If A or B are true or if they are both true, the return will be True
        #Its only when both are False, this statement returns false
    #not operator
#     Reverses the condition
    #if the condition is False, then the return is True and vice versa
        #Ex: a = 12
        #not a > 15
        #return will be True
# \ between words will tell Python to ignore the ' in words like You're and treat it as text. So "You\'re"
# ('abc. "kc". ij') is going to be interpreted as one string because of the single quotes
#     the double quote words is for the users attention

#Day 4
# Randomisation and lists

#4.1 Randomisation

# Imp when we want to create computer programs that have a degree of unpredictibility
# Mersenne Tester
#import random
#random_integer = random.randint(1, 10)
#print(random_integer)
#The code above will print random integers between 1 and 10, including 1 and 10 (this is a range)

#What is a module
    #split the code up into individual modules where each module represents a different set of program
#Can create multiple new files and import those files in main.py
#example:
    #create a file my_module.py
    #now add pi = 3.1415
    #now import the my_module.py in the main.py
    #and print my_module.pi
    #Return value will be 3.1415

#random_float = random.random()
#print(random_float)
#Will always generate a number between 0 and 1 (excluding 1) and has many decimal places.
#Random floating number between 0 and 5
    # * by 5
    # import random
    # random_float = random.random()
    #print (random_float)

    #random_float * 5
    #to expand the range from 0 to 1, all the way to 0 to 5 but not including 5

#For example, in the love score example,
#love_score = random.randint(1, 100)
#print(f"Your love score is {love_score}")

#random can be used in a game of dice, flipping a coin etc

#4.2.1 Lists
# It is a data structure - way of organizing
#[" "] items separated by comma
# order of the item is represented by index [0]
#you can also right negative number, [-1] shows last item of the list
# can alter item in the list using the following syntax
#     var[index] = "new value"
# can add to the list using the following syntax
#    var.append("new addition") this will be added at the end of the list

#4.2.2 Index errors and working with nested lists
# Index out of range
# by (var - 1), the last number of the index in the list becomes one less. i.e in a 50 states list, the last state takes the index number 49 and first takes 0

# to have multiple lists in one list, follow the following code

#Nested lists example code

#vegetables = ["Spinach", "Kale", "Tomatoes","Celery", "Potatoes"]
#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#dirty_dozen = [vegetables, fruits]
#print(dirty_dozen)
#return value = [['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes'], ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']]


# Index errors
# nested lists
# Appending
# Offset


# 5.1 Loops
# Loops, Range and code blocks

#for loop
#Everytime a loop runs, it is = to something. For instance, in the following code, fruits = peach, fruits = apple etc
#for loop
#fruits = ["peach", "apple", "banana"]
#for fruit in fruits:
    #print(fruit)
    #print(fruits)
#Notice how print(fruit) is different from print(fruits). Also how, loop goes through one item at a time.
#will assign the variable fruit to each item individually. Executing the print statement three times
#can execute multiple things indended in the loop. For ex,

#fruits = ["Peach", "Apple", "Banana"]
#for fruit in fruits:
    #print(fruit)
    #print(fruit + " Pie")
#return will be Peach Pie, Apple Pie, Banana Pie

#Inside the for loop
    #whenever you see a : if it is intended, it is inside the loop
    #if print(fruits) inside the loop, then it is going to run as many times as the number of items inside the variable. In the above case, thrice
#outside the for loop
    #if print(fruits) is not associated to the indentation, it is going to print the list only once and after the for loop is over


#How the loop functions
#     when you say for something in something:
#     the for loop will run through each item individually
#         so, for something(0), for something(1) etc
# Example
#     numbers = [1, 2, 3, 4]
#     for n in numbers:
#       the for loop will run through 1, then 2, then 3, then 4

#     Adding items in the loop without using the sum() function
#     want to replicate for 1 + 2 + 3 + 4
#     but because you don't know how many numbers (items) in the list, you need to add it with 0 and assign the list to a variable
#      so it will be
#       x = 0
#       for n in numbers:
#             x = x + n
#       print(x)
# So the way this functions is, x = 0 + 1, then 1 + 2 (since x will now be 1 - given that loop runs one at a time), then 3 + 3 and then 6 + 4. return value 10

#5.2  for loops and the range() function
# The range function is very usueful if you want to generate a range of numbers to loop through
# The syntax
    #for number in range(a, b):
    #print(number)
#creating a range between a and b and getting hold of each number inside that range to do something with that number and not including b
#By default, the range function will step through all the numbers from the start to the end and will increase by 1
#steps size = To increase by any other number compared to the default add comma to the end of it and specify how large you want the step to be
#range(start, stop[,step])
    #for number in range(1, 11, 3):
    #print(number)
#Will return: 1 4 7 10
#
#
#Day 6
    #Code blocks
#     Indentations
# While loops
# Functions
#   Anything inside the "" is a function
# Making our own function
    # start by defining the function using the keyword def
#     then execute the function, unless the function is executed, the defined function doesn't work
#   call the function by writing the name of the function
# Example:
#     def my_function():
#      print("Hello World")
#       print("Bye")
# my_function()
# Call the function by writing the name followed by ()
# Functions allows us to use all the instructions at one time. Single instruction for multiple outcomes in one function
# Goal - reduce the number of line and make it more readable


