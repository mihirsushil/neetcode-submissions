class Solution:
    def isValid(self, s: str) -> bool:

        dic = {")":"(", "}":"{", "]":"["}
        arr = []

        for c in s:
            if c in dic.keys():
                if arr and arr[-1] == dic[c]:
                    arr.pop()
                else:
                    return False 
            else: 
                arr.append(c)
        if not arr: 
            return True
        else: 
            return False