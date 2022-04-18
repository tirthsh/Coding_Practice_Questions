#https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbing_stairs(self, n):
        '''
        steps | ways
        ------------
          0      1
          1      1
          2      2 
          3      3
          4      5
          5      8
        
        
        Pattern: ways[i] = ways[i-1] + ways[i-2]
        '''

        if n <= 1:
            return 1

        dp = [1] * (n+1)
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


solution = Solution()
print(solution.climbing_stairs(5))