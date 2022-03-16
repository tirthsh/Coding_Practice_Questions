#https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m, n):
        '''
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        '''
        #how to make 2d array in python - https://www.delftstack.com/howto/python/python-initialize-2d-array/
        dp = []
        first_row = [1] * n
        #first row is all 1s
        dp.append(first_row)

        '''
        Start with filling 1st row and 1st column with 1 -> there's only 1 way to get to those places 
        1   1   1
        1   0   0

        Then at dp[i][j] -> you want to add # of possible paths from above (dp[i-1][j]) and from left (dp[i][j-1])

        1   1   1
        1   2   0

        1     1         1
        1   2(2+1)   3 (2+1)

        '''
        
        base = []
        #first column is 1, rest is 0s (to be determinied)
        for i in range(0,n):
            if i == 0:
                base.append(1)
            else:
                base.append(0)
        
        #add rest of rows
        for j in range(1, m):
            dp.append(base)
                
        #dynamic programming
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        #return bottom right corner value
        return dp[m-1][n-1]
        
        
        
m = 3
n = 7

solution = Solution()
print(solution.uniquePaths(m,n))