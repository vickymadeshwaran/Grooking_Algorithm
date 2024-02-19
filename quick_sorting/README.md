## Quick_Sort
Quick Sort is a highly efficient sorting algorithm that follows the divide-and-conquer paradigm.

It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The process is then applied recursively to the sub-arrays, eventually resulting in a fully sorted array.

## Usage

Run `quick_sort.py` in a Python environment.

## Sample Output

Hard Coded : [10,8,6,4,2]

Output : [2,4,6,8,10] .

## Complexity Analysis

### The Time Complexity

The average and best cases is O(n log n). This occurs when the pivot selection and partitioning consistently divide the array into approximately equal halves, resulting in efficient sorting.

The worst-case time complexity is O(n^2). This occurs when the pivot selection always chooses the smallest or largest element, leading to highly unbalanced partitions in each recursive step.

### The Space Complexity

The average case is O(log n) due to the recursive calls. It occurs when the pivot selection and partitioning result in balanced partitions, keeping the depth of recursion shallow.

In the worst-case the complexity can reach O(n) due to an unbalanced partitioning, causing the depth of recursion to match the size of the input array.
