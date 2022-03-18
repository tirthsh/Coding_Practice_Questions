class Solution:
    def numIslands(self, grid):
        if (grid == None or len(grid) == 0):
            return 0
        
        num_of_islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                #if we see a 1, we know we're on an island
                #make all adjacent 1's to a 0 to annotate we're all connected
                if grid[i][j] == '1':
                    num_of_islands += 1
                    self.dfs(i,j, grid)
        
        return num_of_islands
        
    def dfs(self, i, j, grid):
        if (i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1 or grid[i][j] == '0'):
            return 
        
        #flip it to a 0 so we don't loop back to the current spot
        grid[i][j] = '0'
        
        #make all nearby islands to 0 as well - recurisvely 
        self.dfs(i-1, j, grid)
        self.dfs(i, j-1, grid)

        self.dfs(i+1, j, grid)
        self.dfs(i, j+1, grid)
        
solution = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(solution.numIslands(grid))