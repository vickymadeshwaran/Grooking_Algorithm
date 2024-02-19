# Define the graph as a dictionary where each node is a key, and its neighbors and weights are stored in another dictionary.
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# Set initial costs for each node and initialize costs for "fin" as infinity.
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Set initial parents for each node, and initialize the parent of "fin" as None.
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# List to keep track of processed nodes during the algorithm.
processed = []

# Function to find the node with the lowest cost among the unprocessed nodes.
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        # Check if the cost is lower than the current lowest_cost and if the node is not processed.
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the initial node with the lowest cost and print it.
node = find_lowest_cost_node(costs)

# Main loop of Dijkstra's algorithm.
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    # Iterate through neighbors of the current node.
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]

        # Update the cost and parent if a shorter path is found.
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    # Mark the current node as processed.
    processed.append(node)
    # Find the next node with the lowest cost.
    node = find_lowest_cost_node(costs)
    # Print the next node.

# Print the total shortest distance to reach "fin" and its parent.
print("Total shortest distance to reach final: ", costs["fin"])
print("Parent of Destination: ", parents["fin"])
