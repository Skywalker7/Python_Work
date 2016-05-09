#dictionaries within dictionaries exercise 6.7

people = {

"user_uno": {
	"first_name": "margo",
	"last_name": "francis",
	"city": "ohio",

},

"user_dos": {
	"first_name": "vinnie",
	"last_name": "tomas",
	"city": "detroit",
},

"user_tres": {
	"first_name": "terry",
	"last_name": "rose",
	"city": "new york",
},

}

for username, user_info in people.items():
	print("\nUsername:" + " " + username)
	full_name = user_info["first_name"] + " " + user_info["last_name"]
	location = user_info["city"]

	print("\tFull name:" + " " + full_name.title())
	print("\tLocation:" + " " + location.title())

#dictionaries 6.8

pets = {
	"wallace": {
		"owner": "sally",
	},
	"george": {
		"owner": "nemo",
	},
	"tomas": {
		"owner": "randall"
	},
}

# looping through keys for names of pets

for pet in pets.keys():
	print("\nPet name:" + " " + pet.title())

# looping through keys and values

for pet, pet_owner in pets.items():
	print("\nThis pet's name is:" + " " + pet.title())
	owner = pet_owner["owner"]
	print("Its owner's name is:" + " " + owner.title())

# favorite places 6.9

favorite_places = {
	"patricia": {
		"city": "hawaii",
	},
	
	"bettie": {
		"city": "paris",
	},

	"victoria": {
		"city": "san juan",
	},

}

for friend, favorite_city in favorite_places.items():
	print("\n" + friend.title() + " " + "loves:")
	city = favorite_city["city"]
	print(city.title())

# favorite numbers 6.10
#lists in dictionaries
favorite_numbers = {
	"jamie": {
		"numbers": [12, 14],
	},
	"rachel": {
		"numbers": [42, 2],
	},
	"tomas": {
		"numbers": [7, 24],
	},
}

for name, fav_numbers in favorite_numbers.items():
	print("My friend" + " " + name.title() + "'s" + " " + "favorite numbers are:")
	the_numbers = fav_numbers["numbers"]
	print(the_numbers)

# cities 6.11

cities = {
	"paris": {
		"popular_food": "bagettes",
		"country": "france",
		"population": "over one million",
	},
	"new_york": {
		"popular_food": "bagels",
		"country": "united states of america",
		"population": "over one million",
	},
	"buffalo": {
		"popular_food": "buffalo chicken",
		"country": "united states of america",
		"population": "over three thousand",
		}
}

for city, facts in cities.items():
	print ("\nThe city of" + " " + city.title() + " " + "is known for the following:")
	fact1 = facts["popular_food"]
	fact2 = facts["country"]
	fact3 = facts["population"]
	print(fact1.title() + "," + " " + "being a part of" + " " + fact2.title() + "," + " " + "and" + " " + "a population of" + " " + fact3 + "." )

#Extensions

cities = {
	"paris": {
		"popular_food": "bagettes",
		"country": "france",
		"population": "over one million",
	},
	"new_york": {
		"popular_food": "bagels",
		"country": "united states of america",
		"population": "over one million",
	},
	"buffalo": {
		"popular_food": "buffalo chicken",
		"country": "united states of america",
		"population": "over three thousand",
		}
}

for city, facts in cities.items():
	print ("\nThe city of" + " " + city.title() + " " + "is known for the following:")
	fact1 = facts["popular_food"]
	fact2 = facts["country"]
	fact3 = facts["population"]
	if "united states of america" in fact2:
 		print ((fact1.title() + "," + " " + "being a part of the" + " " + fact2.title() + "," + " " + "and" + " " + "a population of" + " " + fact3 + "." ))
	else: 
		print(fact1.title() + "," + " " + "being a part of" + " " + fact2.title() + "," + " " + "and" + " " + "a population of" + " " + fact3 + "." )

	