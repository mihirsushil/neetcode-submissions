class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = {}
        for c in words[0]:
            dic[c] = dic.get(c, 0) + 1

        for word in words[1:]:
            dic_2 = {}
            for c in word:
                dic_2[c] = dic_2.get(c, 0) + 1
            for c in dic:
                dic[c] = min(dic[c], dic_2.get(c, 0))   # merge runs once, after dic_2 is fully built

        ans = []
        for key, value in dic.items():
            ans.extend([key] * value)
        return ans

    
            
             


    

        

        
            



        