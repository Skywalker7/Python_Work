#hello admin exercise

usernames = ["Peg Carter", "Howard Stark", "Daniel Souza", "Edwin Jarvis", "Jack Thompson", "admin"]

for username in usernames:
	if username == 'admin' in usernames:
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello," + " " + username + "," + " " + "welcome back!")

#no users 
#check code--it wasn't running compare to code on page 91
#fixed it; syntax error didn't pop but something was up. Spacing maybe? I wrote the code 
#again this time making sure I didn't mix spacing & tabs

admin_members = []

if admin_members:
	for admin_member in admin_members:
		print("Adding " + admin_member + ".")
	#print("\nFinished making your pizza!")
else:
	print("We need to find some users!")
   		

#Checking user names
#check code -- compare with code on page 92
#fixed it. I wasn't looping through the new users to check if the new_user matched with 
#one of the current_users

current_users = ["Black Widow", "Captain America", "Iron Man", "The Hulk", "Thor"]

new_users = ["Daisy Johnson", "Agent Mae", "Captain America", "Agent Coulson", "Gemma Simmons"]

for new_user in new_users:
	if new_user in current_users:
		print("Hi," + " " + new_user + "!" + " " + "That user name is taken.")
	else:
		print("Hey" + " " + new_user + "," + " " + "that user name is available.")

#Ordinal Numbers

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print( str(number) + "nd")
	elif number == 3:
		print( str(number) + "rd")
	else:
		print( str(number) + "th")
