import time
def get_typing_accuracy(sentence , typed):
	
	time_taken_to_type = start_point - end_point
	
	words = sentence_to_type.split()

	typed_words = typed_input.split()
	
	correct_words = 0
	index = 0
	if len(words) == len(typed_words): 
		for word in words:
			if word == typed_words[index]:
				correct_words += 1
			index += 1
	else:
		print("The sentence is wrong!")
		
	
	accuracy = correct_words / len(words) * 100
	if time_taken_to_type > 0:
		word_per_minute = words / (time_taken_to_type / 60)
	else:
		word_per_minute = 0
	
	return time_taken_to_type, word_per_minute , accuracy	





sentence_to_type = "Anime is amazing isn't it?"
	
start_point = time.time()
typed_input = input(f"Enter the sentence '{sentence_to_type}' : ");
end_point = time.time()

typing = get_typing_accuracy(sentence_to_type , typed_input)

print(f"You took {typing[0] * -1:.2f} seconds to type~")
print(f"Words_per_minute {typing[1]:.2f}")
print(f"Typing accuracy = {typing[2]:.2f}%")