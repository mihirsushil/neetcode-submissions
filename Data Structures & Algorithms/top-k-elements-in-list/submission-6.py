class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        sorted_values = sorted(dic.values(), reverse=True)
        ans_values = sorted_values[:k]

        ans = []
        for x in ans_values:
            for key, value in dic.items():
                if value == x and key not in ans:
                    ans.append(key)
                    break
        return ans
        





                    