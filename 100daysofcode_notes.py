#Day 1

#1.1 print function elements - () "" ''
    #"" or '' is identical
    #print("print("what to print")") - double quotes "" two times gives a syntax error.
    #Solution - use one "" and one '' print("print('what to print')") or print('print("what to print")')
    #\n = new line can be return in between codes on the same line that need to be separated
        #print("Hello world!\nHello world!\nHello world!")
    #you can also concatenate using + print("Hello" + " Neha") or print ("Hello" + " " + "Neha")
    #Indentation error = always start at the beginning of the line
    #Syntax errors
    #Python gives out only one traceback at a time. Once you fix that, it moves to the next. Instead, opt for code
    #intellegence will hint before you run
#1.2 Debugging
    #Look for identation and syntax error
    #Also look for error (syntax) where python thinks what's inside the double quotes is a string and + is just concatenation.
        #Ex, buggy code: print("String Concatenation is done with the "+" sign.")
        #Here, Python takes "String...the" as one string + as a code and " sign." as another string
        #Two ways to fix this:
            #print('String Concatenation is done with the "+" sign.')
            #print("String Concatenation is done with the ""+"" sign.")
        #The first is less confusing
#1.3 input()
    #used as a prompt for the user to input something related to the prompt in the ()
        #Ex: input("What is your name?")
    #The program gets paused and will only continue if the user answers the prompt
    #Its only when the user gives the input, the program ends
    #input("A prompt for the user")
    #When the user enters a reply to the prompt as a part of the input, then the part of the code in main
    #that says input("A prompt for the user/something else") gets replaced by the reply of the prompt
    #print and input statement can be used together like:
        #print("Hello" + " "+ input("What is your name?"))
        #Will return Hello Neha
#instead of adding a # all the time for comments, you can also press command and forward slash on Mac
# undo, command z for mac

#1.4 Variables
#Can be changed/varied
#Can refer it later
#Referring the piece of data by a variable name. Different piece of data is possible
#rules on naming the variables
    #Make the code readable
    #clear name like user_name
    #multiple names
    #can't have spaces in between words. _ to separate codes
    #numbers cannot be in the beginning of the variable name
    #Certain previledge words, do not use them as name
    #make sure all the names of the variable gets highlighted in the same color
    #name error if the name of the variable and the typed name not matched

#Day 2
# datatype, numbers, operations, Type conversions, f-strings

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
#Example code:

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





