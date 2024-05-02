graph={
    '5':['3','7'],
    '3':['2','4'],
    '2':[],
    '7':['8'],
    '4':['8'],
    '8':[]
}

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

#Driven Code                
print("Following is Breadth First Search graph:")
bfs(visited,graph,'5')
