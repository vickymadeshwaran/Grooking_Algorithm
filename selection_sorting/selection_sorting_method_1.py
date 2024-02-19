#Selection Sorting Method - 1

# Define a function to find the index of the smallest element in an array
def find_smallest(array):
    # Assume the first element is the smallest
    smallest = array[0]
    smallest_index = 0

    # Iterate through the array starting from the second element
    for i in range(1, len(array)):
        # If a smaller element is found, update smallest and smallest_index
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

# Define a function to perform selection sort on an array
def selection_sorting(array):
    # Create an empty list to store sorted elements
    new_array = []

    # Iterate through the entire input array
    for i in range(len(array)):
        # Find the index of the smallest element in the remaining unsorted part of the array
        smallest_index = find_smallest(array)
        
        # Pop the smallest element from the original array and append it to the new_array
        new_array.append(array.pop(smallest_index))
    
    return new_array

# Initialize an unsorted array
array = [5, 4, 3, 2, 1]

# Call the selection_sorting function and print the sorted array
print(selection_sorting(array))

# Time Complexity O(n^2) because of nested loop
# Space Complexity O(n) due to new_array[]
