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
        Complexity -> Time: O(n^2), Space: O(1)
        '''
        max_palindrome = ""
        
        #go through each substring 
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                #if the substring is a palindrome, store if its the longest substring seen so far
                if self.isPalindrome_helper(substring):
                    tmp_palindrome = s[i:j+1]
                    if len(tmp_palindrome) > len(max_palindrome):
                        max_palindrome = tmp_palindrome
        
        return max_palindrome
            
    #helper to find if a string is a substring or not
    def isPalindrome_helper(self, s):
        if len(s) <= 1:
            return True
    
        return s[0] == s[-1] and self.isPalindrome_helper(s[1:-1])

s1 = "babad"
s2 = "cbbd"
s3 = "tracecars"

solution = Solution()
max_pal = solution.longestPalindrome(s1)
print(max_pal)

max_pal = solution.longestPalindrome(s2)
print(max_pal)

max_pal = solution.longestPalindrome(s3)
print(max_pal)