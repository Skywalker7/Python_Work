#checking for true 
car = 'honda'
print ("She bought a car == 'honda' I predict True.")
print(car=='honda')


#converted user_name to lower case the statement evaluated as 'true'
user_name = 'Holly'
print (user_name.lower() == 'holly')

#case matters this statement equals false because the user_name variable is saved with an upper case 'H'
print(user_name == 'holly')

min_age = 13
legal_age = 21

#checking if legal_age is equal to min_age & it's not 
print(min_age == legal_age)

#min_age is less than legal_age so this complete statement evaluates as false
print((min_age >= legal_age) and (legal_age >= min_age))

#only one of these statements has to evaluate as true for this statement to be true
print((min_age >= legal_age) or (legal_age >= min_age))

#checking if min_age is not equal to legal_age 
print(min_age != legal_age)

#sonic_the_hedgehog is not an snes game so the print statement was 
#"Ah, that's sounds like a good game, but it's not in my list."
snes_games = ["The Legend of Zelda", "Donkey Kong", "Super Mario Bros"]
game = 'sonic_the_hedgehog'

if game not in snes_games:
	print ("Ah, that's sounds like a good game, but it's not in my list.")

#made a new game & checked for it the list, it's there so the message I wanted appeared
game_2 = 'The Legend of Zelda'

if game_2 in snes_games:
	print("Ah, sweet, I had that game too!")