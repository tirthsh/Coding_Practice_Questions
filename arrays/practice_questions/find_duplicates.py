#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate_bruteForce(self, nums):
        '''
        Input -> list of integers
        Output -> boolean (if duplicates exist or not)
        Assumption -> 
        Edge cases -> multiple duplicates, no duplicates
        Example -> nums = [1,0,9,1], ans = True
                   nums = [9,3,1], ans = False
                   nums = [9,9,1,1] ans = True
        Algo -> 
        Complexity -> 
        '''
        
        for i in range(0, len(nums)):
            curr_num = nums[i]
            
            if curr_num in nums[i+1:]:
                return True
        
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Input -> list of integers
        Output -> boolean (if duplicates exist or not)
        Assumption -> 
        Edge cases -> multiple duplicates, no duplicates
        Example -> nums = [1,0,9,1], ans = True
                   nums = [9,3,1], ans = False
                   nums = [9,9,1,1] ans = True
        Algo -> 
        Complexity -> 
        '''
        
        #set can never have duplicates
        new_set = set(nums)
        
        #if their lengths arent the same, means there are duplicates in the list
        return not len(new_set) == len(nums)