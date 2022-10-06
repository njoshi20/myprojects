#Day 1

#print function elements - () "" ''
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
#Debugging
    #Look for identation and syntax error
    #Also look for error (syntax) where python thinks what's inside the double quotes is a string and + is just concatenation.
        #Ex, buggy code: print("String Concatenation is done with the "+" sign.")
        #Here, Python takes "String...the" as one string + as a code and " sign." as another string
        #Two ways to fix this:
            #print('String Concatenation is done with the "+" sign.')
            #print("String Concatenation is done with the ""+"" sign.")
        #The first is less confusing
#input()
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

#Variables
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

#datatype
    # strings
    # integers
    # booleans
    # float

# string str
    #pulling out each character of a string individually is done by putting the index/position of
    # the character we want
    # print("Hello"[4])
    #This method is called subscripting.
    # Remember to add the index after "" to not include it as a string i.e. piece of text but extraction

#integer int
    #can use operators to calculate two numbers without using "" but in () to add integers or for
    # Python to know it is an integer
        # print(123)
        # print(123 + 5)
    #In python, commas between numbers can be replaced with _ so (100_000) instead of (100,000)
    #and it will be interpreted by the computer as 100000 so the computer will remove _and ignores it

#Float float
    # floating point number (3.14)

#Boolean bool
    # Two possible values True or False
    # Capital T and F are important

# Datatype and their conversions
    # len() gives an error when passing a number i.e int instead of a str
    # type() checks for what's in the parenthesis and gives you the type data that it is
    # can save a converted datatype into a new variable. for instance
        #num_char = len(input("What is your name?"
        #new_num_char = str(num_char)
        #print("Your name has " + new_num_char + " character.")

#Mathematical operations
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

#Number manipulation
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

#F-strings
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

#if condition:
    #do this
#else:
    #do this
#Everything written after the :, it is a block of code

#Comparision operators

# >     Greater than
# <     Less than
# >=    Greater than or equal to
# <=    Less than or equal to
# ==    equal to
# !=    not equal to

# %     modulo - will divide a number by another and give the remainder of that division as the return value
#remember example: 7% 2 = 1 because it is 2 + 2 + 2 + 1 and 7% 3 = 1 because it is 3 + 3 + 1

#Nested if and elif statement

#In a nested if, if one condition is passed, we check for another condition and then we can have another if else inside the if condition
#The computer looks at the overall condition and starts evaluating the first if statement. Here, it wants to find out if it needs to read through the else block or
#go to the nested if - else condition

#if condition:
    #if another condition:
        #do this
    #else:
        #do this
    #else:
        #do this

#To go to the 2nd if, the 1st if already has to be true
#Example code:

#Can use multiple elif between the nested if...else

#elif condition:
    #if condition1:
        #do this
    #elif condition2:
        #do this
    #else:
        #do this

# in a if...elif...else condition, only 1 condition will be
# carried out but in nested if, all conditions will be carried out

# Logical operators
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
