graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

stack = []
visited = []

def dfs(visited, graph, node):

    if node == '' or node == None:
        return visited

    stack.append(node)

    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
        
        for each_child in graph[curr]:
            if each_child not in visited:
                stack.append(each_child)

    return visited

ans = dfs(visited, graph, 'A')
print(ans)