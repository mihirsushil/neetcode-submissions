class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        dic = {}

        for i in nums:
            dic[i] = dic.get(i,0) +1

        for k,v in dic.items():
            if v % 2 != 0:
                return False 
        return True
        