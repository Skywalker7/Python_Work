#printing original list
travel = ["england", "new zealand", "japan", "italy"]
print(travel)
#printing sorted list sorted funtion sorts list alphabetically temporarily 
print(sorted(travel))
#printing original list
print(travel)
#.reverse() method reverses the list permanently but you can use reverse to reverse the list back 
# to its original form
travel.reverse()
print(travel)
travel.reverse()
print(travel)
#.sort method permanently sorts the list alphabetically
travel.sort()
print(travel)
#using .sort(reverse=True) with on the list will permanently sort the list into reverse alphabetical order
travel.sort(reverse=True)
print(travel)

#Dinner guests to see the world with
guests = ["mom", "audrey", "tiara", "allie"]
#checking number of guests with .len() method
print(len(guests))


