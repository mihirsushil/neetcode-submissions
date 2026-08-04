class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = {}
        for n in nums:
            count[n] = count.get(n,0) + 1 
        ans = []
        for keys, values in count.items():
            ans.append((values, keys))
        ans = sorted(ans,reverse=True)
        ans = ans[:k]
        result = []
        for values, keys in ans:
            result.append(keys)
        return result 