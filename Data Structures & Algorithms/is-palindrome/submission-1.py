class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        s = ''.join(char for char in s if char  in alphanumeric)
        s = s.lower()
        print(s)
        if s == s[::-1]:
            return True 
        else:
            return False