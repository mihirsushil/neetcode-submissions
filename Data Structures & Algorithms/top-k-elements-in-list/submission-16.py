class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} # 

        freq = [[] for i in range(len(nums) +1 )] # an arr of arrs of len(nums) +1, since there could be only one number found in the arr 

        for n in nums: # loop through nums and initializes the count as 0 and adds ones every time 
            count[n] = count.get(n,0) +1 
        
        for n,c in count.items(): # looks at keys and vals in count and sorts them into arr by count
            freq[c].append(n)

        arr = []
        

        for i in range(len(freq) -1,-1,-1): # starts from end, goes down by one, and goes until beg. of arr
            for n in freq[i]:
                arr.append(n)
                if len(arr) == k:
                    return arr 

            
            

