# Python code to realise iterative Binary Search 

def binary_search(list, search):
    """
    - Searches a sorted array by repeatedly 
    dividing the search interval in half
    - returns index of given search param
    - time complexity to log2(n)
    """

    low = 0
    high = len(list) - 1 

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        # Repeatedly checks if the value is found
        if guess == search:
            return mid

        elif guess > search:
            high = mid - 1

        else:
            low = mid + 1

    return None


"""
sorted array mylist[] of n=5 elements, 
max_tries = log2(5)
max_tries = 2.3219280949
"""
my_list = [1,3,5,7,9]


print(binary_search(my_list, 4))
print(binary_search(my_list, 3))

