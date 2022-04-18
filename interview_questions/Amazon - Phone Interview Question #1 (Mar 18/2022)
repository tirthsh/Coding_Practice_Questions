# Write a method/function that assesses the bracket matching of a string. It should succeed in cases where brackets are balanced and matching.
# Write this as production level code in a language of your choice
# E.g. pass cases: "[]", "(banana)", "[{fish}(banana?)]", "[fish(banana[app.le])]"
# E.g. fail cases: "[" , "][", "[{banana]", "{[}]"

'''
Input -> string
Output -> Boolean (True if string is valid, else False)
Assumptions ->  0<= len(s), s=None
Edge cases -> length of string is 0, or None, return True
Examples ->
    s = "", return True
    s = None, return True
    s = (banana), return True
    s = [{banana] 
Algorithm ->
    - use a stack to keep track of opening brakets
    - use a dictionary to keep track of mapping of each closing bracket
Complexity -> 
    Time -> O(n)
    Space -> O(n)
'''

def validateString(s):
    #edge cases
    if s == None or len(s) == 0:
        return True
    
    #will keep track of opening brackets
    stack = []
    
    mapping = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    
    #go through each character in string
    for char in s:
        #if its an opening bracket, add to stack
        if char in mapping.values():
            stack.append(s)
        elif char in mapping.keys():
            opening_bracket = stack.pop()
            if mapping[char] != opening_brakcet:
                return False
        
    return len(stack) == 0
            
            