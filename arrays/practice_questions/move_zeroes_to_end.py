class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #track when the last non-zero number is placed
        #when you see a non-zero number, place it here
        latest_index_of_non_zero = 0
        
        for each_num in nums:
            if each_num != 0:
                nums[latest_index_of_non_zero] = each_num
                latest_index_of_non_zero += 1
        
        #fill rest of nums after latest_index_of_non_zero with zeroes
        for i in range(latest_index_of_non_zero, len(nums)):
            nums[i] = 0
                    
        print(nums)

solution = Solution()    

nums = [0,1,0,3,12]
solution.moveZeroes(nums)


nums = [0,0,1]
solution.moveZeroes(nums)

nums = [0]
solution.moveZeroes(nums)
