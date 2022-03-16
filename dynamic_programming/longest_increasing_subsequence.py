class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Input -> list of integers
        Output -> int (max length of increasing subsequence)
        Assumptions -> it can have negative numbers, length greater than 1
        Edge cases -> 
            - what if all nums are same in the list -> 1
            - what if all nums are increasing and unique -> len(nums)
            - what if len(nums) = 1 -> 1
        Examples -> 
            - nums = [1,2,3,4], output = 4
            - nums = [1,1,1,1], output = 1
            - nums = [1], output = 1
            - nums = [3,2,1,5,0,3,9,8], output = 3
        Algo -> 
        Complexity -> 
        '''
        
        #sub problems
        #what is the longest substring till nums[i]
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            tmp_max_index = -1
            tmp_max_val = -1
            #go through all previous subsequences 
            for j in range(0, i):
                #find the highest subsequence val of number less than num[i]
                if nums[j] < nums[i] and dp[j] > tmp_max_val:
                    tmp_max_val = dp[j]
                    tmp_max_index = j
            #if we havent updated tmp_max_index, means longest subsequence is 1 (it self)
            if tmp_max_index == -1:
                dp[i] = 1
            else:
                #longest subsequence at dp[i] will be 1 (it self) + highest subsequence value at dp[tmp_max_index]
                dp[i] = 1 + dp[tmp_max_index]
        
        print(dp)
        #return the highest subsequence val
        return max(dp)