#use bfs when we want to check shortest path
def find_shortest_path(graph, start, end):
    if graph == None or start == None or end == None:
        return -1
    
    if start == end:
        print("Start and end is the same...")
        return 0

    visited = []
    queue = []

    queue.append([start])

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            for each_neighbor in neighbors:
                new_path = list(path)
                new_path.append(each_neighbor)

                queue.append(new_path)

                if each_neighbor == end:
                    print(new_path)
                    return new_path
            
            visited.append(node)
    
    print("Could not find a path")
    return -1

graph = {'A': ['B', 'E', 'C'],
        'B': ['A', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'F'],
        'F': ['C', 'G', 'D'],
        'G': ['C', 'D']}
find_shortest_path(graph, 'A', 'D')
