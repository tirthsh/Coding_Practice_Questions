class Solution:

    def climbStairs_recursive(self, n):
        if n == 0 or n == 1:
            return 1
        
        return self.climbStairs_recursive(n-1) + self.climbStairs_recursive(n-2)

    def climbStairs(self, n):
        '''
        steps | ways
        ------------
          0      1
          1      1
          2      2 
          3      3
          4      5
          5      8
        '''
        if n <= 1:
            return 1
        
        dp = [1] * (n+1)
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        
        
solution = Solution()
n = 100
print(solution.climbStairs(n))
print(solution.climbStairs_recursive(n))