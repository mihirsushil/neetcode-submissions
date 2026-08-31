class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p,s) for p,s in zip(position,speed)] # making it a tuple and going throught both arrays 
        stack = []

        for p,s in sorted(arr)[::-1]: # looking at postion and sorting form high
            stack.append((target-p)/s) # time it takes
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if stack[-1] greater then stack[-2] pop [-1] bc its now a fleet and repeat 
                stack.pop()
        return len(stack) # number of fleets 
        









        