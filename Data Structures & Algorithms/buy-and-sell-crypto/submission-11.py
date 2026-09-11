class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        start_index = 0 

        for i in range(1,len(prices)):
            window_diff = prices[i] - prices[start_index]

            if window_diff <= 0:
                start_index = i 
            else:
                maximum = max(window_diff, maximum)
        
        return maximum 





            

       



        