#using active variable to stop loop

prompt = ("\nWhat would you like on your pizza? ")
prompt += "\n(Enter 'quit' when you are done adding your toppings.)"

active = True
while active:
	topping = input(prompt)

	if topping == 'quit':
		active = False	
	else:	
		print("Okay, adding " + topping + "!")

#using break to stop a loop

prompt = ("\nWhat would you like on your pizza? ")
prompt += "\n(Enter 'quit' when you are done adding your toppings.)"


while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print("Okay, adding " + topping + "!")

#using conditional to stop a loop

prompt = ("\nWhat would you like on your pizza? ")
prompt += "\n(Enter 'quit' when you are done adding your toppings.)"


while topping != 'quit':
	topping = input(prompt)
	
	print("Okay, adding " + topping + "!")