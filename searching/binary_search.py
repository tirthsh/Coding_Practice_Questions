def binary_search_iterative(nums, target):
    '''
    Look through A SORTED LIST of nums, and check if a number exists or not in O(log(N)) time

    Algo:
    Find the midpoint of a list, check if the midpoint is what you're looking for. If you are great, great - we're done.
    If we're not, check if our mid number is greater or less than our target.

    If it's greater:
        - means our number must be in the left of the midpoint, so we make our end pointer to mid-1
    If it's less:
        - means our number must be in the right of the midpoint, so we make our start pointer to mid + 1
    '''

    if len(nums) == 0:
        return -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        curr_num = nums[mid]

        #if curr number is bigger, means we need to move window to the left
        if curr_num > target:
            end = mid - 1
        #if curr number is less, means number must on the right half, so start from mid+1
        elif curr_num < target:
            start = mid + 1
        else:
            return mid
    
    return -1

def binary_search_resursive(start, end, nums, target):
    if start <= end:
        mid = (start + end) // 2

        if nums[mid] > target:
            return binary_search_resursive(start, mid - 1, nums, target)
        elif nums[mid] < target:
            return binary_search_resursive(mid + 1, end, nums, target)
        else:
            return mid

    return -1

nums = [ 2, 3, 4, 10, 40 ]
target = 10

print(binary_search_iterative(nums, target))
print(binary_search_resursive(0, len(nums)-1, nums, target))