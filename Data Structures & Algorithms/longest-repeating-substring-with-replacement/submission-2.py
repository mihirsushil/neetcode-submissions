class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0 

        for target in set(s):
            l = 0 
            count = 0 
            for i in range(len(s)):
                if s[i]!= target:
                    count += 1 
                while count >k:
                    if s[l]!= target:
                        count-=1
                    l+=1 
                res = max(res, i-l +1)
        return res 
        
            
        
        