#Bottom-up 
#It's implemented with iteration and starts at the base cases
def fib(num):
    #default two values
    dp = [-1] * (num+1)

    #base case
    dp[0] = 0
    dp[1] = 1

    #append new fib calculated in the dp list
    for i in range(2, num+1):
        dp[i] = dp[i-2] + dp[i-1]
    
    return dp[num]

feb_num = fib(5)
print(feb_num)