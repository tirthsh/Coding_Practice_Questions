#breadth first search
#we will use a QUEUE 

class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children


class Solution1:
    def bfs(self, root):
        if root == None:
            return [None]
        if root.children == None:
            return [root.data]
        
        queue = []
        visited_nodes = []

        #add root to queue
        queue.append(root)

        #keep exploring until queue is empty
        while (len(queue) != 0):            
            curr_vertex = queue.pop(0)
            visited_nodes.append(curr_vertex.data)

            if curr_vertex.children != None:
                for each_child in curr_vertex.children:
                    queue.append(each_child)

        return visited_nodes

class Solution2:
    def dfs(self, graph, node):
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)

        while len(queue) != 0:
            curr_vertex = queue.pop(0)
            print(curr_vertex + " -> ", end="")
            for neighor in graph[curr_vertex]:
                visited.append(neighor)
                queue.append(neighor)

node7 = TreeNode(7)
node6 = TreeNode(6)
node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node2 = TreeNode(2, [node7, node6, node3])
node1 = TreeNode(1, [node5, node4, node2])

solution1 = Solution1()
#print(solution1.bfs(node1))

#solution2

#adjaceny list
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : [],
  'D' : [],
  'E' : []
}

solution2 = Solution2()
solution2.dfs(graph, 'A')