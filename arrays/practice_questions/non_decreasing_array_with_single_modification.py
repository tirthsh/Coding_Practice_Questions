#https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums):
        modification_count = 0 
        
        #if length of nums is less than or equal to 1, then we'll only need to make upto 1 modification
        if len(nums) <= 1:
            return True
        
        #make sure we only traverse to n-2 index (so we can do n-1) -> else index out of range for nums[i+1]
        for i in range(0, len(nums)-1):
            #if curr num is greater than next num, we need to make 1 modification
            if nums[i] > nums[i+1]:
                modification_count += 1

                #if next num is less than prev num, we need to update next num to be at least curr num
                #we skip i=0 so we can do i-1 (else index out of range for nums[i-1])
                if i != 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
            
            if modification_count > 1:
                return False
        
        return True
    
nums1 = [1,3,2]
nums2 = [4,2,1]
nums3 = [4,2,3]
nums4 = [3,4,2,3]
nums5 = [-1,4,2,3]

solution = Solution()

print(solution.checkPossibility(nums1))
print(solution.checkPossibility(nums2))
print(solution.checkPossibility(nums3))
print(solution.checkPossibility(nums4))
print(solution.checkPossibility(nums5))