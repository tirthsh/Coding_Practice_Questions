#https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Input -> list of numbers
        Output -> None
        Assumptions -> non-decreasing integers, length of at least 1, only contains 0,1,2 (red, white, blue resp.)
        Edge Cases -> length of nums is 1, all colors are the same
        Examples -> 
            nums = [2,1,0] -> [0,1,2]
            nums = [1,1,2,0,2] -> [0,1,1,2,2]
            nums = [1] -> [1]
            nums = [0,0,0] -> [0,0,0]
        Algo ->
        Complexity -> Time: O(n), Space: O(1)
        '''

        #left pointer will keep track of in which index can we insert 0s
        left = 0
        #right pointer will keep track of in which index can we insert 2s
        right = len(nums) - 1

        #will help go through all elems in the list
        index = 0
        

        while index <= right:
            #if current number is 0, swap with the beginning
            #essentially put the 0 where all 0's are located (determined by left pointer)
            if nums[index] == 0:
                #swap current number with 0
                nums[index] = nums[left]
                nums[left] = 0
                #now new index of 0's will be 1 more (so next time we can insert it here)
                left += 1
            #if current number is 2, swap with the end
            #essentially put the 2 where all 2s are located (determined by right pointer)
            elif nums[index] == 2:
                #swap
                nums[index] = nums[right]
                nums[right] = 2
                #now new index of 2's will be 1 less (so next time we can insert it here)
                right -= 1
                #negate to increasing index += 1 every time
                #i.e. we dont want to increase our index when we are swapping with a 2 
                #bc we could possibly put a 0 in the middle 
                #i.e. go through an example -> [0,1,2,1,0,2]
                #we will eventually have [0,1,0,1,2,2]
                #                             - <- this index
                index -= 1
        
            #go to next element (every time - but techincally only when we see a 0 or 1)
            #will be negated if we see a 2 bc of line 52
            index += 1
     
        
nums = [2,0,2,1,1,0]
solution = Solution()
solution.sortColors(nums)

print(nums)