#https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target, nums):
        #check if nums is none or length is 0
        if not nums or len(nums) == 0:
            return 0
        
        #pointer to keep track of starting of subarray
        start = 0
        
        #minimum length - keep it as +inf, so we can keep minimum later
        minimal_len = float("+inf")
        total = 0
        
        #go through each number (nums[i] will be the end of our subarray)
        for i in range(0, len(nums)):

            #keep track of total
            total += nums[i]
            
            #as long as total is bigger or equal to target, keep moving our start pointer forward
            #also update our minimum length
            while total >= target:
                minimal_len = min(minimal_len, (i-start) + 1)
                total -= nums[start]
                start += 1
        
        #return 0 if we couldnt find, else 
        return 0 if minimal_len == float("+inf") else minimal_len
        
nums = [2,3,1,2,4,3]
target = 7

solution = Solution()
print(solution.minSubArrayLen(target, nums))

            
        