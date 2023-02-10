# 5. Maximizing Profit from Stocks

# Your algorithms have become so good at predicting the market that you now know what the share price of Silly Purple Toothpicks Inc. 
# (SPT) will be for a number of minutes going forward. Each minute, your high frequency trading platform allows you to either buy one share of SPT, 
# sell any number of shares of SPT that you own, or not make any transaction at all. Find the maximum profit you can obtain with an optimal trading strategy.

# Purchases are negative and sales are positive cash flows in the following equations. 
# For example, if predicted prices over the next n = minutes are prices = [3, 4, 5, 3, 5, 2], one way to the best outcome is to purchase a share in each of the 
# first 2 minutes for cash flows -3 +-4 = -7, then sell them at the third minute for 2 * 5 = 10. 
# Purchase a share in the 4th minute for 3 and sell it in the 5th minute for 5. Total profits are -3 - 4 + 10-3+5=5. 
# Another way to the same outcome is to purchase a share in each of the 1st, 2nd and 4th minutes for -3 - 4 - 3 = -10, 
# do nothing at minute 2 then sell all three shares at 5 (total 3*5 = 15) on the 5th minute, again for a total profit of -10 + 15 = 5. 
# There is no reason to purchase in the last minute as there is no time to sell.



# Function Description:
# Complete the maximumProfit function in the editor below. The function must return a long integer that denotes the maximum possible profit.

# maximumProfit has the following parameter:
# price: an array of n integers that denote the stock prices at minutes 1 through n.

# Test case:
# [5,3,2] = 0
# [1,2,100]= 197
# [1,3,1,2] = 3

# Explanation:
# For the first case, no profit can be had because the share price never increases, so do nothing. 
# For the second case, buy one share in each of the first two minutes, then sell both shares in the third minute.
# For the third case, buy one share in the first minute, sell one in the second minute, buy one share in the third minute, 
# and sell one share in fourth minute to get a total profit of 3.


def maximumProfit(price):
    # Write your code here
    profit = 0; max_so_far = price[len(price)-1]
    
    for i in range(len(price)-2, -1, -1):
        if price[i] < max_so_far:
            profit += max_so_far - price[i]
        else:
            max_so_far = price[i]
    return profit

print(maximumProfit([5,3,2]))
print(maximumProfit([1,2,100]))
print(maximumProfit([1,3,1,2]))