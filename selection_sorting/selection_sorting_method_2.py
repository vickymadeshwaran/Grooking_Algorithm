#Selection Sort Method - 2

# Function to find the index of the smallest element in the array from a given index.
def find_smallest(array, index):
    # Initialize smallest_index with the provided index.
    smallest_index = index

    # Iterate through the array starting from index+1 to find the smallest element.
    for i in range(index + 1, len(array)):
        # Check if the current element is smaller than the smallest found so far.
        if array[i] < array[smallest_index]:
            # Update smallest_index if a smaller element is found.
            smallest_index = i
    
    return smallest_index

def selection_sorting(array):
    # Function to perform selection sort on the input array.
    for i in range(len(array)):
        smallest_index = find_smallest(array, i)

        # Swap the current element at index i with the smallest element found.
        array[i], array[smallest_index] = array[smallest_index], array[i]

    return array

# Initialize an example array with 10 integers in descending order.
array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Call the selection_sorting function with the array and print the sorted array.
print(selection_sorting(array))

# Time Complexity O(n^2) because of nested loop
# The space complexity of selection sort is O(1)
