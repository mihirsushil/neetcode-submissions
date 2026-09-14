class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic, t_dic = {}, {}

        for a ,b in zip(s,t):
            if a in s_dic and s_dic[a] != b:
                return False
            if b in t_dic and t_dic[b] != a:
                return False 
            s_dic[a] = b
            t_dic[b] = a 
        return True              