def main():
    my_name = "eli"

    # capitalize a string
    print(f"My name capitalized: {my_name.capitalize()}")

    # make a string uppercase
    print(f"My name uppercased: {my_name.upper()}")

    # make a string lowercase
    last_name = "Bandy"
    print(f"My full name lowercased: {my_name.lower()} {last_name.lower()}")

    # compare two strings
    my_name_title_case = "Eli"
    if my_name.lower() == my_name_title_case.lower():
        print("The strings are equal.")
    else:
        print("The strings are not equal.")
    print("\nUsing the Startswith() Method\n----------------")
    # determine if a string starts with a set of characters
    print(f"{my_name} starts with a E or e: {my_name.startswith("E") or my_name.startswith("e")}")

    if(not my_name.startswith("eli") and (not my_name.startswith("Eli"))):
        print(f"You spelled {my_name.capitalize()} incorrectly.")
    else:
        print(f"You spelled {my_name.capitalize()} correctly.")

    if(not my_name.lower().startswith("eli")):
        print(f"You spelled {my_name.capitalize()} incorrectly.")
    else:
        print(f"You spelled {my_name.capitalize()} correctly.")

    print("\nUsing the Endswith() Method\n----------------")
    print(f"{my_name} ends with 'i': {my_name.endswith("i")}")

    print("\nUsing the Find() Method\n----------------")
    # find the l in Eli
    search_letter = "b"
    index_of_substring = my_name.find(search_letter)
    if index_of_substring != -1:
        print(f"The '{search_letter}' is at index {index_of_substring} in my name.")
    else:
        print(f"There is no '{search_letter}' in {my_name.capitalize()}.")

    print("\nLooping through a string\n-------------------")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters.")
    # print the letters in a string along with the index positions
    # for letter_index in range()
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index + 1}: {my_name[letter_index]}")

    print("\nSearch a string\n------------------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    # write code that counts the number of occurences of the word dog in the sentence
    # expected output: 3
    while (True):
        # start at the beginning of the string
        # search for the occurence of the word 'dog' starting at index 0
        dog_index = sentence.find(search_word, start_index)
        # do this until we don't find any more dogs: when find() returns -1
        if dog_index == -1:
            break
        else:
            # if we find 'dog', add 1 to some variable we use to keep track of the 
            # number of dogs we find
            # number of dogs = number of dogs + 1
            number_of_dogs += 1
            # update the starting index by 1
            start_index = dog_index + 1
            # continue searching the string from the next index after the dog we just found
            continue
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence.")



main()