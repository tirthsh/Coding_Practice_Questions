'''
Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

Given an array of integers numbers, 
your task is to check all the triples of its consecutive elements for being a zigzag. 

More formally, your task is to construct an array of length numbers.length - 2, 
where the ith element of the output array equals 1 if the triple 
(numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

Example:
For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].
For numbers = [1, 2, 3, 4], the output should be solution(numbers) = [0, 0].
For numbers = [1000000000, 1000000000, 1000000000], the output should be solution(numbers) = [0].
'''

def solution(numbers):
    '''
    input -> list of numbers, n
    output -> list of numbers results, len(results) = len(n) - 2
    assumptions -> length of n >= 3, n[i] >= 1
    edge cases ->
        1) len(n) = 3 -> base case
    '''

    results = []
    end = 2
    
    def isZigZag(end, numbers):
        num1 = numbers[end-2]
        num2 = numbers[end-1]
        num3 = numbers[end]
        
        if num1 < num2 and num2 > num3:
            return 1
        
        if num1 > num2 and num2 < num3:
            return 1
        
        return 0

    
    while end < len(numbers):
        results.append(isZigZag(end, numbers))
        end += 1
    
    return results

