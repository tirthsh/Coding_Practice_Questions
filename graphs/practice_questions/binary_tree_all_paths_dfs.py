#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        
        all_paths = []
        
        def dfs(node, a_path):
            if node == None:
                return
        
            #we reached leaf node
            if node.left == None and node.right == None:
                #add to a_path and add a_path to all_paths since we reached leaf
                a_path.append(str(node.val))
                all_paths.append("->".join(a_path))
                return
            
            #not leaf node, keep traversing
            a_path.append(str(node.val))
            
            #traverse on left children
            if node.left != None:
                dfs(node.left, a_path)
                #remove leaf once traversal is completed
                a_path.pop()
                
            #traverse on right children
            if node.right != None:
                dfs(node.right, a_path)
                #remove leaf once traversal is completed
                a_path.pop()

            
        dfs(root, [])
        return all_paths
                
        
node6 = TreeNode(6)
node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node7 = TreeNode(7, node6, node4)
node2 = TreeNode(2, node7, node5)
node1 = TreeNode(1, node2, node3)

solution = Solution()
print(solution.binaryTreePaths(node1))
        
        
        
