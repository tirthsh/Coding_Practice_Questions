#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        '''
        Inputs -> list of integers (non-negative), target_sum
        Outputs -> list of two indicies in which their values add up to the target_sum
        Edge cases -> negative #s, no solution, duplicate answers
        Assumptions -> positives, may not be sorted
        Complexity -> O(n) -> hashing 
        Example -> input_nums = [1,4,2] target_sum = 3, answer = [0,2]
        Algorithm
            - create a hash table where key is the index of where that number is located and value is the compliment of the number at that key
            - find if compliment exists else add it to hash table {key: compliment}
        '''

        '''
        Sample hash table
        {
        0: 2
        1: -1
        2: 1
        }
        '''
        
        hash_table = {}
        for i in range(0, len(nums)):
            num = nums[i]
            compliment = target - num
            if num in list(hash_table.values()):
                compliment_index = list(hash_table.keys())[list(hash_table.values()).index(num)]
                return [i, compliment_index]
            else:
                hash_table[i] = compliment
            
        return []
        
solution = Solution()
inputs = [2,1,0,15]
target = 17

print(inputs)
print(target)
print(solution.twoSum(inputs, target))
            