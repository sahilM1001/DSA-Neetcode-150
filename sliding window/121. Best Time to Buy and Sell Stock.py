# EASY
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Approach 1

def maxProfit(prices):
    maxProfit = 0
    left = 0
    right = 1
    while right < len(prices):
        currProfit = prices[right] - prices[left]
        if(prices[left] < prices[right]):
            maxProfit = max(maxProfit,currProfit)
        else:
            left = right
        right+=1
    return maxProfit

# Approach 2
def maxProfit_2(prices):
    max_profit = 0
    for i in range(len(prices)):
        slice = prices[i+1:]
        if len(slice) > 0:
            curr_profit = max(slice) - prices[i]
            max_profit = max(max_profit, curr_profit)

    return max_profit