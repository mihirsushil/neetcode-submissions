class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures) #  make the arr w all 0s 

        stack =[] # stack w/temps 

        for d,t in enumerate(temperatures): # looking at temps and having a number attatched with it too
            while stack and  t > stack[-1][1]: # looks at if stack empty and end of stack and the temp to sicne its a tuple, while bc more tuples can be in it. 1 bc its the second index of tuple. 0 would be first
                stackIndex,stackTemp = stack.pop() # if agreess that pop both
                arr[stackIndex] = (d- stackIndex) # look at arr and chang how many days in between 
            stack.append((d,t)) # appending tuple to stack 
        return arr
                 