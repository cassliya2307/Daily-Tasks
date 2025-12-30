
def count_occurrence(characters):
    character = characters.lower()
    occurrence = 0
    for index in range(len(character) - 1):
        count = 0
        for char in character:
            if(character[index] == char):
                count+= 1
                if count > 1:
                    occurrence += 1
    return occurrence
