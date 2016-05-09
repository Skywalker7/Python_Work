#pizza_topping

#topping_looping -- takes toppings and adds them to your pizza exercise 7.1
#enter quit to exit topping adder


prompt = ("\nWhat would you like on your pizza? ")
prompt += "\n(Enter 'quit' when you are done adding your toppings.)"


while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print("Okay, adding " + topping + "!")