#https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #if string is none or empty
        if not dominoes or len(dominoes) == 0:
            return ""
        
        #convert to list so a) easier to traverse b) can maniuplate a list -> cannot manipulate a string
        dominoes_list = list(dominoes)
        queue = []
        
        
        #add all L and R to the queue -> we don't care if its a "."
        for i in range(len(dominoes_list)):
            char = dominoes_list[i]
    
            if char == "L" or char == "R":
                #add the index as well (i)
                queue.append((i, char))
        
        
        while queue:
            #get the first item
            i, char = queue.pop(0)
            
            #if char is left
            if char == "L":
                #we need to make sure i-1 doesn't go out of bounds before we change
                #only change if previous char is a "."
                if i > 0 and dominoes_list[i-1] == ".":
                    dominoes_list[i-1] = "L"
                    #once we change it, add to queue (at the end)
                    queue.append((i-1, "L"))
                    
            #if char is right
            elif char == "R": 
                #we need to make sure i+1 doesnt go out of bounds before we change
                #only change if next char is a "."
                if i + 1 < len(dominoes_list) and dominoes_list[i+1] == ".":
                    #before we change the next char, check if the next, next char is not "L" 
                    #if it is, remove that "L" and dont do anything 
                    if i + 2 < len(dominoes_list) and dominoes_list[i+2] == "L":
                        queue.pop(0)
                    else:
                        #if its not a "L" then change next char to R and add to queue
                        dominoes_list[i+1] = "R"
                        queue.append((i+1, "R"))
        
        #get string from list
        return "".join(dominoes_list)