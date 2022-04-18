#https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        if not nums or len(nums) == 0:
            return subsets
    
        self.generateSubsets(0, nums, [], subsets)
        
        return subsets

    def generateSubsets(self, index, nums, current_subset, subsets):
        subsets.append(current_subset)
        for i in range(index, len(nums)):
            #generate subset to include the number at i
            current_subset.append(nums[i])
            self.generateSubsets(i + 1, nums, current_subset, subsets)
            #genearte subset to not include the number at i 
            #(which will be the last number in the current set since we just added it in line 17)
            current_subset.pop(len(current_subset)-1)

        
        
        
        