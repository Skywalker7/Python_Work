#ask the user to input the day of the week
day = input("Enter the day of the week")
	print("You entered:", day)
#input used for python3 raw_input[] used for python2
num_knights = int(input("Enter the number of knights"))
	print ("You entered:", num_knights)
enemy = input("Enter type of enemy")

if enemy == "killer bunny":
	print("Holy Hand Grenade!")
else:
     # Orignal Battle Rules
	if num_knights < 3 or day == "Monday":
		print("Retreat!") 
	elif num_knights >= 10 and day == "Wednesday":
		print ("Trojan Rabbit")
	elif day == "Tuesday":
		print("Taco Night")
	else:
		print ("Truce?")