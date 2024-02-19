# Quick Sorting
# Compare to Selection Sorting, Quick Sorting is much faster

# Define a function called quick_sort that takes an array as input
def quick_sort(array):
    # Check if the length of the array is less than 2; if so, return the array (base case for recursion)
    if len(array) < 2:
        return array
    else:
        # Set the pivot as the first element of the array
        pivot = array[0]
        # Create a list 'less' containing elements smaller than or equal to the pivot
        less = [i for i in array[1:] if i <= pivot]
        # Create a list 'great' containing elements greater than the pivot
        great = [i for i in array[1:] if i > pivot]
        # Recursively call quick_sort on the 'less' list, then concatenate the pivot and the result of quick_sort on the 'great' list
        return quick_sort(less) + [pivot] + quick_sort(great)

# Define an array
array = [10, 8, 6, 4, 2]

# Print the result of calling the quick_sort function on the defined array
print(quick_sort(array))

'''
Time Complexity:

Best and Average Case: O(n log n) - This is the average and best-case time complexity when the pivot selection and partitioning consistently divide the array into approximately equal halves.
Worst Case: O(n^2) - This occurs when the pivot selection always chooses the smallest or largest element in the array, resulting in highly unbalanced partitions.


Space Complexity:

The space complexity in this implementation is O(log n) on average for the recursive call stack due to the partitioning of the array in place.
In the worst-case scenario where the recursion depth reaches its maximum, it could become O(n) due to the recursion stack.
'''
