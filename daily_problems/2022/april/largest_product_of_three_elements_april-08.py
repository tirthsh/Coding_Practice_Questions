class Solution:
    def maximumProduct(self, nums):
        if not nums or len(nums) == 0:
            return 
        
        nums.sort()
        
        return max(nums[0]*nums[1]*nums[len(nums)-1], 
                  nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3])
        
solution = Solution()
nums = [-4,-4,2,8]

print(solution.maximumProduct(nums))