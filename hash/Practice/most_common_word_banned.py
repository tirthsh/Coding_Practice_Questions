#https://leetcode.com/problems/most-common-word/
import re #regular expression

class Solution:
    def mostCommonWord(self, paragraph, banned):
        mapping = {}
        pattern = "[^0-9a-zA-Z\s]+"
        paragraph = re.sub(pattern, " ", paragraph.lower())
        list_of_words = paragraph.split(" ")

        for each_word in list_of_words:
            if each_word not in banned:
                if each_word not in list(mapping.keys()):
                    mapping[each_word] = 1
                else:
                    mapping[each_word] += 1
        
        max_count = float("-inf")
        max_word = ""
        for each_word in mapping:
            if mapping[each_word] > max_count and each_word != "":
                max_count = mapping[each_word]
                max_word = each_word

        return max_word


solution = Solution()
banned = ['hit']
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#print(solution.mostCommonWord(paragraph, banned))

banned = []
paragraph = "a."
#print(solution.mostCommonWord(paragraph, banned))

banned = ["a"]
paragraph = "a, a, a, a, b,b,b,c, c"
print(solution.mostCommonWord(paragraph, banned))
