'''
You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 or x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.

nums = [10, 6, 8, 5] 
=> [10, 8]


nums = [4,1,9,0,1]
=> [4,9]

mapping = {
4: 1,
1: 2,
9: 1,
0: 1
}

'''

def findLonely(nums):
    '''
    Input -> list of integers
    Output -> list of distinct, with no adj numbers
    Assumptions -> non-ordered, + / - numbers, at least 1 number
    Edge Cases -> 
      1) All numbers x, have a duplicate -> [1,1,1,2,2]
      2) All numbers x, have an adj number -> [0,1,2]
    Solution
      1) Sort -> nlog(n)
      2) Brute force -> n^2
      2) Hashmap
    '''
  	mapping = {}
    output = []
    for each_num in nums:
    	if each_num not in mapping:
        	mapping[each_num] = 1
        else:
            mapping[each_num] += 1
      
    for each_num in nums:
        adj_one = each_num - 1
        adj_two = each_num + 1
    	if mapping[each_num] > 1 or adj_one in mapping or adj_two in mapping: #dont convert to list
        	continue
        else:
        	output.append(each_num)
    
    return output
