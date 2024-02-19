'''
The code defines a function search(name) to find a mango seller in a social network represented as a graph, using a breadth-first search algorithm. 
The graph is defined with individuals and their connections, and the search starts from a person named "you." 
The function prints and returns True if a mango seller is found, based on a simple condition (person_is_seller function).
'''

# Importing the 'deque' class from the 'collections' module for efficient queue implementation
from collections import deque

# Function to perform a breadth-first search for a mango seller in the graph
def search(name):
    
    # Create a queue for the search
    search_queue = deque()
    # Enqueue the neighbors of the initial person into the queue
    search_queue += graph[name]
    # List to keep track of people already searched
    searched = []

    while search_queue:
        # Dequeue a person from the search queue
        person = search_queue.popleft()
        # Check if the person has not been searched before
        if not person is searched:
            # Check if the person is a mango seller
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                # Enqueue the neighbors of the current person
                search_queue += graph[person]
                # Mark the current person as searched
                searched.append(person)
    return False


# Function to check if a person is a mango seller (based on a simple condition)
def person_is_seller(name):
    return name[-1] == 'b'

# Dictionary representing the graph of relationships between people
graph = {}
graph["you"] = ["Bob", "Alice", "Claire"]
graph["Bob"] = ["Peggy", "Anuj"]
graph["Alice"] = ["Peggy"]
graph["Claire"] =  ["Thom", "Johnny"]
graph["Peggy"] =  []
graph["Anuj"] =  []
graph["Thom"] = []
graph["Johnny"] =  []

# Initial setup: Enqueue the neighbors of the starting person ("you") into the search queue
search_queue = deque()
search_queue += graph["you"]

search("you")
