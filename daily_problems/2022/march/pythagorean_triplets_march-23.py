import math

def pythagorean_triplets(nums):
    
    #assume size of nums is at least 3

    nums.sort() #O(nlog(n)) -> [4,5,6,10,12]

    #sliding window
    first_num_index = 0
    second_num_index = 1

    for each_num in nums[2:]: #start at 3rd num 
        first_num = nums[first_num_index] #4
        second_num = nums[second_num_index] #5

        if math.pow(first_num,2) + math.pow(second_num,2) == math.pow(each_num, 2): #16 + 25 != 36
            return True
        
        first_num_index = second_num_index #slide window
        second_num_index += 1
    
    return False

nums = [10, 4, 6, 12, 5]
print(pythagorean_triplets(nums))


