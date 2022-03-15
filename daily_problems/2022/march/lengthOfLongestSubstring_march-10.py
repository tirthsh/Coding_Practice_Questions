#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring_brute_force(self, s):
        '''
        Inputs -> string of characters
        Outputs -> returns integer of length of longest substring without repeating
        Edge Cases -> empty string, solution does not exist, multiple of same length
        Assumptions -> empty string possible, at least 1 solution exists
        Examples -> s = 'abcabb' output = 'abc'
        Complexity -> Time -> O(n^2), Space -> O(n)
        Algorithm -> Go through every single permutation of non-repeating substrings, and keep track of max length
        '''
        
        #brute force 
        max_len = 0
        tmp_len = 0
        hash_table = {} #we can use a hash table(dict) or a list
        
        #go through all permutations
        for i in range(0,len(s)):
            outter_char = s[i]
            hash_table[outter_char] = 1
            
            tmp_len = 1
                
            for j in range(i + 1, len(s)):
                other_char = s[j]
                #if our char is in hash map, means its a duplicate
                if other_char in hash_table:
                    #update max length before moving on to next substring
                    if tmp_len > max_len:
                        max_len = tmp_len
                    #clean hash table to reset
                    hash_table = {}
                    break
                else:
                    #char not in table, not a duplicate
                    hash_table[other_char] = 1
                    #update tmp length
                    tmp_len = len(hash_table)
        
            if tmp_len > max_len:
                max_len = tmp_len
        
        return max_len
                
            
    def lengthOfLongestSubstring(self, s):
        '''
        Inputs -> string of characters
        Outputs -> returns integer of length of longest substring without repeating
        Edge Cases -> empty string, solution does not exist, multiple of same length
        Assumptions -> empty string possible, at least 1 solution exists
        Examples -> s = 'abcabb' output = 'abc'
        Complexity -> Time: O(n), Space: O(n)
        Algorithm -> Keep track of two pointers, start and next. Keep incrementing next until you 
        '''
            
        start_index = 0
        next_index = 0
        hash_table = {}
        max_len = 0
        tmp_len = 0
        
        while next_index < len(s):
            start_char = s[start_index]            
            next_char = s[next_index]
            
            #if next char is not in our table, means its not a duplicate, we can add it and find new tmp length
            if next_char not in hash_table:
                hash_table[next_char] = 1
                tmp_len = len(hash_table)
                next_index += 1
            else:
            #means we found a duplicate
                #update our max length before going to next possible substring
                if tmp_len > max_len:
                    max_len = tmp_len
                
                start_index += 1
                next_index = start_index
                #erase our hash table
                hash_table = {}

        #needed in case we reach the end without changing max_len 
        #i.e. s = 'au'  
        if tmp_len > max_len:
            max_len = tmp_len
        
        return max_len
        

s1 = "abcabcbb" #abc
s2 = "bbbbb" #b
s3 = "pwwkew" #wke
s4 = "au" #au
s5 = "a" #a
s6 = " " # " "
s7 = "" # 

solution = Solution()

ans_brute = solution.lengthOfLongestSubstring_brute_force(s1)
ans = solution.lengthOfLongestSubstring(s1)

print(ans_brute)
print(ans)

ans_brute = solution.lengthOfLongestSubstring_brute_force(s2)
ans = solution.lengthOfLongestSubstring(s2)

print(ans_brute)
print(ans)

ans_brute = solution.lengthOfLongestSubstring_brute_force(s3)
ans = solution.lengthOfLongestSubstring(s3)

print(ans_brute)
print(ans)

ans_brute = solution.lengthOfLongestSubstring_brute_force(s4)
ans = solution.lengthOfLongestSubstring(s4)

print(ans_brute)
print(ans)

ans_brute = solution.lengthOfLongestSubstring_brute_force(s5)
ans = solution.lengthOfLongestSubstring(s5)

print(ans_brute)
print(ans)

ans_brute = solution.lengthOfLongestSubstring_brute_force(s6)
ans = solution.lengthOfLongestSubstring(s6)

print(ans_brute)
print(ans)

ans_brute = solution.lengthOfLongestSubstring_brute_force(s7)
ans = solution.lengthOfLongestSubstring(s7)

print(ans_brute)
print(ans)