class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 , len(nums) -1 
        min_rn = nums[0]
        
        if min_rn < nums[r] or l == r:
            return min_rn 
        else: 
            while l <= r: 
                m = (l+r) // 2
                min_rn = min(min_rn, nums[m])
                if nums[m] > nums[r]:
                    l = m+1 
                else: 
                    r = m-1 
        return min_rn




        