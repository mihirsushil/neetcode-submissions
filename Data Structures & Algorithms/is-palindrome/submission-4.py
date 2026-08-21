class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        ALPHANUMERIC = 'abcdefghijklmnopqrstuvwxyz0123456789'

        arr_1 = []

        for i in s:
            if i in ALPHANUMERIC:
                arr_1.append(i)
           
        new_str = ''.join(arr_1)

        return new_str == new_str[::-1]

        

        