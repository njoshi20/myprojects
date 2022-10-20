# 1. Input exercise
# print the length of prompt
# print(len(input("What's your name?\n")))

# 2. Variables exercise
# Switch the values of the two variables around
# a = input("a: ")
# b = input("b: ")
# c = a
# a = b
# b = c
# print(a)
# print(b)

# 3. Band name generator program. Help a band to come up with a name for their brand by the band answering a few questions. Further instructions below
# Create a greeting for the program
# Ask the user for the city they grew up in
# Ask the user for the name of the pet
# Combine the name of their city and pet and show their band name
# make sure the input cursor shows on a new line

# print("Welcome to the Band Name Generator")
# print("Hello, " + input("What is your name?\n"))
# x = input("What city were you born in?\n")
# y = input("What is your pet's name?\n")
# print("The name of your band could be " + x + " " + y)

# 4. Datatype conversion

# num_char = len(input("What is your name?\n"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# 5. Total bill + tip calculator
# result needs to be two decimal values long

# print("Welcome to the tip calculator")
# total_bill = float(input("What was the total bill? \n$"))
# num_of_people = int(input("How many people to split the bill? \n"))
# group_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? \n"))
# individual_tip_amount = (group_tip*total_bill)/100/num_of_people
# print(individual_tip_amount)
# total_individual_bill = round(individual_tip_amount + total_bill/num_of_people, 2)
# total_individual_bill = "{:.2f}".format(individual_tip_amount + total_bill/num_of_people)
# print(f"Each person should pay ${total_individual_bill}")

# 6.Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# two_digit_number = first_digit + second_digit
# print(two_digit_number)

# 7. BMI Calculator

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = int(float(weight)/float(height)**2)
# print(bmi)

# print(round(3+4.41, 2))

# 8. How many days, weeks, months are you left with if you were to servive 90 years in total.
# age = input("What is your current age?")
# days = 90*365 - int(age)*365
# weeks = 90*52 - int(age)*52
# months = 90*12 - int(age)*12
# print(f"you have {days} days, {weeks} weeks, and {months} months left")

# 8.1Another way, longer way of solving the above problem
# age = input("What is your current age?")
# age_as_in = int(age)
# years_remaining = 90 - age_as_in
# days_remaining = years_remaining*365
# weeks_remaining = years_remaining*52
# months_remaining = years_remaining*12
# message = (f"you have {days} days, {weeks} weeks, and {months} months left")
# print(message)

# 9.Conditional statements exercise
# Ticketing task
# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm?\n"))
# if height >= 120:
# print("You can ride the rollercoster!")
# age = int(input("What is your age?\n"))
# if age < 12:
# print("You need to pay $5.")
# elif age <= 18:
# print("You need to pay $7.")
# else:
# print("Please pay $12.")
# else:
# print("Sorry, you can't ride the rollercoster")

# 9.1 BMI calculator (age range) using conditional

# print("Welcome to the BMI calculator")
# weight = float(input("What is your weight in kg?\n"))
# height = float(input("What is your height in meter?\n"))
# BMI = round(weight/(height**2))
# if BMI <18.5:
# print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI <25:
# print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI <30:
# print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI <35:
# print(f"Your BMI is {BMI}, you are obese.")
# else:
# print(f"Your BMI is {BMI}, you are clinically obese.")

# 9.2.1 Nested if
# Leap year challenge
# Write a program that works out wheather if a given year is a leap year.
# on every year that is evenly divisible by 4
# except every year is evenly divisible by 100
# unless the year is also evenly divisible by 400
# year = int(input("What year do you want to check?\n"))
# if year % 4 == 0:
# if year % 100 == 0:
# if year % 400 != 0:
# print("Not a leap year")
# else:
# print("Leap year")
# else:
# print("Leap year")
# else:
# print("Not a leap year")

# 9.2.2
# Ticketing task
# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm?\n"))
# bill = 0
# if height >= 120:
# age = int(input("What is your age?\n"))
# if age <= 12:
# bill = 5
# print("child ticket is $5")
# elif age <=18:
# bill = 8
# print("youth ticket is $8")
# else:
# bill = 12
# print("adult ticket is $12")
# photo = input("Do you want a photo taken for an additional $3? Y or N.\n")
# if photo == "Y":
# bill += 3
# print(f"you pay ${bill}")
# else:
# print("sorry, you are short to ride the rollercoster!")

# 9.3.1 Pizza order exercise
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")
# bill = 0
# if size == "S":
# if add_pepperoni == "Y":
# bill += 15 + 2
# else:
# bill += 15
# elif size == "M":
# if add_pepperoni == "Y":
# bill += 20 + 3
# else:
# bill += 20
# elif size == "L":
# if add_pepperoni == "Y":
# bill += 25 + 3
# else:
# bill += 25
# if extra_cheese == "Y":
# bill += 1
# print(f"Your final bill is: ${bill}.")

# 9.3.2 Pizza order exercise - Alternative solution
# to avoid duplication and confusion/mistake in code and input
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")
# bill = 0
# if size == "S":
# bill +=15
# elif size == "M":
# bill += 20
# elif size == "L":
# bill += 25
# if add_pepperoni == "Y":
# if size == "S":
# bill += 2
# else:
# bill += 3
# if extra_cheese == "Y":
# bill += 1
# print(f"Your final bill is: ${bill}.")

# 9.2.3 Ticketing task using logical calculator
# fix the code below
# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm?\n"))
# bill = 0
# if height >= 120:
# age = int(input("What is your age?\n"))
# if age <= 12:
# bill = 5
# print("child ticket is $5")
# elif age <=18:
# bill = 8
# print("youth ticket is $8")
# and statement
# elif age >= 45 and age <=55:
# bill = 0
# print("You ride free")
# else:
# print("adult ticket is $12")
# photo = input("Do you want a photo taken for an additional $3? Y or N.\n")
# if photo == "Y":
# bill += 3
# print(f"you pay ${bill}")
# else:
# print("sorry, you are short to ride the rollercoster!")

# 9.4 Love calculator using logical operators
# Test compatibility score between two people

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# combined_name = name1 + name2
# lower_case_combined_name = combined_name.lower()
# t = lower_case_combined_name.count("t")
# r = lower_case_combined_name.count("r")
# u = lower_case_combined_name.count("u")
# e = lower_case_combined_name.count("e")
# true_word_count = (t + r + u + e)
# l = lower_case_combined_name.count("l")
# o = lower_case_combined_name.count("o")
# v = lower_case_combined_name.count("v")
# e = lower_case_combined_name.count("e")
# love_word_count = (l + o + v + e)
# love_score = int(str(true_word_count) + str(love_word_count))
# if love_score <=10 or love_score >= 90:
# print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >=40 and love_score <=50:
# print(f"Your score is {love_score}, you are alright together.")
# else:
# print(f"Your score is {love_score}")

# 9.5 Treasure island game
# print("Welcome to the Treasure Island!")
# print("Your mission is to find the treasure")
# first_hint = input("Where do you want to go? Left or Right\n")
# if first_hint == "Left":
# second_hint = input("Do you want to swim or wait\n")
# if second_hint == "Wait":
# third_hint = input("Which door do you want to select?\n")
# if third_hint == "Blue":
# print("Eaten by beasts. Game over!")
# elif third_hint == "Red":
# print("Burned by fire. Game over!")
# else:
# print("You win!")
# else:
# print("Attacked by trout. Game over!")
# else:
# print("Fall into a hole. Game over!")

# 10.1 Coin toss program using randomisation
# plus testing
# import random
# random.seed(3)
# print(random.random())

# Heads = 1
# Tails = 0
# Both = 2
# Another = 3
# a = [Heads, Tails]
# a = [Heads, Tails, Both, Another]
# print(a)
# print(random.choice(a))

# 10.2.1 Banker Roulette
# import random

# names_diners = input("Welcome to who will pay today? Insert names of all the diners separated by comma!\n")
# names_list = names_diners.split(",")
# print(names_list)
# length_names = len(names_list)
# print(length_names)
# person_to_pay = names_list[random.randint(0, length_names - 1)]
# print(f"{person_to_pay} is going to pay today's bill. Enjoy!")

# Logic
# fruits = ["Apple", "Sid", "Neha"]
# fruit = fruits[1]
# print(fruit)

# Remember, pears will get replaced by melons in the below code

# Given the code below:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
# What do you think will be printed?

# vegetables = ["Spinach", "Kale", "Tomatoes","Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# dirty_dozen = [vegetables, fruits]
# print(dirty_dozen)

# Return = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

# the print [1] in print (dirty_dozen [1], [2]) is the 2nd list 'fruits' and [2] is the item in that list with that index i.e Apples

# 11 Treasure map

# Redo the following
# row1 = ["A", "B", "C"]
# row2 = ["D", "E", "F"]
# row3 = ["G", "H", "I"]
# map = (f"{row1}\n{row2}\n{row3}")
# print(map)
# col1 = [row1[0] + " " + row2[0] + " " + row3[0]]
# col2 = [row1[1] + " " + row2[1] + " " + row3[1]]
# col3 = [row3[2] + " " + row2[2] + " " + row3[2]]
# split_col1 = col1.split(" ")
# print(split_col1)


# Lists
# index to change the item in the list
# nested list

# for loop
# fruits = ["peach", "apple", "banana"]
# for fruit in fruits:
# print(fruit)
# print(fruits)
# Notice how print(fruit) is different from print(fruits). Also how, loop goes through one item at a time.
# will assign the variable fruit to each item individually. Executing the print statement three times
# can execute multiple things indended in the loop. For ex,

#fruits = ["Peach", "Apple", "Banana"]
#for fruit in fruits:
 #   print(fruit)
# print(fruit + " Pie")
# return will be Peach Pie, Apple Pie, Banana Pie

#12 rock paper scissors game
#rock = 0
#paper = 1
#scissors = 2
#game_images = [rock, paper, scissors]
#your_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors\n"))
#if your_choice > 3 or your_choice < 0:
 #   print("Its an invalid number. Select between 0 and 2")
#else:
 #   print(game_images[your_choice])
  #  import random
    #computer_choice = random.randint(0, 2)
   # print("Computer chose:")
    #print(game_images[computer_choice])

#rock = 0
#paper = 1
#sci = 2
#rock wins against sci (0 against 2)
#sci wins against paper (2 against 1)
#paper wins against rock (1 against 0)

    #if your_choice == 0 and computer_choice == 2:
     #   print("You win!")
 #   elif your_choice == 2 and computer_choice == 0:
  #      print("You lose!")
   # elif your_choice > computer_choice:
    #    print("You win!")
  #  elif computer_choice > your_choice:
   #     print("You lose!")
  #  elif your_choice == computer_choice:
   #     print("Its a draw!")

#game images not working

#13 Average height exercise

#Indentation - inside and outside the loop
#Going through an item one at a time
#assigning the value of a loop to each item
#repetation as many as the indices in the list
#sum and len function without using it
#if...else statement
#for loop
#sum everyone's height, divide by total to find average and convert to whole number round function

student_height = input("Please enter the height in cm for all students individually separated by a comma\n").split( )
#student_height = ["2", "4", "1", "6"]
total_height = 0
for height in student_height:
    total_height += height
print(total_height)



#fruits = ["Peach", "Apple", "Banana"]
#for fruit in fruits:
 #   print(fruit)


# print(fruit + " Pie")
# return will be Peach Pie, Apple Pie, Banana Pie
