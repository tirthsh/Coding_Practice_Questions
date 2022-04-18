class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        '''
        Input -> integer n, list of integers
        Output -> integer - minimum cost
        Assumptions -> n >= 2
                    len(cuts) >= 1
                    1 <= cuts[i] <= n-1
        '''

        cuts = [0] + sorted(cuts) + [n]

        @cache
        def findCost(start, end):
            results = []
            if end-start <= 1:
                return 0
            
            for i in range(start + 1, end):
                current_cost = cuts[end] - cuts[start]
                right_cost = findCost(i, end)
                left_cost = findCost(start, i)
                results.append(current_cost + left_cost + right_cost)

            return min(results)
        
        return findCost(0, len(cuts) - 1)
