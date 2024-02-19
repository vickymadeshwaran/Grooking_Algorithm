def binary_search(my_list, item):
    # Initialize the lower & higher index of the search range
    low = 0
    high = len(my_list) - 1

    while low <= high:
        # Calculate the middle index and Retrieve to value at the middle index
        mid = (low + high) // 2
        guess = my_list[mid]

        if guess == item:
            return mid  # Return the index where the item is found
        if guess < item:
            low = mid + 1  # Adjust the lower bound for the next iteration
        else:
            high = mid - 1  # Adjust the higher bound for the next iteration
    
    # Return None if the item is not found in the list
    return None

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(my_list,"\n")

x = int(input("Enter the Number to find the Position: "))

result = binary_search(my_list, x)  # Perform binary search to find the position

if result is not None:
    print("\nThe Position is:", result)  # Print the position where the number is found
else:
    print("\nThe Entered number is not in the list")  # Print a message if the number is not found
