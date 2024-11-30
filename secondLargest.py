def find_secondlargest(numbers):
    uniquenumbers = list(set(numbers))
    if len(uniquenumbers) < 2:
        return "there is no second largest number"
    uniquenumbers.sort(reverse=True)
    return uniquenumbers[1]


number_list = list(map(int, input().split()))

second_largest = find_secondlargest(number_list)
print(second_largest)
