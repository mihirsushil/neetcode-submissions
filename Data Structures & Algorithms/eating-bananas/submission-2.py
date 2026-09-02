class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_time = r 

        while l <= r:
            k = (l+r) // 2
            hr = 0 
            for p in piles:
                hr += math.ceil(p/k)
            if hr <= h:
                min_time  = min(min_time, k)
                r = k-1 
            else: 
                l = k+1 
        return min_time

           

       