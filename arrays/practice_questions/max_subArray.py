#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray_bruteforce(self, nums: List[int]) -> int:
        '''
        Input -> list of integers (list of numbers)
        Output -> int (largest sum)
        Assumptions -> must be contiguous subarray, can be positive or negative
        Edge cases -> if length is 1, return nums[0]
        Examples ->
        Algo ->
        Complexity -> 
        '''
        largest_sum = float("-inf")
        
        for i in range(0, len(nums)):
            tmp_sum = nums[i]
            if tmp_sum > largest_sum:
                largest_sum = tmp_sum
            
            for j in range(i+1, len(nums)):
                tmp_sum += nums[j]
                if tmp_sum > largest_sum:
                    largest_sum = tmp_sum
            
        
        return largest_sum
    
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Input -> list of integers (list of numbers)
        Output -> int (largest sum)
        Assumptions -> must be contiguous subarray, can be positive or negative
        Edge cases -> if length is 1, return nums[0]
        Examples ->
        Algo ->
        Complexity -> 
        '''
        largest_sum = float("-inf")
        tmp_sum = 0
        
        for i in range(0, len(nums)):
            #simulate what happens if we take contiuous nums
            tmp_sum = max(nums[i], nums[i] + tmp_sum)
            if tmp_sum > largest_sum:
                largest_sum = tmp_sum
            
        return largest_sum
        
        
        