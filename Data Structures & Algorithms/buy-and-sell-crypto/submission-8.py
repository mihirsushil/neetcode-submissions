class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0 

        for i in range(len(prices)):
            for k in range(i+1,len(prices)):
                diff = prices[k] - prices[i]
                maximum = max(maximum,diff)
        return maximum




        