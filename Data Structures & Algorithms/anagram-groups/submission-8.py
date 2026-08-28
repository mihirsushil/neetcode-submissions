class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list) # dictionary with starting values of 0 and we say that keys are goign to be a list  

        for s in strs:
            count = [0] * 26 # list where everythign is 0: [0,0,0,...] 26 times

            for c in s: 
                count[ord(c) - ord('a')] += 1 # we get a val due to ord and add it to count 

            arr[tuple(count)].append(s) # since count is list we make it a tuple so we the key is immuatable(all keys are like that) 

        return(list(arr.values())) # return only the values of dictionary 
