#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Input -> string of parentheses
        Output -> boolean
        Assumptions -> length of string is at least 1, string only consists of ()[]{}
        Edge Cases ->
        Examples ->
            s = (), output = True
            s = (], output = False
            s = [(}{)], output = False
            s = {}([{}]){}, output = True
        Algo -> Add opening brackets to stack, remvoe them as we see matching closing brackets. 
                If the stack is empty at the end, means its valid
        Complexity -> Time: O(n), Space: O(n)
        '''
        
        stack = []
        open_list = ["(", "{", "["]
        mapping = {
            "}": "{", 
            "]": "[", 
            ")": "("
        }
        
        #if there are odd nums of parenthesis means its not valid for sure
        if len(s) % 2 != 0:
            return False    
        
        stack.append(s[0])
    
        
        for i in range(1,len(s)):
            each_char = s[i]
            #if its an open bracket, add to stack
            if each_char in open_list:
                stack.append(each_char)
            else:
                #if its close brack, make sure latest item in stack is a corrosponding open bracket
                #if its not, means there's a closing bracket came before opening one
                if len(stack) == 0 or stack[len(stack)-1] != mapping[each_char]:
                    return False
                else:
                    #if it is, means its valid and remove the latest opening bracket from stack
                    stack.pop()
        
        #if there's still something in the stack, means there are extra brackets 
        #else its valid
        return len(stack) == 0
                
                
                     
        
s1 = "((()))"
s2 = "[()]{}"
s3 = "({[)]"
s4 = "()"
s5 = "()[]{}"
s6 = "(]"

solution = Solution()

print(solution.isValid(s1))
print(solution.isValid(s2))
print(solution.isValid(s3))
print(solution.isValid(s4))
print(solution.isValid(s5))
print(solution.isValid(s6))