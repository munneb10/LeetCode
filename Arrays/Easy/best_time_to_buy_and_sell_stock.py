"""
Question Link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size=len(prices)
        arr=[0]*size
        max_profit=0
        for p in range(size-1,-1,-1):
            if prices[p]>max_profit:
                max_profit=prices[p]
            arr[p]=max_profit
        max_profit=0
        for i in range(size):
            if arr[i]-prices[i]>max_profit:
                max_profit=arr[i]-prices[i]
        return max_profit