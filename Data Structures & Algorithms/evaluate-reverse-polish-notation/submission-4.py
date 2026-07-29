class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for r in range(len(tokens)):
            if tokens[r] in "+-*/":
                a,b=stack.pop(),stack.pop()
                if tokens[r]=="+":
                    stack.append(a+b)
                elif tokens[r]=="-":
                    stack.append(b-a)
                elif tokens[r]=="*":
                    stack.append(a*b)
                else:
                    stack.append((int(b/a)))
            else:
                stack.append(int(tokens[r]))
        return stack[0]
        