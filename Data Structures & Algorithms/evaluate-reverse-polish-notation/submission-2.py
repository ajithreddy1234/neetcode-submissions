class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n=len(tokens)
        stack=[]
        for i in range(n):
            if tokens[i] not in "+*-/":
                stack.append(int(tokens[i]))
            else:
                a=stack.pop()
                b=stack.pop()
                if tokens[i]=="+":
                    stack.append(a+b)
                elif tokens[i]=="*":
                    stack.append(a * b)
                elif tokens[i]=="-":
                    stack.append(b-a)
                if tokens[i]=="/":
                    stack.append(int(float(b) / a))
        return stack[0]
                


        