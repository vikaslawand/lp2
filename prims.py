import heapq

def prim(graph):
    # Initialize an empty set to store visited vertices
    visited = set()
    # Initialize a priority queue to store edges
    pq = []
    # Initialize a minimum spanning tree
    mst = []
    
    # Start from an arbitrary vertex, here we choose the first vertex
    start_vertex = next(iter(graph))
    # Mark the start vertex as visited
    visited.add(start_vertex)
    
    # Add all edges incident to the start vertex to the priority queue
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(pq, (weight, start_vertex, neighbor))
    
    # Repeat until all vertices are visited
    while len(visited) < len(graph):
        # Pop the edge with minimum weight from the priority queue
        weight, u, v = heapq.heappop(pq)
        
        # If the destination vertex has not been visited
        if v not in visited:
            # Add the edge to the minimum spanning tree
            mst.append((u, v, weight))
            # Mark the destination vertex as visited
            visited.add(v)
            # Add all edges incident to the destination vertex to the priority queue
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, v, neighbor))
    
    return mst

# Example usage:
graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 4), ('D', 1)],
    'D': [('B', 1), ('C', 4)]
}

mst = prim(graph)
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(edge)


