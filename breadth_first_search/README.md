## Breadth_First_Search

The code performs a breadth-first search in a graph representing relationships between people to find if there is a person with a name ending in 'b', indicating a mango seller, starting from the person named "you".

## Usage

Run 'breadth_first_search.py'

The result will show the mango seller in your connection

For testing, change line number 39 'b' with ending character of other persons name.

### Family Tree

- **You**
  - Knows: Bob, Alice, Claire
    - Bob
      - Knows: Peggy, Anuj
    - Alice
      - Knows: Peggy
    - Claire
      - Knows: Thom, Johnny
     
## Sample Output

Bob is a mango seller.

## Complexity Analysis

The time complexity of the code is O(V + E), where V is the number of vertices (people) and E is the number of edges (relationships) in the graph.

The space complexity is O(V), where V is the number of vertices (people) in the graph. This is due to the storage of the search_queue and searched lists, which can potentially hold all vertices.
