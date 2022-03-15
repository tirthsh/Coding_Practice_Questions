#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        '''
        Input -> list of strings
        Output -> length of max concatenated str
        Assumptions -> there's at least 1 element in the list, chars are all lowercase
        Edge cases -> 1 elem, all elements are unique
        Examples -> 
            arr = ["a"], output = 1
            arr = ["a","b","cd", "e"], output = 5
            arr = ["a", "bc", "ad", "db", "d"], output = 4
        Algo ->
        Complexity ->
        '''
        
        if len(arr) == 1:
            return len(arr[0])
        
        max_len = len(arr[0])
        tmp_max_str = ""
        #Concatenatations, means only adding to end
        for i in range(0, len(arr)):
            first_elem = arr[i]
            unique = True
            for each_elem in first_elem:
                if each_elem in tmp_max_str:
                    unique = False
                else:
                    tmp_max_str += each_elem
            if unique:
                tmp_max_str = first_elem
            for j in range(i+1, len(arr)):
                next_elem = arr[j]
                unique = True
                for each_elem in next_elem:
                    if each_elem in tmp_max_str:
                        unique = False
                if unique:
                    tmp_max_str += next_elem
                    if len(tmp_max_str) > max_len:
                        max_len = len(tmp_max_str)
                        
        
        return max_len
                        
                
                
        