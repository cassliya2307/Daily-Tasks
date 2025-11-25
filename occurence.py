def occurence_of_each_character_in_a_string(strings):
    new_list = []
    for string in strings:
        if string not in new_list:
            new_list.append(string)
    return new_list

