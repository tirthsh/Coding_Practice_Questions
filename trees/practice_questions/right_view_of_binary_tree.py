# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        '''
        Input -> treenode, root
        Output -> list of treenodes
        Assumptions -> 
        Edge Cases -> Empty tree, entire tree is right skewed
        Examples ->
            root = [1,2,3,null,5,null,4], output = [1,3,4]
            root = [], output = []
            root = [1,null, 2, null,null,null,3], output = [1,2,3]
        Algo ->
        Complexity
        '''
        
        #if tree is empty, then cant see anything
        if root == None:
            return []
        
        #will use BFS - use a queue
        queue = []
        #keep track of visible nodes from the right
        visible_nodes = []

        #BFS - add root node to queue
        queue.append(root)
        
        #iterate until queue is not empty
        while (len(queue) != 0):
            queue_size = len(queue)
            #go through all vertex in current level
            for i in range(0, queue_size):
                curr_node = queue.pop(0)
                #if the curr node is the LAST VERTEX on this level, means its the right most
                if (i == queue_size-1):
                    #add right most vertex to our list of visible nodes
                    visible_nodes.append(curr_node.val)
                
                #travese on left of current vertex
                if curr_node.left != None:
                    queue.append(curr_node.left)
                #travese on right of current vertex
                if curr_node.right != None:
                    queue.append(curr_node.right)
        
        return visible_nodes

vertex5 = TreeNode(5)
vertex4 = TreeNode(4)
vertex3 = TreeNode(3, None, vertex4)
vertex2 = TreeNode(2, None, vertex5)
vertex1 = TreeNode(1,vertex2, vertex3)

solution = Solution()
print(solution.rightSideView(vertex1))

vertex6 = TreeNode(6)
vertex7 = TreeNode(7, vertex6, None)
print(solution.rightSideView(vertex7))
