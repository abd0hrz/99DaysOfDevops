class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([y - x for x, y in zip(prices[0:-1], prices[1:]) if x < y])
