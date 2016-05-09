#movie tickets exercise 7.5

age = input("Tell me your age so you can get a ticket! ")
age = int(age)

if age == 3:
	print ("Your ticket is free!")
elif age <= 12:
	print("Your ticket is $10.")
else:
	print("Your ticket is $15")
