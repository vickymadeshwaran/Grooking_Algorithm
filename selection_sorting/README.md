## Selection_Sorting

Selection Sort involves iteratively selecting the smallest element from an unsorted portion and swapping it with the first unsorted element, gradually sorting the array.

## Usage

Run `selection_sorting_method_1.py` in a Python environment.

or

Run `selection_sorting_method_2.py` in a Python environment.

## Sample Output's
### 1. Selection_sorting_method_1.py

Hard Coded Value [5, 4, 3, 2, 1]

Result [1, 2, 3, 4, 5]

### 2. Selection_sorting_method_2.py

Hard Coded Value [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Result [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .

## Complexity Analysis
### 1. Selection_sorting_method_1.py

Time Complexity: O(n^2) due to nested loops (find_smallest function inside selection_sorting function).

Space Complexity: O(n) due to the creation of a new array to store sorted elements.

### 2. Selection_sorting_method_2.py

Time Complexity: O(n^2) because of nested loops (find_smallest within selection_sorting).

Space Complexity: O(1) since sorting is performed in-place, requiring minimal additional space.
