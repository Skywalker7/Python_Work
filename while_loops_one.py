#topping_looping -- takes toppings and adds them to your pizza exercise 7.1
#enter quit to exit topping adder
#problem first choice doesn't get excuted into message, but the choices afterwards do
#also the first choice lingers underneath the next choice's sentence

prompt = input("\nWhat would you like on your pizza? ")
prompt += "\nEnter 'quit' when you are done adding your toppings."

while True:
	city = input(prompt)

	if city == 'quit'
		break
	else:
		print("I'd love to go to " + city.title() + "!")

