class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 

        freq = [[] for i in range(len(nums)+1)] # every freq[n] is an arr so sum like freq = [[],[],..]
        for n in nums:
            count[n] = count.get(n,0) + 1 

        for n, c in count.items():
            freq[c].append(n)   

        arr = []

        for i in range(len(freq) -1 ,0,-1): # descending, to 0, delimeter is -1 
            for n in freq[i]:
                arr.append(n)
                if len(arr) == k:
                    return arr


