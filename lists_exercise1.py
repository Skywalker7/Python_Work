#names list exercise

names = ["Chelsea", "Audrey", "Allie"]
print(names[0])
print(names[1])
print(names[2])

#adding names to greeting message
greeting = "Hello," + " " + names[0] + "!"
print(greeting)

#a list of my own
hobbies = ["Longboarding", "Cycling", "Knitting", "Sewing"]

statement1 = "I like" + " " + hobbies[0].lower() + " " + "in warm weather."
print(statement1)
statement2 = "I enjoy" + " " + hobbies[1].lower() + " " + "with friends."
print(statement2)
statement3 = hobbies[2] + " " + "is a great exercise for the hands and the mind."
print(statement3)
statemtent4 = hobbies[3] + " " + "is a new skill I'm learning."
print(statemtent4)

#modifying lists
hobbies[1] = "Python"
print(hobbies)
# .append() adds item to the end of a list
hobbies.append("Cycling")
print(hobbies)
#adding items to an empty list
foods = []
foods.append("avocado")
foods.append("rice")
foods.append("wasabi")
print(foods)
#adding items to certain areas in a list with .insert()
foods.insert(0, "seaweed")
print(foods)
#deleting items with delete statement del 
#after use del on an item  it doesn't exist; you can't interact with it
del foods[0]

# .pop() lets you remove an item & still interact with it. It takes off the last item. 
this = foods.pop()
message = "I like" + " " + this + " " + "on my sushi."
print(message)
# if you place a number within the (), you can choose which piece of the list you use
# each time you use pop the item is no longer stored in the list
meal = foods.pop(1)
message = "This" + " " + meal + " " + "is good."
print(message)

#.remove() remove an item by its value 
# you can use also use .remove() to interact with a value that's being removed from a list
junk = ["hoverboard", "trolls", "beanie babies", "plastic eggs"]
print(junk)
junk.remove("plastic eggs")
print(junk)
#added back plastic eggs for the purpose of interacting with it and defining reason for removing it. 
# The reason = "environmental hazard"
junk.append("plastic eggs")
environmental_hazard = "plastic eggs"
junk.remove(environmental_hazard)
print(junk)
print(environmental_hazard.title() + " " + "horrible toys.")
# .remove() only removes the first occurence of the item you removed






