class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # making an arr with all postion starting w/ 1 
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # pos startign w/ prefix of last i val 
            prefix *= nums[i] # multiplying the last postions with curr i, for next iteration prefix
        postfix = 1 
        for i in range(len(nums)-1,-1,-1): # starting from end go to 0th pos(-1) and delimeter is 1 
            res[i] *= postfix # pos startign w last postfix val from end and then multiplyin the prefix 
            postfix *= nums[i] # postifix to inc curr num 
        return res




    