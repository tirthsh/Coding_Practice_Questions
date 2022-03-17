'''
You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 12,
return true since 4 + 1 = 5.
'''

def two_sum(nums, target):
    if len(nums) == 0:
        return False
    
    hash_map = {}
    for each_num in nums:
        print(hash_map)
        compliment = target - each_num
        #if compliment is not in the hash map, add [key, compliment]
        if compliment not in list(hash_map.keys()):
            hash_map[each_num] = compliment
        else:
            #if compliment is in the hash map then we found our pair
            return True 
    
    return False

nums = [4, 7, 1 , -3, 2] 
target = 7

print(two_sum(nums, target))