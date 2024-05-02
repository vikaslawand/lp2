import heapq

def dijkstra(graph, source):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('inf') for vertex in graph}
    # Set distance of the source vertex to 0
    distances[source] = 0
    # Initialize a priority queue to store vertices and their distances
    pq = [(0, source)]  # (distance, vertex)
    
    # Iterate until priority queue is empty
    while pq:
        # Pop vertex with smallest distance from priority queue
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If current distance is greater than recorded distance, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors of current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            # If new distance is shorter than recorded distance, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add neighbor to priority queue with updated distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}
source = 'A'
shortest_distances = dijkstra(graph, source)
print("Shortest distances from", source, "to all other vertices:")
for vertex, distance in shortest_distances.items():
    print(f"To {vertex}: {distance}")

