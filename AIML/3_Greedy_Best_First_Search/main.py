# Practical 3: Greedy Best-First Search (Informed Search)

graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'G': 12},
    'B': {'C': 2},
    'C': {'G': 3},
    'G': {}
}

# Heuristic: Estimated cost from current node to Goal 'G'
heuristics = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}

def greedy_bfs(graph, heuristics, start, goal):
    visited = set()
    path = []
    
    current = start
    while current != goal:
        visited.add(current)
        path.append(current)
        
        # Look at neighbors
        neighbors = graph[current]
        
        if not neighbors:
            print("Stuck! No way out.")
            return
            
        # Find the neighbor with the SMALLEST heuristic (appears closest to goal)
        best_neighbor = None
        min_h = float('inf')
        
        for n in neighbors:
            if n not in visited and heuristics[n] < min_h:
                best_neighbor = n
                min_h = heuristics[n]
                
        if best_neighbor is None:
            print("Stuck!")
            return
            
        current = best_neighbor
        
    path.append(goal)
    print("Path found:", " -> ".join(path))

if __name__ == "__main__":
    print("Starting Greedy Best-First Search from S to G...")
    greedy_bfs(graph, heuristics, 'S', 'G')
