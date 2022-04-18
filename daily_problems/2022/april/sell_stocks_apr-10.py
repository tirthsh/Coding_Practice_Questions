def buy_sell_stocks(stocks):
    if not stocks or len(stocks) == 0:
        return None

    max_profit = 0
    buy = stocks[0]

    for i in range(1,len(stocks)):
        sell = stocks[i]
        tmp_profit = sell - buy

        if tmp_profit > max_profit:
            max_profit = tmp_profit
        elif buy > sell:
            #since its cheaper to buy at stocks[i], replace buy val with stocks[i]
            buy = sell
    
    return max_profit

stocks = [9, 11, 8, 5, 7, 10]

print(buy_sell_stocks(stocks))