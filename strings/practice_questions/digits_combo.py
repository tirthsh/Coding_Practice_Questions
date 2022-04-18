#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits):
        result = []

        #base case 
        if digits == None or len(digits) == 0:
            return result
        
        #create a mapping for each number to list of letters (according to telephone)
        mapping = {
            "2": ['a','b','c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
        }

        #rescursive call
        self.recursive_call(result, digits, "", 0, mapping)

        return result
    
    def recursive_call(self, result, digits, curr_combo, index, mapping):
        #base case
        #if current index has reached last digit, add to our result and exit recursive call
        if index == len(digits):
            result.append(curr_combo)
            return

        #get list of letters for current index
        #i.e. 2 -> ['a',b',c']
        letters = mapping[digits[index]]

        #recursive call
        for i in range(0, len(letters)):
            self.recursive_call(result, digits, curr_combo + letters[i], index+1, mapping)
        

solution = Solution()
print(solution.letterCombinations("23"))