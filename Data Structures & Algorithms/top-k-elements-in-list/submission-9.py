class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = {}
        for n in nums: 
            if n in count: 
                count[n]+=1 
            else:
                count[n] =1 

        ans = []
        for keys, values in count.items():
            ans.append((values, keys))
        ans = sorted(ans,reverse=True)
        ans = ans[:k]
        return[key for values, key in ans]