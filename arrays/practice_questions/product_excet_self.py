#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf_bruteForce(self, nums: List[int]) -> List[int]:
        '''
        Input -> list of nums
        Output -> lsit of nums
        Assumptions -> there exists at least 2 nums
        Edge cases -> 
        Examples -> 
        Algo ->
        Complexity ->
        '''
        
        product_list = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                else:
                    product_list[i] = product_list[i] * nums[j]
        
        return product_list
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Input -> list of nums
        Output -> lsit of nums
        Assumptions -> there exists at least 2 nums, no use of division allowed
        Edge cases -> 
        Examples -> 
        Algo ->
        Complexity -> O(n)
        '''
        
        #make all products by default to 1
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        product_list = [1] * len(nums)
        
        #calculate product of everything that's left of i
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        print(left_product)
        
        #calculate product of everything that's right of j
        for j in range(len(nums) - 2, -1, -1):
            right_product[j] = right_product[j+1] * nums[j+1]
        
        print(right_product)
        
        #product of k is product of left of k * product of right of k
        for k in range(0, len(nums)):
            product_list[k] = left_product[k] * right_product[k]
        
        return product_list
        