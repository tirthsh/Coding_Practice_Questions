def quick_sort(nums):
    '''
    Recursion -> O(nlog(N)):
    
    Select a pivot, and everything less than pivot, keep it to left, and greater than pivot, keep it to left.
    Select a new pivot from the two lists and repeat until entire list is sorted. 

    Example:

    nums = [0, 9, 3, 8, 2, 7, 5]

    <- root call ->
    pivot = 5
    
    less_than_pivot = [0, 3, 2] - recursive call #1 
    greater_than_pivot = [9, 8, 7] - recursive call #2 

    return: [0,2,3,5,7,8,9] -> from all below calls

    <- recursive call #1 (less than pivot from above) ->
    nums = [0,3,2]
    pivot = 2

    less_than_pivot = [0]
    greater_than_pivot = [3]

    return: [0,2,3] -> already sorted

    <- recursive call #2 (greater than pivot from above) ->
    nums = [9,8,7]
    pivot = 7

    less_than_pivot = []
    greater_than_pivot = [9,8] -> recursive call #3 
    return: [8,9] -> from below

    <- recursive call #3 (greater than pivot from above) ->
    nums = [9,8,7]
    pivot = 8

    less_than_pivot = []
    greater_than_pivot = [9]

    return: [8,9]
    '''

    if len(nums) <= 1:
        return nums
    

    #select last elem as pivot
    pivot = nums.pop()

    less_than_pivot = []
    greater_than_pivot = []

    for num in nums:
        if num < pivot:
            less_than_pivot.append(num)
        else:
            greater_than_pivot.append(num)
        
    
    #recurisely call quick sort on left and right of pivot 
    #need to make sure we also append pivot in the entire list (middle of the two)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

nums = [2,0,2,1,1,0]
print(quick_sort(nums))