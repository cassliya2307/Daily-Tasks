list_of_friends = ["maya" , "gabriel" , "nate" , "jake" , "garry"]

for names in list_of_friends:
	if len(names) > 4:
		list_of_friends.remove(names)

print(list_of_friends)
