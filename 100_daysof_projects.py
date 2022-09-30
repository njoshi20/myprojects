#1. Input exercise
# print the length of prompt
#print(len(input("What's your name?\n")))

#2. Variables exercise
#Switch the values of the two variables around
#a = input("a: ")
#b = input("b: ")
#c = a
#a = b
#b = c
#print(a)
#print(b)

#3. Band name generator program. Help a band to come up with a name for their brand by the band answering a few questions. Further instructions below
#Create a greeting for the program
#Ask the user for the city they grew up in
# Ask the user for the name of the pet
#Combine the name of their city and pet and show their band name
#make sure the input cursor shows on a new line

#print("Welcome to the Band Name Generator")
#print("Hello, " + input("What is your name?\n"))
#x = input("What city were you born in?\n")
#y = input("What is your pet's name?\n")
#print("The name of your band could be " + x + " " + y)

#4. Datatype conversion

#num_char = len(input("What is your name?\n"))
#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")

#5. Tip calculator
#result needs to be two decimal values long

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\n"))
num_of_people = int(input("How many people to split the bill?\n"))
tip_percentage_given = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
bill_split_per_person = (total_bill/num_of_people)
#print(bill_split_per_person)
percentage_split_per_person= bill_split_per_person/100*bill_split_per_person
#print(percentage_split_per_person)
total_bill_split_after_tip = bill_split_per_person + percentage_split_per_person
final_amount = round(total_bill_split_after_tip, 2)
print(f"Each person should pay ${final_amount} for the food")





#print("Each person should pay: " + str(x/y)/(z/100)+x/y)))

#5.Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
#first_digit = int(two_digit_number[0])
#second_digit = int(two_digit_number[1])
#two_digit_number = first_digit + second_digit
#print(two_digit_number)

#BMI Calculator

#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
#bmi = int(float(weight)/float(height)**2)
#print(bmi)

#print(round(3+4.41, 2))

#How many days, weeks, months are you left with if you were to servive 90 years in total.
age = input("What is your current age?")
days = 90*365 - int(age)*365
weeks = 90*52 - int(age)*52
months = 90*12 - int(age)*12
print(f"you have {days} days, {weeks} weeks, and {months} months left")

#Another way, longer way of solving the above problem
age = input("What is your current age?")
age_as_in = int(age)
years_remaining = 90 - age_as_in
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
months_remaining = years_remaining*12
message = (f"you have {days} days, {weeks} weeks, and {months} months left")
print(message)
