class Solution:
    def numRescueBoats(self, people, limit):
        '''
        Inputs -> list of integers, int defining the target
        Outputs -> int defining the # of boats
        Assumptions -> 
            - not sorted
            - everyone would be able to cross the river
            - there's at least 1 person to cross
            - only max of 2 people can cross on the boat
        Edge cases ->
            - if there's 1 person then there's 1 boat required
            - n boats required for n people (no two people can add up to the limit)
        Examples ->
            people = [1], limit = 1, boats = 1
            people = [3,2,4,3], limit = 4, boats = 4
            people = [1,2,3,4], limit = 3, boats = 3
        Algo ->
            - sort the people
            - keep pointer at lightest (first) and heaviest (last)
            - if their weight is bigger, take the heavier alone, and decrement its index
            - if their weight is less than limit, take both, increment and decrement both indices resp.
        Complexity -> O(nlog(n)) * O(n) = O(n^2log(n)), space = O(n)
        '''
        boats = 0
        
        if len(people) == 1:
            boats += 1
            return boats
    
        #sort list of people
        people.sort()
        
        #keep track of lightest and heaviest person
        first_index = 0
        last_index = len(people) - 1
        
        while first_index <= last_index:
            first_person = people[first_index]
            second_person = people[last_index]
            total_weight = first_person + second_person
            
            #if the weight is less than limit, take both people
            if total_weight <= limit:
                first_index += 1
                last_index -= 1
            else: #take last person by them selves
                last_index -= 1
            
            boats += 1
        
        return boats
            
        
people = [1,2,2,3]
limit = 3
solution = Solution()
print(solution.numRescueBoats(people, limit))
