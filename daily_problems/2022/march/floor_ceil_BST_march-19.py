class Treenode:
    def __init__(self,value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
#inorder traversal
class Solution:
    def floor_ceil_of_bst(self, node, k):
        answer = [None, None]

        if root == None:
            return answer
        
        stack = []
        sorted_nums = []

        curr = root

        while (curr != None or len(stack) != 0):
            while (curr != None):
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            
            if (curr.value < k):
                answer[0] = curr.value
            elif (curr.value > k and answer[1] == None):
                answer[1] = curr.value
                return answer
            else: #what if we find k? [k,k]?
                return [k,k]

            curr = curr.right

        return answer
    
    def print_stack(self, stack):
        vals = []
        for each_node in stack:
            vals.append(each_node.value)
        
        print(vals)




# node5 = Treenode(10)
# node6 = Treenode(14)
# node2 = Treenode(2)
# node3 = Treenode(6)
# node1 = Treenode(4,node2,node3)
# node4 = Treenode(12,node5,node6)
# root = Treenode(8,node1,node4)

node1 = Treenode(5)
node2 = Treenode(12)
root = Treenode(10, node1,node2)

solution = Solution()
k = 5
print(solution.floor_ceil_of_bst(root, k))
