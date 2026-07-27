class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_str = {}
        for s in strs: 
            str = "".join(sorted(s))
            if str in new_str:
                new_str[str].append(s)
            else:
                new_str[str] = [s]
        return list(new_str.values())



        