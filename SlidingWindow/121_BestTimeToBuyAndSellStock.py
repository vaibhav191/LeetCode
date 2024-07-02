import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s, p = 0, 0, 0
        while s < len(prices):
            if p < prices[s] - prices[b]:
                p = prices[s] - prices[b]
            if prices[s] < prices[b]:
                b = s
            s += 1
        return p
