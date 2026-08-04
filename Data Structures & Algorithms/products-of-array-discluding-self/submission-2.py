class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_1 = []
        for k in range(len(nums)):
            arr_2 = []
            for i in range(len(nums)):
                if i == k:
                    continue
                arr_2.append(nums[i])
            ans = 1 
            for a in arr_2:
                ans *= a
            arr_1.append(ans)
        return arr_1

        


    