# Band name generator
# Use printing, commenting, \n, variables, str concatenation and input function

#Comment - Create a greeting for your user
# print("Welcome to the Band Name Generator")
# Comment - Ask their name and welcome them. Name in next line.
# print("Hello, " + input("What is your name?\n"))
#Ask the user for the city that they were born in. Answer in next line.
# city = input("What's the name of the city you were born in?\n")
# Ask the user their pet's name. Answer in next line
# pet = input("What's the name of your pet?\n")
# Combine the name of their city with the name of their pet
# print("Your band name could be " + city + " " + pet)

# Tip calculator
# Long version
# print("Welcome to the Tip Calculator")
# total_bill = input("What was the total bill?\n")
# percentage_split = input("What percentage tip would you like to give? 10, 15 or 20?\n")
# people_split = input("How many people to split the bill?\n")
# total_tip_per_person = float(total_bill) * int(percentage_split)/100/int(people_split)
# total_bill_per_person = float(total_bill)/int(people_split)+total_tip_per_person
# total_bill_per_person_rounded = round(total_bill_per_person,2)
# print(f"Each person should pay ${total_bill_per_person_rounded}")

# Cleaner, shorter version

# print("Welcome to the Tip Calculator!")
# bill = float(input("What is the total bill? \n$"))
# tip = int(input("How much tip would you like to give? 10, 15, 20? Please don't add a % sign before or after your tip\n"))
# people = int(input("How many people to split the bill?\n"))
# One line calculation but check below for further split
# bill_with_tip = tip/100 * bill + bill
# print(bill_with_tip)
# can split further like below:
# tip_as_percentage = tip/100
# total_tip_amount = bill*tip_as_percentage
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill/people
# Traditional rounding of the number below.
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")
# The above rounding doesn't work with something like 10.60 it will show only 10.6. This is a formatting error. Check fix below:
# final_amount = "{:.2f}".format(bill_per_person)
# print(final_amount)

# Leap year calculator - Tough challenge

# print("Welcome to the Leap year calculator")
# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

