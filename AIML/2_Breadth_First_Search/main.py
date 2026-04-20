# Practical 2: Breadth First Search (BFS)
from collections import deque

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

def bfs(graph, start_node):
    visited = set()
    # Queue is like a line of people waiting. First in, first out.
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        # Get the first person in line
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # Check all their friends (neighbors)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # Add them to the queue line
                queue.append(neighbor)
                visited.add(neighbor)

if __name__ == "__main__":
    print("Graph Structure:")
    for key, val in graph.items():
        print(f"{key} -> {val}")
        
    print("\nStarting Breadth First Search from node A:")
    bfs(graph, 'A')
    print("\nDone!")
