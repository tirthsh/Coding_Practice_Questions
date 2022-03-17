class Solution:
    def findAllPaths(self, graph, node):
        all_paths = []

        def dfs(graph,node, a_path):
            if len(graph[node]) == 0:
                a_path.append(node)
                all_paths.append("->".join(a_path))
                return
            
            a_path.append(node)
            for each_child in graph[node]:
                dfs(graph, each_child, a_path)
                a_path.pop()
            
        dfs(graph, node, [])
        return all_paths

#adjaceny list
graph = {
  'A' : ['B','C', 'G'],
  'B' : ['D', 'E'],
  'C' : [],
  'D' : ['F'],
  'E' : ['F'],
  'G': [],
  'F': []
}

solution = Solution()
print(solution.findAllPaths(graph, 'A'))
