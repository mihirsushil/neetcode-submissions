class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l,r = 0 , len(s)-1

        while l < r:
            while l < r and not self.isAlpha(s[l]): # calling the func like this 
                l+=1 
            while l < r and not self.isAlpha(s[r]):
                r-=1
            if s[r] != s[l]:
                return False
            # if both characters are same then move to next one 
            l+=1 
            r-=1 

        return True 




    def isAlpha(self,c):
        return (ord('a') <= ord(c) <= ord('z') or 
        ord('0')<= ord(c) <= ord('9'))
                
           

  


        
  

        