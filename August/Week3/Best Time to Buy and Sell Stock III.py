# Best Time to Buy and Sell Stock III
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def getans(i, prices, k, flag, hashmap):       
            
            if i>=(len(prices)) or k==0:
                return 0
            
            key = f'{str(i)}+" "+{str(flag)}+" "+{str(k)}'
            if key in hashmap:
                return hashmap[key]
            
            x = 0
            
            if not flag:
                buy = getans(i+1, prices, k, not flag, hashmap)-prices[i]
                notbuy = getans(i+1, prices, k, flag, hashmap)
                
                x = max(buy, notbuy)
            else:
                sell = getans(i+1, prices, k-1, not flag, hashmap)+prices[i]
                notsell = getans(i+1, prices, k, flag, hashmap)
                
                x = max(sell, notsell)
                
            hashmap[key] = x
            return x
        return getans(0, prices, 2, False, dict())
            
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        
        min_price = float('inf')
        dp = [0] * n
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            dp[i] = max_profit

        max_price = 0
        for i in range(n-1, 0, -1):
            if prices[i] > max_price:
                max_price = prices[i]
                continue
            curr_max = max_price - prices[i]
            if curr_max + dp[i - 1] > max_profit:
                max_profit = curr_max + dp[i - 1]

        return max_profit
'''