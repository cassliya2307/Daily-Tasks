def get_the_reverse_of_each_word_in_a_list( list_of_strings):
    new_list = []
    for string in list_of_strings:
        if string not in new_list:
            new_list.append(string)
    return new_list