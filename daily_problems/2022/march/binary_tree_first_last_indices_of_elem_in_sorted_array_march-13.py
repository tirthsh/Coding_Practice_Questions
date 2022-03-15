#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums, target):
        '''
        Input -> list of sorted integers, int as target
        Output -> list of length two, first one representing lowest index of target, second one representing highest index of target
        Assumptions -> integers are non-decreasing, non-negative (0+)
        Edge Cases -> empty list, only 1 occurance of target, no occurances of target
        Examples -> 
            nums = [5,6,7,8,9,9,10], target = 9, output = [4,5]
            nums = [5,7,7,8,8,10], target = 6, output = [-1, -1]
            nums = [], target = 0, output = [-1,-1]
        Algo ->
        Complexity ->
        '''

        if len(nums) == 0:
            return [-1,-1]

        list_of_indicies = []
        list_of_indicies = self.binary_search_recursive_call(0, len(nums)-1, nums, target, list_of_indicies)

        if list_of_indicies == []:
            return [-1,-1]
        
        else:
            return [list_of_indicies[0], list_of_indicies[len(list_of_indicies) - 1]]

    def binary_search_recursive_call(self, left, right, nums, target, list_of_indicies):
        if left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                #add index of matched target into list
                list_of_indicies.append(mid)
                #you need to search on both left and right side of the tree in case there there are more 'targets' adjacent to it
                list_of_indicies = self.binary_search_recursive_call(0, mid-1, nums, target, list_of_indicies)
                list_of_indicies = self.binary_search_recursive_call(mid+1, right, nums, target, list_of_indicies)

            #find all indices left of it
            if nums[mid] > target:
                list_of_indicies = self.binary_search_recursive_call(0, mid-1, nums, target, list_of_indicies)

            #find all indices right of it
            if nums[mid] < target:
                list_of_indicies = self.binary_search_recursive_call(mid+1, right, nums, target, list_of_indicies)

        print(list_of_indicies)
        return list_of_indicies


nums1 = [5,6,7,8,9,9,10]
target1 = 9

nums2 = [5,7,7,8,8,10]
target2 = 9

nums3 = [0,1,2,3,3,4,5]
target3 = 3

nums4 = []
target4 = 9

solution = Solution()
#print(solution.searchRange(nums1,target1))
#print(solution.searchRange(nums2,target2))
print(solution.searchRange(nums3,target3))
#print(solution.searchRange(nums4,target4))


