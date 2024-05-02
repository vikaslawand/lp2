class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph):
    # Create a mapping from vertex names to integer indices
    vertex_indices = {vertex: index for index, vertex in enumerate(graph.keys())}
    # Create a set of all vertices in the graph
    vertices = set(graph.keys())
    # Sort all edges in non-decreasing order of their weight
    edges = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors]
    edges.sort()
    
    # Initialize a disjoint set to keep track of connected components
    disjoint_set = DisjointSet(len(vertices))
    # Initialize an empty list to store the minimum spanning tree
    mst = []

    # Iterate through all sorted edges
    for weight, u, v in edges:
        # Convert vertex names to integer indices
        u_index = vertex_indices[u]
        v_index = vertex_indices[v]
        # Check if including the edge forms a cycle
        if disjoint_set.find(u_index) != disjoint_set.find(v_index):
            # Add the edge to the minimum spanning tree
            mst.append((u, v, weight))
            # Union the sets of u and v
            disjoint_set.union(u_index, v_index)

    return mst

# Example usage:
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

mst = kruskal(graph)
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(edge)

