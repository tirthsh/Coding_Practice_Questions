#Top-Down
#It's implemented with recursion and made efficient with memoization

'''
memoizing a result means to store the result of a function call, 
usually in a hashmap or an array, 
so that when the same function call is made again, 
we can simply return the memoized result instead of recalculating the result.
'''

# #create a list for memoization
# def feb(num):
#     memoization_list = [0] * (num + 1)

#     return memoization_technique(memoization_list, num)

# def memoization_technique(memoization_list, num):
#     if num == 0 or num == 1:
#         return num
    
#     #if the value at num has been changed, means it has already been calculated
#     if memoization_list[num] > 0:
#         return memoization_list[num]
    
#     #feb(n) = feb(n-1) + feb(n-2)
#     memoization_list[num] = memoization_technique(memoization_list, num-1) + memoization_technique(memoization_list, num-2)
#     return memoization_list[num]

memoization = {}
def calcualte_feb(num):
    if num == 0 or num == 1:
        return num
    
    if num not in memoization:
        memoization[num] = calcualte_feb(num-1) + calcualte_feb(num-2)
    
    return memoization[num]

feb_num = calcualte_feb(5)
print(feb_num)