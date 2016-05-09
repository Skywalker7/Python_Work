#Battle Rules
num_knights = 10
day = "Wednesday"

if num_knights < 3 or day == "Monday":
	print ("retreat")
elif num_knights >= 10 and day == "Wednesday":
	print ("Trojan Rabbit")
elif day == "Tuesday":
	print("Taco Night")
else:
	print ("Truce?")

