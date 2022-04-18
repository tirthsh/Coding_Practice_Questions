#https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangeRotting(self, grid):
        if len(grid) == 0 or 2 not in grid:
            return -1
        
        minute_count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                self.dfs(i,j,grid, minute_count)
        
        print(grid)
        return -1 if 1 in grid else minute_count

    def dfs(self, i, j, grid, minute_count):
        if (i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1 or grid[i][j] == 2 or grid[i][j] == 0):
            return minute_count
        
        grid[i][j] = 2
        minute_count += 1

        self.dfs(i - 1, j, grid, minute_count)
        self.dfs(i, j - 1, grid, minute_count)
        self.dfs(i + 1, j, grid, minute_count)
        self.dfs(i, j + 1, grid, minute_count)

grid = [[2,1,1],[1,1,0],[0,1,1]]

solution = Solution()
print(solution.orangeRotting(grid))



