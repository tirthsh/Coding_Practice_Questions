def witnesses(witness_list):
    if not witness_list or len(witness_list) == 0:
        return 0
    
    dp = [witness_list[len(witness_list)-1]] * len(witness_list)
    witness_count = 1
    print(dp)

    for i in range(len(witness_list)-2, -1, -1):
        #what if its the same height? - clarify
        if witness_list[i] > dp[i+1]:
            dp[i] = witness_list[i]
            witness_count += 1
        else:
            dp[i] = dp[i+1]
        
        print(dp)
    
    return witness_count


witness_list = [3, 6, 3, 4, 1]
print(witnesses(witness_list))

witness_list = [1,1,1,1,6]
print(witnesses(witness_list))

witness_list = [3,2,1]
print(witnesses(witness_list))