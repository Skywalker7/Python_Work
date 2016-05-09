#making a list with odd numbers
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
	print(odd_number)


# multiples of three

multiples = []
for value in list(range(1, 31)):
  	  multiple = value*3
  	  multiples.append(multiple)

print(multiples)



# cubes

cubing = []
for value in list(range(1,11)):
    cube = value**3
    cubing.append(cube)

print(cubing)

#cube comprehension

cubes = [value**3 for value in list(range(1,11))]
print(cubes)