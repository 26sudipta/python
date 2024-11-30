31 - Exisit_in_Dictionary

My_Dict = {'name': 'Ayon', 'age': '22'}
key_to_Check = input("enter the key you want to check: ")

if key_to_Check in My_Dict:
    print(f"The key '{key_to_Check}' Exists in the dictionary.")
else:
    print(f"The key '{key_to_Check}' does not exists in the dictionary.")

32 - Merge_2_Dictionary

dictionary1 = {'a': 1, 'b': 2, 'c': 3}
dictionary2 = {'d': 4, 'e': 2, 'f': 6}

dictionary1.update(dictionary2)

print("Merge Dictionary :", dictionary1)

33 - Remove_a_key_from_dict

My_Dict = {'name': 'Ayon', 'age': '22'}
key_to_remove = input("enter the key you want to check: ")

if key_to_remove in My_Dict:
    remove = My_Dict.pop(key_to_remove)
    print(f"The key '{key_to_remove}' remove with value {remove} from the dictionary.")
    print(f"Updated dictionary = {My_Dict}")
else:
    print(f"The key '{key_to_remove}' does not exists in the dictionary.")

34 - Sort_a_Dictionary

my_dict = {
    'apple': 3,
    'banana': 1,
    'cherry': 2,
    'date': 5,
    'elderberry': 4
}
sorted_dictionary = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Dictionary sorted by values: ", sorted_dictionary)

35 - count_frequency


def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char != ' ':
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency


input_string = input("Enter a string = ")

frequency_count = count_character_frequency(input_string)

print("Character Frequency:", frequency_count)