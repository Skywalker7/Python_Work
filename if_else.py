#if else elif workout 

alien_color = ["green", "yellow", "red"]

if "green" in alien_color:
	  points = 5
print("Yay, that's an alien color and you just won" + " " + str(points) + "!")

if "green" in alien_color:
	print("Yo, that's quite a color!")
elif "blue" in alien_color:
	print("So aquatic.")

#alien colors again

#violet is not in the alien_color list so the else statement runs
color = "violet"

if color in alien_color:
	points = 5
	print("You just got" + " " + str(points) + " " + "points for shooting the alien!")
else:
	points = 10
	print("Whoa, you just got" + " " + str(points) + " " + "points!")

#the color is in the alien_color list so the if statement runs
color = "green"

if color in alien_color:
	points = 5
	print("You just got" + " " + str(points) + " " + "points for shooting the alien!")
elif color not in alien_color:
	points = 10
	print("Whoa, you just got" + " " + str(points) + " " + "points!")

#if elif else w alien_colors


#for these exercises only the if runs because Python doesn't run test beyond the first 
#test in an if elif else statement

alien_colors1 = ["yellow", "green", "red"]



if "green" in alien_colors1:
	print("Cool, you just earned" + " " + str(5) + " " + "points!")
elif "yellow" in alien_colors1:
	print("Cool, you just earned" + " " + str(10) + " " + "points!")
elif "red" in alien_colors1:
	print("Cool, you just earned" + " " + str(15) + " " + "points!")

print("Finished earning points?")


if "red" in alien_colors1:
	print("Cool, you just earned" + " " + str(15) + " " + "points!")
elif "green" in alien_colors1:
	print("Cool, you just earned" + " " + str(5) + " " + "points!")
elif "yellow" in alien_colors1:
	print("Cool, you just earned" + " " + str(10) + " " + "points!")

print("Finished earning points?")

if "yellow" in alien_colors1:
	print("Cool, you just earned" + " " + str(10) + " " + "points!")
elif "red" in alien_colors1:
	print("Cool, you just earned" + " " + str(15) + " " + "points!")
elif "green" in alien_colors1:
	print("Cool, you just earned" + " " + str(5) + " " + "points!")

print("Finished earning points?")

# all of the statements print for this exercise because it is a series of if statements
alien_colors1 = ["yellow", "green", "red"]

if "green" in alien_colors1:
	print("Cool, you just earned" + " " + str(5) + " " + "points!")
if "yellow" in alien_colors1:
	print("Cool, you just earned" + " " + str(10) + " " + "points!")
if "red" in alien_colors1:
	print("Cool, you just earned" + " " + str(15) + " " + "points!")

print("Finished earning points?")

#person's stage of life w if elif else

person_age = 14

if person_age < 2:
	print("Aw, you're a baby!")
elif person_age < 4:
	print("You're a toddler!")
elif person_age < 13:
	print("You're a kid.")
elif person_age < 20:
	print("You're a teen.")
elif person_age < 65:
	print("You're an adult.")
else:
	print("You're an elder.")

#favorite fruit exercise

favorite_fruits = ["avocado", "pineapple", "banana","strawberry","kiwi", "mango" ]

if "avocado" in favorite_fruits:
	print("Mmm, so creamy!")
if "pineapple" in favorite_fruits:
	print("So good in Pina Coladas!")
if "banana" in favorite_fruits:
	print("Keeps smoothies awesome!")
if "strawberry" in favorite_fruits:
	print("So, sweet, so good!")
if "kiwi" in favorite_fruits:
	print("Goes great with strawberries!")
if "mango" in favorite_fruits:
	print("Ah my goodness, so juicy!")
