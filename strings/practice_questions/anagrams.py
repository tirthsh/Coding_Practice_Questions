#https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        
        

solution = Solution()
s = "cbaebabacd"
p = "abc"
s = "abab"
p = "ab"
print(solution.findAnagrams(s, p))
