class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Input -> string
        Output -> sub-string
        Assumptions -> length is at least 1 char, string only consists of english alphabets
        Edge cases -> 1 char, no palindrome, entire s is palindrome
        Examples -> 
            s = "a", output = "a"
            s = "million" output = "illi"
            s = "abbc", output = "bb"
        Algo ->
        Complexity ->
        '''
        max_palindrome_len = float("-inf")
        max_palindrome = ""
        
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if self.isPalindrome(substring):
                    tmp_len = (j+1) - i
                    if tmp_len > max_palindrome_len:
                        max_palindrome_len = tmp_len
                        max_palindrome = s[i:j+1]
        
        return max_palindrome
                
            
    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
    
        return s[0] == s[-1] and self.isPalindrome(s[1:-1])

s1 = "babad"
s2 = "cbbd"

solution = Solution()
max_pal = solution.longestPalindrome(s1)
print(max_pal)

max_pal = solution.longestPalindrome(s2)
print(max_pal)