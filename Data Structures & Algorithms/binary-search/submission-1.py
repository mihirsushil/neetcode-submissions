class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums)-1  # pointers 

        while l <= r: # could be just  nums = [1]
            m = (l+r) // 2 # start in middle of nums 

            if nums[m]> target: # if greater it should be in first half
                r = m-1
            elif nums[m] < target: # if less it shoul be in the second half 
                l = m+1
            else: # if equal return index 
                return m 
        return -1 # else return -1 