class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list1 =[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                list1.append(prices[j]-prices[i])
        print(list1)
        if not list1:
            return 0 
        max_profit = max(list1)
        print(max_profit)
        if max_profit < 0:
            return(0)
        else:
            return(max_profit)
            
             
      
        
        
    
          