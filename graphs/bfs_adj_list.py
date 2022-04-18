graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

queue = []
visited = []

def bfs(visited, graph, node):

    if node == '' or node == None:
        return visited
    
    visited.append(node)
    queue.append(node)

    while len(queue) != 0:
        curr = queue.pop(0)

        for each_child in graph[curr]:
            if each_child not in visited:
                #this step is different than dfs
                #in bfs, we add child to visited right away
                visited.append(each_child)
                queue.append(each_child)
    
    return visited

ans = bfs(visited, graph, 'A')
print(ans)