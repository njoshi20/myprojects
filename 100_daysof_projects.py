#1. Input exercise
print the length of prompt
print(len(input("What's your name?")))

#2. Variables exercise
#Switch the values of the two variables around
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print(a)
print(b)

#3. Band name generator program. Help a band to come up with a name for their brand by the band answering a few questions. Further instructions below
#Create a greeting for the program
#Ask the user for the city they grew up in
# Ask the user for the name of the pet
#Combine the name of their city and pet and show their band name
#make sure the input cursor shows on a new line

print("Welcome to the Band Name Generator")
print("Hello, " + input("What is your name?\n"))
x = input("What city were you born in?\n")
y = input("What is your pet's name?\n")
print("The name of your band could be " + x + " " + y)

#4. Tip calculator

print("Welcome to the tip calculator")
x = float(input("What was the total bill?\n"))
y = float(input("How many people to split the bill?\n"))
z = float(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
print("Each person should pay: " + str(x/y/z+x/y))











