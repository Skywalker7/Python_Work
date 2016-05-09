#python crash course dictionary practice

#shield_agent dictionary
shield_agent = {
	"first_name": "daisy",
	"last_name": "johnson",
	"age": 27,
	"city": "unknown",
}

print(shield_agent["first_name"].title())
print(shield_agent["last_name"].title())
print(shield_agent["age"])
print(shield_agent["city"])


#favorite_numbers dictionary
favorite_numbers = {
	"michael": 42,
	"jen": 14,
	"rachel": 72,
	"francis": 9,
}

print([favorite_numbers])

#python programming_words dictionary

glossary = {
	"pep_8": "python syle guide",
	"tuple": "a list in python that contains immutable values; it uses '()' to store its values in.",
	"len": "is a function that helps you find the length of an item.",
	"range": "is a function that prints a series of numbers up to the number you posted.",
	"sort": "is a function that permanently sorts a list into alphabetical order.",
}

print("Pep 8" + " "+ "is a" + " " + glossary["pep_8"])
print("\nA tuple" + " " + "is" + " " + glossary["tuple"])
print("\nLen" + " " + glossary["len"])
print("\nRange" + " " + glossary["range"])
print("\nSort" + " " + glossary["sort"])

