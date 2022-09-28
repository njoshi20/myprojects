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

    