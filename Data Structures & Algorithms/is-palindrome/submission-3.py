class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        r = []
        alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for c in s:
            if c in alphanumeric:
                r.append(c)
        r = ''.join(r)
        print(r)
        print(r[::-1])
        return r == r[::-1]