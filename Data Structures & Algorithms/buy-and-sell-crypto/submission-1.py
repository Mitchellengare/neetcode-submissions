class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxProf = 0

        for r in range(1, len(prices)):
            if prices[l]>prices[r]:
                l=r
            else:
                profit = prices[r]-prices[l]
                maxProf = max(maxProf, profit)
        return maxProf
        