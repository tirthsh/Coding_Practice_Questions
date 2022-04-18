class Solution:
    def totalFruit(self, fruits):
        if fruits == None or len(fruits) == 0:
            return 0
        
        #where you start is very important
        #determine where to start!
        
        max_fruit_count = 0
        tmp_fruit_count = 0

        #keep track of two baskets, could prob use hashmap {tree: latest index of where it occurs}
        #see solution #2
        basket_1 = []
        basket_2 = []
        
        start = 0
        end = 0
        
        #moving window approach
        while end < len(fruits):
            #if we dont have anything in the basket1, or if that same fruit is in basket, we can add more fruits to it
            if  len(basket_1) == 0 or fruits[end] in basket_1:
                basket_1.append(fruits[end])
                end += 1
                tmp_fruit_count += 1
            #if we dont have anything in the basket2, or if that same fruit is in basket, we can add more fruits to it
            elif len(basket_2) == 0 or fruits[end] in basket_2:
                basket_2.append(fruits[end])
                end += 1
                tmp_fruit_count += 1
            else:
                #neither of the basket can add this fruit since this fruit is of type 3
                #update max length
                #end - start -> instead of tmp_fruit_count
                if tmp_fruit_count > max_fruit_count:
                    max_fruit_count = tmp_fruit_count
                
                #next time start 1 after and also empty the baskets
                start += 1
                end = start
                basket_1 = []
                basket_2 = []
                tmp_fruit_count = 0
        
        #in the case the last iteration has a higher count than max
        if tmp_fruit_count > max_fruit_count:
            return tmp_fruit_count
        else:
            return max_fruit_count

    def totalFruit_hashmap(self, fruits):
        if fruits == None or len(fruits) == 0:
            return 0
        
        max_fruit_count = 1
        start = 0
        end = 0 
        mapping = {}

        while end < len(fruits):
            #only include 2 types of fruits
            if len(mapping) <= 2:
                #store key has fruit type, and value as the index of that fruit 
                #it'll be the last index so far of this fruit type
                mapping[fruits[end]] = end
                end += 1
            else:
                #if there are already 2 fruit types in the basket
                minimum = len(fruits) - 1
                #find the earlier index and start from +1 after that index next time
                for each_val in list(mapping.values()):
                    minimum = min(minimum, each_val)
                
                start = minimum + 1
                #get rid of the first type
                mapping.pop(fruits[minimum])

            #update fruit count
            max_fruit_count = max(max_fruit_count, end - start)

        return max_fruit_count

        
                
solution = Solution()
fruits1 = [1,2,1]
fruits2 = [0,1,2,2]
fruits3 = [1,2,3,2,2]
fruits4 = [3,3,3,1,2,1,1,2,3,3,4]
fruits5 = []

# print(solution.totalFruit(fruits1))
# print(solution.totalFruit(fruits2))
# print(solution.totalFruit(fruits3))
# print(solution.totalFruit(fruits4))

print(solution.totalFruit_hashmap(fruits1))