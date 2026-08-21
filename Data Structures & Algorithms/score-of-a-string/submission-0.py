class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for k in range(len(s)-1):
            count += abs(ord(s[k]) - ord(s[k+1]))
        return count 
        

        