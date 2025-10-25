def convert_string_to_array(string):
	result = ""
	store = []
	if type(string) == str:
		for words in string:
			if words != " ":
				result += words
			else:
				if result != "":
                			store.append(result)
               				result = ""
		if result != "":
			store.append(result)
		return store
				
	else: raise TypeError("Invalid Input")

string = "I love programming"
print(convert_string_to_array(string))


