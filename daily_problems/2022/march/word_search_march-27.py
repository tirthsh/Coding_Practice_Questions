class Solution:
    def exist(self, board, word):
        #represents all 4 directions
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        #have a visited array to keep track of what you've already visited and what you've not
        #0 -> not visited yet, 1 -> already visited
        def dfs(i, j, word_index, visited):

            #check if we're not out of range
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False
            
            #check if we haven't already visited that node, or if the current letter doesnt match what we're looking for
            if visited[i][j] == 1 or board[i][j] != word[word_index]:
                return False
            
            #mark current place as visited
            visited[i][j] = 1

            #if its the last letter, means we've reached the end
            if word_index == len(word)-1:
                return True
            
            #go through all 4 directions and check if we can find the NEXT letter (word_index + 1)
            ans = False
            for each_direction in dirs:
                new_x, new_y = i + each_direction[0], j + each_direction[1]
                ans |= dfs(new_x, new_y, word_index + 1, visited)
            
            #reset so next char can start fresh
            visited[i][j] = 0
            return ans

        #if board is None or empty, dont do anything
        if not board or len(board) == 0:
            return False
    
        word_index = 0

        #created a visited array, filled with 0s
        visited = [[0] * len(board[0]) for _ in range(len(board))] 
        
        #go through each letter
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if dfs(i, j, 0, visited):
                    return True
        print(visited)
        return False
        

solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "AA"
print(solution.exist(board, word))

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(solution.exist(board, word))

