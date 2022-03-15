#https://www.programiz.com/dsa/longest-common-subsequence
'''
The longest common subsequence (LCS) is defined as the longest subsequence that is common to all the given sequences, 
provided that the elements of the subsequence are not required to occupy consecutive positions within the original sequences
'''

'''
Input ->
Output ->
Assumptions ->
Edge cases ->
Examples -> 

S1 = {B, C, D, A, A, C, D}
S2 = {A, C, D, B, A, C}

LCS = {C,D,A,C}

Algo ->
Complexity ->

'''

def longest_subsequence_brute_force(s1,s2):
    if len(s1) <= len(s2):
        outer = s1
        inner = s2
    else:
        outer = s2
        inner = s1

    max_sequence = []
    tmp_sequence = []
    max_length = 0
    for each_elem in outer:
        if each_elem in inner:
            tmp_sequence.append(each_elem)
        



s1 = ["B", "C", "D", "A", "A", "C", "D"]
s2 = ["A", "C", "D", "B", "A", "C"]

longest_subsequence_brute_force(s1,s2)