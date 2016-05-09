#list & dictionary sample exercise -- looping through dictionaries

favorite_languages = {
	"jen": "python",
	 "sarah": "c",
	 "edward": "ruby",
	 "phil": "python",
}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print("Hi " + name.title() +
		", I see your favorite language is " +
		favorite_languages[name].title() + "!")

#Glossary 2

#using glossary from 6.2 to create a loop that runs through it
#the words key and value are place holders I can switch for other words
glossary = {
	"pep_8": "a python syle guide",
	"tuple": "a list in python that contains immutable values; it uses '()' to store its values in.",
	"len": "is a function that helps you find the length of an item.",
	"range": "is a function that prints a series of numbers up to the number you posted.",
	"sort": "is a function that permanently sorts a list into alphabetical order.",
	"sorted": "is a function temporarily sorts a list into alphabetical order.",
	"python": "is a programming language named for Monty Python.",
	"boolean expression": "another name for conditional test",
	"boolean value": "is either true or false", 
	"list": "a collection of items that can be modified",
}

for name, definition in glossary.items():
	print(name.title() + " " + definition)

#to print it in alphabetical order I can place my dictionary within sorted() for a temporary alphabetical sorting

for name, definition in sorted(glossary.items()):
	print(name.title() + " " + definition)

#Rivers

rivers = {
	"Nile": "Egypt.",
	"Ganges": "India.",
	"Mississippi": "the United States.",
}

for river, country in rivers.items():
	print("The" + " " + river + " " + "runs through" + " " + country)

for river in rivers.keys():
	print("The river" + " " + river + " " + "runs through its entire country.")

for country in rivers.values():
	print(country)

#favorite languages poll

favorite_languages = {
	"jen": "python",
	 "sarah": "c",
	 "edward": "ruby",
	 "phil": "python",
}

people_who_need_to_poll = ["richard", "sarah", "jen", "tom"]

for name in favorite_languages.keys():
	print(name.title())

	if name in people_who_need_to_poll:
		print("Hey" + " " + name.title() + " " + "would you please take this poll?")
