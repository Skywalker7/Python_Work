#printing slice
#first prints first two slices
#second middle three
#third prints final three

slice_of_goodness = ["cake", "cheese", "cheesecake", "bacon", "pizza"]
 
print(slice_of_goodness[:2])
print(slice_of_goodness[1:4])
print(slice_of_goodness[-3:]) 

#copying and adding to pizza lists

my_pizza_pizza = ["sicilian","pepperoni", "veggie", "cheese","sausage"]
friends_pizza_pizza = my_pizza_pizza[:]

print("These are my favorite pizzas")
print(my_pizza_pizza)

print("These are my friend's favorite pizzas")
print(friends_pizza_pizza)

my_pizza_pizza.append("hawaiian")
friends_pizza_pizza.append("salad")

for pizza in my_pizza_pizza[0:4]:
	print("These are my favorite pizzas:")
	print(my_pizza_pizza)

for pizza in friends_pizza_pizza[0:4]:
    print("These are my friend's favorite pizzas:")
    print(friends_pizza_pizza)



foods_favorite = ["pizza", "cannoli", "ice cream"]
for food in foods_favorite[0:3]:
   print(food.title())



