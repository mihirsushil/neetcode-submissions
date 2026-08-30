class Solution:
    def isValid(self, s: str) -> bool:

        dic = {")":"(", "}":"{", "]":"["} # goal is to look at closing braces and append open 

        stack = [] # initializing stack 

        for c in s:
            if c in dic.keys(): # if closing 
                if stack and stack[-1]==dic[c]: # if stack not empty and last index of stack matches the the dic val of c 
                    stack.pop() # pop it 
                else: # if not then it is not proper stack and it is false 
                    return False
            else: # if not closing append to stack 
                stack.append(c)
        if not stack: # if stack empty then return true
            return True
        else:
            return False 