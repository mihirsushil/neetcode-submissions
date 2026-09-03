class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles) # slowest, and fastest time to eat. 
        res = r # we know this will work for sure b/c takes len(piles) which we are assured 

        while l <= r :
            k = (l+r) // 2 # mid of lowest and highest 
            hrs = 0 # tracker 
            for i in piles: 
                hrs+= math.ceil(i/k) # take the upper limit of hours to take 
            if hrs <= h:# if less then 
                res = min(res, k) # take the min of fastest and k val
                r = k-1 # since works we check if there are lower vals that can still work 
            else: 
                l = k+1 # since it didn't work there mightbe sum bigger val that could work 
        return res         

           

       