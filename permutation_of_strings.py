def generate_capitalization_permutations(string):

    results = []
    number_of_string = len(string)

    def backtrack(index, current_string):
        print(index)
        if index == number_of_string:

            results.append(current_string)
            return

        char = string[index]

        if char.isalpha():

            backtrack(index + 1, current_string + char.lower())

            backtrack(index + 1, current_string + char.upper())
        else:

            backtrack(index + 1, current_string + char)


    backtrack(0, "")
    return results


input_string = "abc"
permutations = generate_capitalization_permutations(input_string)
print(f"Input: '{input_string}'")
print(f"Output: {permutations}")




