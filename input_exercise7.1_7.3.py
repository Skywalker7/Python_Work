# exercise 7.1 Rental Car - Write a program that asks what kind of rental car some one would like.

car = input("What type of car would you like? ")
print("Let me see if I can find a" + " " + car + " " + "for you.")


# exercise 7.2 Restaurant Seating - Write a program that asks for the number of a dinner party

dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
	print("Thanks for letting me know. Please expect your waiting time for seating to be ten to fifteen minutes.")
else:
	print("Your table is ready.")


# exercise 7.3 Multiples of ten

prompt = "Enter a number and I will tell you if it is a multiple of ten."
prompt += "\nWhat's your number? "

#prompt will now be a statement that requires an input
prompt = input(prompt)

#the input of prompt will be saved as a integer in the variable number
number = int(prompt)

if number % 10 == 0:
	print("Yay, your number is a multiple.")
else:
	print("This number is not a multiple.")