first_name = "monty"
last_name = "python"
greetings = "hello"
greet_person = greetings + " " + first_name + " " + last_name
print (greet_person)
# famous works
famous_sketch1 = "\n\t Hell's Grannies"
# n = new line & \t = tab
famous_sketch2 = "\n\t The Dead Parrot"

print("Famous Work:" , famous_sketch1, famous_sketch2)
#cracklepop exercise for recurse
#Write a program that prints out the numbers 1 to 100 (inclusive). 
#If the number is divisible by 3, print Crackle instead of the number. If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. 
#Please use whichever language you're focused on learning. 
#kept getting unexpected indent error for line 1 in repl.it >_<  
n = range(100)
    if n % 3 = 0:
        print "crackle"
    else:
        n % 5 = 0:
            print "pop"
    elif: n % 3 == n % 5:
        print "crackle_pop"