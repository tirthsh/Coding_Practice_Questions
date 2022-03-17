'''
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

Challenge: Find a way to do this using O(1) memory.
'''

def find_non_duplicate(nums):
    '''
    Input -> list of integers 
    Output -> int, non-duplicate number, return -1 if none
    Assumptions -> only 1 number will occur once, rest will occur twice, no order, assume at least two elements exist
    Edge cases -> empty list, 1 number
    Examples ->
    Algo ->
    Complexity -> 
    '''
    
    #hash map to keep track of occurance of each num
    hash_map = {}
    for each_num in nums:
        if each_num not in hash_map:
            hash_map[each_num] = 1
        else:
            hash_map[each_num] += 1
    
    for each_num in hash_map:
        #if occurance is 1, means this num is the non_duplicate
        if hash_map[each_num] == 1:
            return each_num
    
    return -1

def find_non_duplicate_constant_space(nums):
    if len(nums) <= 1:
        return -1
    
    #time - nlog(n)
    nums.sort()
    #constant space
    prev = nums[0]

    for each_num in nums[1:]:
        if each_num != prev:
            return prev
    
    return -1

nums = [4, 3, 2, 4, 1, 3, 2]
print(find_non_duplicate(nums))

print(find_non_duplicate_constant_space(nums))
