class Solution:
    def coinChange(self, coins, amount):
        '''
        Input -> list of numbers rep. list of coins, int rep. amount
        Output -> int rep. number of coins to make amount
        Assumptions -> infinte # of each kind of coin exists
        Edge cases -> no coins can make the amount, amount is 0
        Examples ->
            coins = [1,2,5], amount = 11, output = 3 [5,5,1]
            coins = [2], amount = 3, output = -1
            coins = [1], amount = 0, output = 0
        Algo ->
        Complexity ->
        '''
        
        #make a dp array of size amount + 1 (need to account for how many coins we need to make amount = 0)
        #dp array will rep. how many coins do we need to make dp[i], where i is the amount 
        #i.e how many coins do we need to make 1 amount, 5 amount, 20, etc
        #the # of coins will be the least # of coins
        dp = [amount+1] * (amount+1)
        #it takes 0 coins to make amount = 0
        dp[0] = 0
        
        #fill the dp array to amount + 1, where you are finding least # of coins needed from 0-amount+1
        for i in range(0, amount+1):
            #go through list of coins and see if you can make the amount i in least # of coins
            for j in range(0, len(coins)):
                #check if we can use the current coin
                if coins[j] <= i:
                    #take minimum of whatever is calculated at dp[i] and if we had used the current coin
                    #thats why we need to add +1 to rep. we're using coins[j]
                    #minimum works bc by default each value is amount+1 at dp[i] (line 20)
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        
        #remember our initial amount at dp[i] was amount + 1
        if dp[amount] < amount + 1:
            return dp[amount]
        return -1
                    
                
        
coins = [1,2,3]
amount = 7
solution = Solution()
print(solution.coinChange(coins, amount))