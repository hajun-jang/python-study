def binary_search(arr, item):
    # set search area
    low = 0
    high = len(arr) - 1
    search_frequency = 0

    while low <= high: # search until find
        mid = (low + high) // 2 # search for middle number
        guess = arr[mid]
        if guess == item: #found it
            return f"{mid}-th, search_frequency:{search_frequency}"
        elif guess > item: #big then item
            high = mid - 1
        else: # small then item
            low = mid + 1
        search_frequency += 1
        
    return f"No item in the list! search_frequency:{search_frequency}" # no item in list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(binary_search(my_list, 18))
print(binary_search(my_list, -1))