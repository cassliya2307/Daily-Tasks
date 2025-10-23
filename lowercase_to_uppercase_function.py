def lower_to_upper(words):
	if type(words) == str:
		output = words.upper()

	else:
		raise TypeError("You can only input a word")

	return output

words = input("Enter a sentence: ")

print(lower_to_upper(words))
