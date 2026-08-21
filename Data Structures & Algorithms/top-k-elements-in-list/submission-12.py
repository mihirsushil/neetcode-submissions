class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count ={}

        for n in nums:
            count[n] = count.get(n,0) + 1
        
        arr = []

        for keys,val in count.items():
            arr.append((val,keys))
        
        arr = sorted(arr,reverse=True)

        arr = arr[:k]
        ans = []
        for k, v in arr:
            ans.append(v)    

        return ans 

       

            
    

        