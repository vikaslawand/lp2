# DFS algorithm in Python

def dfs(graph,start,visited=None):
    if visited is None:
        visited= set()
    
    visited.add(start)
    
    print(start,end=" ")
    
    for next_vertex in graph[start]:
        
        if next_vertex not in visited:
            dfs(graph,next_vertex,visited)
            

    return visited
    
graph={
    '0': set(['1','2']),
    '1' : set(['0','3','4']),
    '2': set(['0']),
    '3': set(['1']),
    '4':set(['1','2','3'])
    
}    

#driven Code

print("Following is the Depth-First Search")
dfs(graph,'0')
