class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr_1 =[]
        count = 0 
        while count!= 2:
            for n in nums:
                arr_1.append(n)
            count +=1 
        return arr_1
        
        