# Practical 4: A* Search (Informed Search)
import heapq

graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'G': 12},
    'B': {'C': 2},
    'C': {'G': 3},
    'G': {}
}

# Heursitics (estimations to goal)
heuristics = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}

def a_star_search(graph, heuristics, start, goal):
    # Priority queue stores (f_score, current_node, path)
    # f_score = actual distance so far + estimated distance to goal
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))
    
    visited = set()
    
    while open_list:
        f_score, current_cost, current_node, path = heapq.heappop(open_list)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        if current_node == goal:
            print("Path found:", " -> ".join(path))
            print("Total Cost:", current_cost)
            return path
            
        for neighbor, travel_cost in graph[current_node].items():
            if neighbor not in visited:
                new_cost = current_cost + travel_cost
                new_f_score = new_cost + heuristics[neighbor]
                heapq.heappush(open_list, (new_f_score, new_cost, neighbor, path + [neighbor]))
                
    print("No path found.")

if __name__ == "__main__":
    print("Starting A* Search from S to G...")
    a_star_search(graph, heuristics, 'S', 'G')
