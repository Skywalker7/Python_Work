#tuples cannot be modifed like lists but they can be rewritten
#tuples are good for data that you don't want to change throughout the program
buffets = ("steak", "fish", "chicken", "pork")
for buffet in buffets:
	print(buffet)

#tuple' object does not support item assignment so the following code does not work
#buffets[1] = "avocado"

#menu change

buffets = ("veal", "turkey", "fish", "pork")
for buffet in buffets:
	print(buffet)

	