#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit_brute_force(self, prices):
        '''
        Inputs -> list of integers
        Output -> int (profit val)
        Assumptions -> All positive integers
        Edge cases -> there may be no profit
        Examples -> prices = [1,2,3,4,5], profit = 4 (5-1)
                    prices = [3,2,1,4,7], profit = 6 (7-1)
        Algorithm ->
        Complexity -> O(n)
        '''
        
        max_profit = 0
        
        for i in range(0, len(prices)):
            curr_val = prices[i]
            for j in range(i+1, len(prices)):
                next_val = prices[j]
                
                if (next_val - curr_val ) > max_profit:
                    max_profit = next_val - curr_val
        
        return max_profit
                
    def maxProfit(self, prices):
        '''
        Inputs -> list of integers
        Output -> int (profit val)
        Assumptions -> All positive integers
        Edge cases -> there may be no profit
        Examples -> prices = [1,2,3,4,5], profit = 4 (5-1)
                    prices = [3,7,1,4,6], profit = 5 (6-1)
                    prices = [4,7,1], profit = 3
        Algorithm ->
        Complexity -> O(n)
        '''
        
        max_profit = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            sell = prices[i]
            temp_profit = sell - buy
            
            if temp_profit > max_profit:
                max_profit = temp_profit
            elif buy > sell: 
                '''
                If you can buy it for cheaper tomorrow, why buy it today
                If tomorrow's buy price is cheaper than today, you're guaranteed to make at least the same profit as today, if not more 
                '''
                buy = sell
        
        return max_profit