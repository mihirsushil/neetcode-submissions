class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens: 
            if c == "+":
                new_c = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(new_c)            
            elif c == "-":
                new_c = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new_c)
            
            elif c == "/":
                new_c = int((stack[-2]) /(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(new_c)
            
            
            elif c == "*":
                new_c = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(new_c)
            

            else:
                stack.append(int(c))
        return stack[0]

        