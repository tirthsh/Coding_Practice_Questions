#depth first search
class Solution1:
    visited = []
    def dfs(self, graph, node, visited):
        if node not in visited:
            print(node + " -> ", end="")
            visited.append(node)
            for neighbor in graph[node]:
                self.dfs(graph, neighbor, visited)

#adjaceny list
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : [],
  'D' : [],
  'E' : []
}

solution1 = Solution1()
solution1.dfs(graph, 'A', [])

