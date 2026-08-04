class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_arr = []
        for k in range(len(nums)):
            arr = []
            for i in range(len(nums)):
                if i == k:
                    continue
                else:
                    arr.append(nums[i])
            ans = 1
            for n in arr:
                ans *= n
            ans_arr.append(ans)
        return ans_arr




    