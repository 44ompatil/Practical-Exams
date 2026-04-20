# Practical 1: Depth First Search (DFS)

# This graph is represented as a dictionary where keys are nodes
# and values are lists of connected nodes.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the start node as visited and print it
    visited.add(start_node)
    print(start_node, end=" ")
    
    # Go deep into the connected nodes
    for connected_node in graph[start_node]:
        if connected_node not in visited:
            dfs(graph, connected_node, visited)
            
    return visited

if __name__ == "__main__":
    print("Graph Structure:")
    for key, val in graph.items():
        print(f"{key} -> {val}")
        
    print("\nStarting Depth First Search from node A:")
    dfs(graph, 'A')
    print("\nDone!")
