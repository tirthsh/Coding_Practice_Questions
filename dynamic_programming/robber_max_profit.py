#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums):
        '''
        Input -> list of integers 
        Output -> int (represents max amount of money to rob)
        Assumptions -> integers in the list are non-negative (0+), length of list is at least 1
        Edge cases -> 
            length of list is 1
            **optimal distance further than 2 houses apart - i.e. [3,2,1,3]
        Examples -> 
            nums = [1,2,3,4] money = 6
            nums = [1] money = 1
            nums = [4,2,5,3,1] money = 10
            **nums = [3,2,1,3] money = 6
        Algo -> DP as its asking to find max
        Complexity -> 
        '''
        if len(nums) == 0:
            return 0
        
        dp = [-1] * len(nums)
        
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            #store max of index 0 and 1 at index 1
            if i == 1:
                max_money = nums[i]
            else:
                #find max money
                max_money = nums[i] + dp[i-2]
            #store max money of previous and current
            dp[i] = max(max_money, dp[i-1])
        
        #you want to find max of the last two values 
        return max(dp[len(dp) - 1], dp[len(dp) - 2])

solution = Solution()
nums1 = [1,2,3,1] #4
nums2 = [1] #1
nums3 = [2,1,1,2] #4
nums4 = [2,1,3,3,4] #9

max_profit = solution.rob(nums1)
print(max_profit)

max_profit = solution.rob(nums2)
print(max_profit)

max_profit = solution.rob(nums3)
print(max_profit)

max_profit = solution.rob(nums4)
print(max_profit)