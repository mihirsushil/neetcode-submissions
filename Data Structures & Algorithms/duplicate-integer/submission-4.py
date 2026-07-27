class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = len(nums)
        true_count = len(set(nums))

        if count == true_count:
            return False 
        else:
            return True